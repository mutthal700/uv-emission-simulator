"""Guideline scenarios for Stage A.

One entry per verified document row. Not reconciled, not averaged. `ach_total`
of None means the source states no air-change rate, so the scenario cannot be
simulated until that value is sourced.
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Guideline:
    key: str
    document: str
    locator: str
    ach_total: Optional[float]
    ach_outdoor: Optional[float]   # absolute outdoor floor, if the source gives one
    f_oa_fixed: Optional[float]    # equality constraint, if the source gives one
    filter_class: Optional[str]
    pressure: Optional[str]
    temp_c: Optional[tuple]
    rh_pct: Optional[tuple]

    @property
    def simulatable(self) -> bool:
        return self.ach_total is not None

    def min_f_oa(self) -> Optional[float]:
        if self.f_oa_fixed is not None:
            return self.f_oa_fixed
        if self.ach_outdoor is None or self.ach_total is None:
            return None
        return self.ach_outdoor / self.ach_total


GUIDELINES = [
    Guideline("G1", "ANSI/ASHRAE/ASHE 170-2025",
              "Table 7-1, Critical care patient care station",
              6.0, 2.0, None, "MERV-14", "N/R", (21, 24), (30, 60)),
    Guideline("G2", "HTM 03-01 Part A, 2021",
              "Table 3, Level 2/3 critical care individual room, p64",
              10.0, None, None, "BS EN 1822 EPA10", "+5 Pa", (20, 25), (None, 60)),
    Guideline("G3", "HTM 03-01 Part A, 2021",
              "Appendix 2, Critical care areas, p147",
              10.0, None, None, "BS EN 16798 SUP1", "+10 Pa", None, None),
    Guideline("G4", "SHTM 03-01 Part A v2, Feb 2014 (ARCHIVED)",
              "Appendix 1, Table A1, Critical Care Areas, p139",
              10.0, None, None, "F7", "+10 Pa", (18, 25), None),
    Guideline("G5", "ISCCM Consensus Statement, 2020",
              "Environmental Requirements, HVAC system of ICU",
              6.0, 2.0, None, "99% down to 5 um", None, (16, 25), None),
    Guideline("G6", "VHHSBA HTG-2020-004, May 2020",
              "4.172 ICU and CCU, p34",
              None, None, 0.50, "remote HEPA", "positive", None, None),
    Guideline("G7", "AusHFG RDS 1BR-ICU, Rev 2, 12.11.2025",
              "page 1 HVAC checklist",
              None, None, None, None, None, None, None),
    Guideline("G8", "NABH Accreditation Standards, 6th ed., Jan 2025",
              "COP.9",
              None, None, None, None, None, None, None),
]

BY_KEY = {g.key: g for g in GUIDELINES}
