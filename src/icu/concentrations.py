"""ICU pollutant concentrations, as validation regimes.

Per master section 1.1 these are validation targets, NOT regulatory limits and
NOT source inputs. They are what a simulated distribution is checked against
(master D7), never what is fed in.

Two provenance tiers, kept apart deliberately:
  VERIFIED  - full locator, primary document checked
  REPORTED  - carried in the project master file with partial attribution;
              cannot be promoted until a full locator is supplied
"""

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Regime:
    pollutant: str
    unit: str
    clean: Optional[tuple]
    moderate: Optional[tuple]
    india_high: Optional[tuple]
    event_tail: Optional[str]
    provenance: str
    locator: str


# --- VERIFIED ----------------------------------------------------------------
KIM_2010 = "Kim, Kim & Kim, Industrial Health 48(2):236-243 (2010)"

VERIFIED = {
    "bacteria_icu_total": (202, "CFU/m3", f"{KIM_2010}, Table 2"),
    "bacteria_icu_respirable": (142, "CFU/m3", f"{KIM_2010}, Table 2, stages 3-6"),
    "fungi_icu_total": (65, "CFU/m3", f"{KIM_2010}, Table 3"),
    "fungi_icu_respirable": (47, "CFU/m3", f"{KIM_2010}, Table 3, stages 3-6"),
}

# --- REPORTED IN MASTER, NOT YET LOCATOR-COMPLETE ----------------------------
_M = "project master file section 1.1"
_NEED = "full document title, edition/year and table/section with named row"

REPORTED = [
    Regime("CO2", "ppm", (450, 800), (828, 1570), (1822, 2258),
           "occupancy/visitation peaks", _M + " (Tang; Aligarh)", _NEED),
    Regime("PM2.5", "ug/m3", (1, 5), (20, 35), (50, 98),
           "activity/cleaning peaks", _M, _NEED),
    Regime("PM10", "ug/m3", (0.9, 10), (10, 60), (57, 118),
           "instantaneous peaks can be much higher", _M, _NEED),
    Regime("bacteria", "CFU/m3", (70, 250), (250, 450), (94, 151),
           ">1000 to ~7236 (Tang)", _M, _NEED),
    Regime("fungi", "CFU/m3", (2.6, 70), None, None,
           ">1000 to ~11654 (Tang)", _M, _NEED),
    Regime("TVOC", None, None, None, None, None,
           "BLOCKED - no ICU concentration evidence held at all",
           "any primary ICU TVOC measurement with instrument and averaging time"),
]

# --- physical character, which decides which removal terms apply -------------
CHARACTER = {
    #  pollutant : (type, size basis, removal mechanisms available)
    "CO2":      ("gas", "not applicable", ("dilution",)),
    "TVOC":     ("gas mixture, lumped surrogate", "not applicable",
                 ("dilution", "adsorption if a carbon stage is fitted")),
    "PM2.5":    ("particulate MASS METRIC", "mass below 2.5 um, not a distribution",
                 ("filtration", "deposition")),
    "PM10":     ("particulate MASS METRIC", "mass below 10 um, not a distribution",
                 ("filtration", "deposition")),
    "bacteria": ("viable particulate", "six Andersen stages, 0.65 um to >7 um",
                 ("filtration", "deposition", "UVGI")),
    "fungi":    ("viable particulate", "six Andersen stages, 0.65 um to >7 um",
                 ("filtration", "deposition", "UVGI")),
}
