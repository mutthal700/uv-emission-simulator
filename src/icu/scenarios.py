"""Guideline scenarios.

Revised per ICU_MODEL_INPUTS_EVIDENCE_AUDIT, 2026-08-30.

`ach_total = None` means the source states no air-change rate.
`blocked` means the normative row itself is not in evidence, so the scenario
carries no values at all and must not be simulated.
"""

from dataclasses import dataclass, field
from typing import Optional


@dataclass(frozen=True)
class FreshAirRule:
    """A minimum outdoor-air provision, source-specific.

    HTM 03-01:2021 sets both a fraction and a per-person floor; the controlling
    value is the greater. SHTM 03-01:2014 supplies only the fraction at its
    edition date. The two documents must not be combined.
    """

    min_fraction: Optional[float] = None
    min_l_s_per_person: Optional[float] = None
    locator: str = ""

    def controlling_m3_h(self, q_supply_m3_h: float, n_occupants: int) -> float:
        candidates = []
        if self.min_fraction is not None:
            candidates.append(self.min_fraction * q_supply_m3_h)
        if self.min_l_s_per_person is not None:
            candidates.append(self.min_l_s_per_person * n_occupants * 3.6)
        if not candidates:
            raise ValueError("no fresh-air provision defined for this source")
        return max(candidates)


@dataclass(frozen=True)
class Guideline:
    key: str
    document: str
    locator: str
    ach_total: Optional[float] = None
    ach_total_max: Optional[float] = None
    ach_outdoor: Optional[float] = None
    ach_outdoor_max: Optional[float] = None
    f_oa_fixed: Optional[float] = None
    fresh_air_rule: Optional[FreshAirRule] = None
    filter_descriptor: Optional[str] = None
    pressure: Optional[str] = None
    temp_c: Optional[tuple] = None
    rh_pct: Optional[tuple] = None
    blocked: str = ""

    @property
    def simulatable(self) -> bool:
        return not self.blocked and self.ach_total is not None


HTM_FRESH_AIR = FreshAirRule(
    min_fraction=0.20, min_l_s_per_person=10.0,
    locator="HTM 03-01 Part A, 2021, §8.6 p41; see also §9.120",
)
SHTM_FRESH_AIR = FreshAirRule(
    min_fraction=0.20,
    locator="SHTM 03-01 Part A v2, 2014, §2.37 p26 (Building (Scotland) Regs)",
)

GUIDELINES = [
    # Reinstated 2026-08-30 as ANSI/ASHRAE/ASHE 170-2021, on the researcher's
    # attestation that the previously recorded figures are the 2021 Table 7-1
    # row. They were formerly mislabelled 170-2025. 170-2025 remains NOT in
    # evidence, and §6.4 filter-bank topology is not held for either edition:
    # MERV-14 is stated, but which airstream it applies to is not established.
    Guideline("G1", "ANSI/ASHRAE/ASHE 170-2021",
              "Table 7-1, Critical care patient care station",
              ach_total=6.0, ach_outdoor=2.0,
              filter_descriptor="MERV-14 minimum (airstream per §6.4, NOT HELD)",
              pressure="N/R", temp_c=(21, 24), rh_pct=(30, 60)),
    Guideline("G2", "HTM 03-01 Part A, 2021",
              "Table 3, Level 2/3 critical care individual room/open bays, p64",
              ach_total=10.0, fresh_air_rule=HTM_FRESH_AIR,
              filter_descriptor="EPA10 final filter", pressure="+5 Pa",
              temp_c=(20, 25), rh_pct=(None, 60)),
    Guideline("G3", "HTM 03-01 Part A, 2021",
              "Appendix 2, Critical care areas (Level 2 and 3), p147",
              ach_total=10.0, fresh_air_rule=HTM_FRESH_AIR,
              filter_descriptor="SUP1 supply-filter designation",
              pressure="+10 Pa"),
    Guideline("G4", "SHTM 03-01 Part A v2, Feb 2014 (ARCHIVED)",
              "Appendix 1, Table A1, Critical Care Areas, p139",
              ach_total=10.0, fresh_air_rule=SHTM_FRESH_AIR,
              filter_descriptor="F7 supply filter", pressure="+10 Pa",
              temp_c=(18, 25)),
    Guideline("G5", "ISCCM Consensus Statement, 2020 (Rungta et al., IJCCM 24(S1):S43-S60)",
              "Environmental Requirements, HVAC system of ICU",
              ach_total=6.0, ach_outdoor=2.0,
              filter_descriptor="99% efficiency down to 5 um",
              pressure="clean to less-clean airflow; no numerical differential",
              temp_c=(16, 25)),
    Guideline("G6", "VHHSBA HTG-2020-004, May 2020",
              "§4.172 ICU and CCU, p34 (Reference Table 1/2 still required)",
              f_oa_fixed=0.50, filter_descriptor="remote HEPA outside the ICU",
              pressure="positive, beds toward circulation"),
    Guideline("G7", "AusHFG RDS 1BR-ICU, Rev 2, 12.11.2025",
              "page 1 HVAC checklist",
              filter_descriptor="not selected in this room data sheet",
              pressure="not selected in this room data sheet"),
    Guideline("G8", "NABH Accreditation Standards, 6th ed., Jan 2025",
              "COP.9 excerpt only",
              blocked="Full edition not audited. Absence of HVAC values from "
                      "one excerpt does not prove absence throughout."),
    Guideline("G9", "MoHFW Government of India, Guidelines for HDU & ICU, March 2022",
              "Physical Infrastructure, ICU and HDU beds, item 6, p24; "
              "Annexure III item 3.2, p47",
              ach_total=10.0, ach_total_max=12.0,
              ach_outdoor=4.0, ach_outdoor_max=5.0,
              filter_descriptor="AHU with fine filters (not a curve)",
              pressure="positive", temp_c=(21, 25), rh_pct=(45, 65)),
]

BY_KEY = {g.key: g for g in GUIDELINES}
