"""Confirmed model inputs.

Every constant here is traceable to a primary document recorded in
docs/ICU_MODEL_INPUTS.md. Anything not yet sourced is a BLOCKED sentinel that
raises on use rather than silently defaulting.
"""

from dataclasses import dataclass


class BlockedInput(Exception):
    """Raised when the model needs a quantity that has no source yet."""


class _Blocked:
    """Fail-closed sentinel. Any use raises with the closing requirement."""

    def __init__(self, name: str, closes_with: str) -> None:
        self.name = name
        self.closes_with = closes_with

    def __float__(self):
        raise BlockedInput(f"{self.name} is not sourced. Closes with: {self.closes_with}")

    __add__ = __mul__ = __sub__ = __truediv__ = lambda self, other: float(self)


# --- Room geometry -----------------------------------------------------------
# AusHFG Room Data Sheet 1BR-ICU, Rev 2, 12.11.2025, page 1.
FLOOR_AREA_M2 = 25.00
CEILING_HEIGHT_M = 3.0
ROOM_VOLUME_M3 = FLOOR_AREA_M2 * CEILING_HEIGHT_M  # 75.0, gross geometric
BED_COUNT = 1

# Occupancy as listed on page 1: 1 patient + 1-2 visitors + 1-2 staff,
# plus 4-6 additional staff as required.
OCCUPANCY_BASE_MIN = 3
OCCUPANCY_BASE_MAX = 5
OCCUPANCY_SURGE_MAX = 11

# --- Duct --------------------------------------------------------------------
# Fixed by the researcher; length matches the physical rig (master section 4).
DUCT_SIDE_M = 0.3048
DUCT_AREA_M2 = DUCT_SIDE_M ** 2  # 0.092903, exactly 1 sq ft
DUCT_LENGTH_M = 6.0

# --- CO2 generation, per person ----------------------------------------------
# Per verified_co2_generation_source_audit, 2026-08-29. Volumetric rates are
# meaningless without their gas reference state, so each carries one.
#
# Altunalan et al. (2026) is EXCLUDED: the article's Results prose and Table 2
# contradict one another on VCO2 versus VO2, and the source does not permit a
# defensible choice between them.

R_GAS = 8.314462618  # J/(mol K)


class GasState:
    """A volumetric rate with its reference temperature and pressure."""

    def __init__(self, v_dot_m3_s: float, t_k: float, p_pa: float, basis: str):
        self.v_dot_m3_s = v_dot_m3_s
        self.t_k = t_k
        self.p_pa = p_pa
        self.basis = basis

    def to_molar(self) -> float:
        """mol/s. Preferred internal quantity: no reference-state ambiguity."""
        return self.p_pa * self.v_dot_m3_s / (R_GAS * self.t_k)

    def at_state(self, t_k: float, p_pa: float) -> float:
        """Ideal-gas conversion to another dry-gas state, m3/s."""
        return self.v_dot_m3_s * (t_k / self.t_k) * (self.p_pa / p_pa)


# Draeger Evita 4 reports CO2 production at STPD: 0 degC, 1013 hPa, dry.
# Instructions for Use, Edition 5, 2015-01, doc 9039485, Technical data, p176.
STPD_DRAEGER_T = 273.15
STPD_DRAEGER_P = 101300.0

# Persily & de Jonge (2017) Table 4 basis, stated in the text preceding Table 4.
PERSILY_T = 273.0
PERSILY_P = 101000.0

# Patient, Kagan et al., Critical Care 22:186 (2018). Six-hour block mean from
# the Evita 4 ventilator, cohort mean - not a universal patient emission factor.
VCO2_PATIENT_KAGAN = GasState(244.5 / 60 / 1e6, STPD_DRAEGER_T, STPD_DRAEGER_P,
                              "Draeger Evita 4 STPD")
VCO2_PATIENT_KAGAN_SD = 85.9 / 60 / 1e6

# Patient, Rousing et al., Ann Intensive Care 6:16 (2016). GE E-CAiOVX module;
# GE states standard temperature 0 degC and dry gas but NOT a numeric standard
# pressure, so this value must not be pressure-harmonised. Left unstated.
VCO2_PATIENT_ROUSING_M3_S = 273.0 / 60 / 1e6
VCO2_PATIENT_ROUSING_SD = 63.0 / 60 / 1e6
VCO2_PATIENT_ROUSING_PRESSURE_BASIS = _Blocked(
    "numeric standard pressure for the GE E-CAiOVX reference state",
    "a GE document stating the numeric standard pressure for the relevant "
    "monitor revision; until then Rousing cannot be exactly harmonised",
)

# Occupant SCENARIO, not a generic staff or visitor class: Persily & de Jonge
# (2017), Indoor Air 27(5):868-879, Table 4, MALE AGE 21 TO <30 row, p875.
# Applies to that sex/age class at Persily's mean body mass. Met level is a
# declared scenario parameter - ISO 8996:2021 is blocked.
VCO2_MALE_21_30_BY_MET = {
    met: GasState(v, PERSILY_T, PERSILY_P, "Persily 273 K / 101 kPa")
    for met, v in ((1.0, 3.90e-6), (1.2, 4.80e-6), (1.4, 5.60e-6), (1.6, 6.40e-6))
}

# --- Researcher-selected evaluation state ------------------------------------
# NOT a measured ICU condition. Any CO2 result computed at this state, and the
# resulting shift relative to the source reference states, is researcher-defined
# arithmetic and must never be presented as source data. Prefer the molar route
# until the actual room temperature and pressure are measured.
RESEARCHER_EVAL_T_K = 297.15
RESEARCHER_EVAL_P_PA = 101325.0

ROOM_ACTUAL_T_P = _Blocked(
    "measured ICU room temperature and pressure",
    "site measurement; until then any volumetric evaluation state is "
    "researcher-selected and results carry that label",
)


def source_at_eval_state(gas_state) -> float:
    """Researcher-selected evaluation state. Label results accordingly."""
    return gas_state.at_state(RESEARCHER_EVAL_T_K, RESEARCHER_EVAL_P_PA)


# --- Energy reference values -------------------------------------------------
# ECBC 2017 Table 9-5 minimum efficiencies for STANDARD-DESIGN chillers. These
# are code minima for a compliance baseline, not the efficiency of any ICU plant.
CHILLER_COP_LT_260KW = 2.8   # ECBC 2017, 9.4.2.8, Table 9-5
CHILLER_COP_GE_260KW = 3.0   # ECBC 2017, 9.4.2.8, Table 9-5

# The previous ECSBC entry conflated two different quantities: fan MECHANICAL
# efficiency and motor IE efficiency CLASS are not interchangeable and cannot be
# combined into one number.
FAN_EFFICIENCY = _Blocked(
    "fan total electrical efficiency at the duty point",
    "the official ECSBC 2024 tables read directly for the mechanical-efficiency "
    "requirement, and selected-equipment or measured data for actual fan, motor "
    "and drive efficiency; IE class is not a fan efficiency",
)

# --- Blocked -----------------------------------------------------------------
OUTDOOR_CO2_PPM = _Blocked(
    "outdoor CO2 baseline",
    "a sourced outdoor CO2 concentration for each climate zone",
)
SYSTEM_PRESSURE_DROP_PA = _Blocked(
    "system pressure drop at a stated duty point",
    "filter model clean/loaded dP plus duct and coil resistance",
)
K_DEPOSITION = _Blocked(
    "size-resolved deposition rate for this room",
    "a directly applicable deposition formulation plus the actual room "
    "surface-to-volume ratio, surface/material conditions, airflow regime and "
    "a compatible particle-size distribution. Generic non-ICU aerosol "
    "literature may not be inserted as an ICU input under the no-proxy rule",
)
ICU_PM_SIZE_DISTRIBUTION = _Blocked(
    "nonviable ICU PM size distribution",
    "dN/dlogDp or dM/dlogDp with instrument channel boundaries",
)
# Two distinct things, deliberately separated.
# A researcher declaration yields a LABELLED SENSITIVITY SCENARIO. It is not
# representative ICU data and cannot support an actual-ICU prediction.
STAFF_VISITOR_SCENARIO_DECLARED = None  # set to a declared composition to enable
                                        # sensitivity runs only

STAFF_VISITOR_OBSERVED = _Blocked(
    "observed staff and visitor composition for THIS ICU",
    "site roster composition plus activity categories and timing. Required for "
    "any actual-ICU prediction; a declared scenario is a sensitivity case only",
)
PATIENT_EXHAUST_PATH = _Blocked(
    "ventilator and breathing-circuit configuration for THIS ICU",
    "the specific ventilator model and circuit arrangement, and whether expired "
    "gas is discharged into the room or connected to scavenging/exhaust. A "
    "generic statement about how ICU ventilators usually behave is NOT "
    "sufficient and must not be substituted",
)
OCCUPANCY_SCHEDULE = _Blocked(
    "diurnal occupancy schedule",
    "hospital ICU SOP or IPC manual event timing (Stage C only)",
)


@dataclass(frozen=True)
class ViableBins:
    """Kim, Kim & Kim, Industrial Health 48(2):236-243 (2010), six Andersen stages.

    Stage 1 is open-ended above 7.0 um; any representative diameter for it is a
    modelling choice, not a measurement.
    """

    edges_um = ((0.65, 1.1), (1.1, 2.1), (2.1, 3.3), (3.3, 4.7), (4.7, 7.0), (7.0, None))
    icu_bacteria_total_cfu_m3 = 202
    icu_bacteria_respirable_cfu_m3 = 142
    icu_fungi_total_cfu_m3 = 65
    icu_fungi_respirable_cfu_m3 = 47
