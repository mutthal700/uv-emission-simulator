"""Pollutant state vector and per-species removal pathways.

Design decision that follows from the evidence: PM2.5 and PM10 are **mass
metrics, not state variables**. Filter penetration is size-dependent, so a mass
metric cannot be penetrated directly. The state is carried in size bins and the
metrics are computed as integrals over them at reporting time.

Removal pathways per species, from the physical character in the register:

    species          filter   deposition   UVGI    dilution
    CO2                no         no        no       yes
    TVOC               no         no        no       yes
    PM bins           yes        yes        no       yes
    bacteria bins     yes        yes       yes       yes
    fungi bins        yes        yes       yes       yes
"""

from dataclasses import dataclass
from typing import Optional, Tuple

# Kim, Kim & Kim (2010) six-stage Andersen aerodynamic ranges, ascending.
# Stage 1 is open-ended above 7.0 um; no representative diameter is assigned
# here because none is reported by the source.
VIABLE_BINS_UM: Tuple[Tuple[float, Optional[float]], ...] = (
    (0.65, 1.1), (1.1, 2.1), (2.1, 3.3), (3.3, 4.7), (4.7, 7.0), (7.0, None),
)


@dataclass(frozen=True)
class Species:
    name: str
    binned: bool
    filtered: bool
    deposits: bool
    uv_susceptible: bool
    unit: str

    @property
    def dilution_only(self) -> bool:
        return not (self.filtered or self.deposits or self.uv_susceptible)


SPECIES = {
    "CO2":      Species("CO2", False, False, False, False, "ppm"),
    "TVOC":     Species("TVOC", False, False, False, False, "ug/m3"),
    "PM":       Species("PM", True, True, True, False, "ug/m3 per bin"),
    "bacteria": Species("bacteria", True, True, True, True, "CFU/m3 per bin"),
    "fungi":    Species("fungi", True, True, True, True, "CFU/m3 per bin"),
}


def reported_metric(bin_values, bin_edges_um, cutoff_um: float) -> float:
    """Integrate binned state into a mass metric such as PM2.5 or PM10.

    A bin is included only if it lies wholly at or below the cutoff. Partial
    bins are not apportioned: splitting a bin needs the within-bin distribution,
    which is part of the blocked size-distribution evidence.
    """
    total = 0.0
    for value, (lo, hi) in zip(bin_values, bin_edges_um):
        if hi is not None and hi <= cutoff_um:
            total += value
    return total
