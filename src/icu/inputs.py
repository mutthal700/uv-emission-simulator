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

# --- CO2 generation, per person, m3/s ---------------------------------------
# Patient: direct ICU measurement of mechanically ventilated adults.
# Unit conversion from source-reported mL/min; derived, not source-reported.
VCO2_PATIENT_KAGAN = 244.5 / 60 / 1e6        # Kagan, Crit Care 22:186 (2018)
VCO2_PATIENT_KAGAN_SD = 85.9 / 60 / 1e6
VCO2_PATIENT_ROUSING = 273.0 / 60 / 1e6      # Rousing, Ann Intensive Care 6:16 (2016)
VCO2_PATIENT_ALTUNALAN = 188.362 / 60 / 1e6  # Altunalan, BMC Anesthesiol 26:89 (2026)

# Staff and visitors: Persily & de Jonge, Indoor Air 27:868-879 (2017), Table 4,
# male 21-<30, at 273 K and 101 kPa. The met level is a DECLARED parameter with
# a sensitivity range, not a sourced ICU value: ISO 8996:2021 is blocked.
PERSILY_M21_30 = {1.0: 0.0039, 1.2: 0.0048, 1.4: 0.0056, 1.6: 0.0064}
VCO2_STAFF_BY_MET = {met: v / 1000 for met, v in PERSILY_M21_30.items()}  # m3/s

# --- Energy reference values -------------------------------------------------
# Code minima, not measured equipment performance.
CHILLER_COP_LT_260KW = 2.8   # ECBC 2017, 9.4.2.8, Table 9-5
CHILLER_COP_GE_260KW = 3.0   # ECBC 2017, 9.4.2.8, Table 9-5
FAN_MECH_EFF = {"ECSBC": 0.65, "ECSBC+": 0.70, "SuperECSBC": 0.75}  # ECSBC 2024, 6.3.1

# --- Blocked -----------------------------------------------------------------
OUTDOOR_CO2_PPM = _Blocked(
    "outdoor CO2 baseline",
    "a sourced outdoor CO2 concentration for each climate zone",
)
SYSTEM_PRESSURE_DROP_PA = _Blocked(
    "system pressure drop at a stated duty point",
    "filter model clean/loaded dP plus duct and coil resistance",
)
ICU_PM_SIZE_DISTRIBUTION = _Blocked(
    "nonviable ICU PM size distribution",
    "dN/dlogDp or dM/dlogDp with instrument channel boundaries",
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
