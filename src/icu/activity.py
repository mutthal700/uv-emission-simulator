"""Activity-based indoor emission model.

No ICU study in evidence reports activity-resolved emission factors, so this
module deliberately supports TWO modes and refuses to blur them:

  PREDICTION   every emission factor and every event time carries an ICU source
               locator. Produces a result about an ICU. Currently unreachable.

  SENSITIVITY  factors are researcher DECLARED. Produces a labelled sensitivity
               scenario. It is NOT representative ICU data and must never be
               reported as an ICU prediction.

The structure is built so that sourced factors drop straight in. Nothing here
invents a number: an activity with no emission factor contributes zero and says
so, rather than receiving a default.
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import Optional, Sequence, Tuple

from .inputs import BlockedInput


class Basis(Enum):
    SOURCED = "sourced"
    DECLARED = "declared"


class Mode(Enum):
    PREDICTION = "prediction"
    SENSITIVITY = "sensitivity"


@dataclass(frozen=True)
class EmissionFactor:
    """Emission of one species during one activity.

    `per_bin` is a rate per size bin in the species' own units per second, in
    the same bin order as the species' state. A scalar species uses a
    single-element tuple.
    """

    species: str
    per_bin: Tuple[float, ...]
    basis: Basis
    source: str = ""

    def __post_init__(self):
        if any(v < 0 for v in self.per_bin):
            raise ValueError("emission rates cannot be negative")
        if self.basis is Basis.SOURCED and not self.source:
            raise ValueError(
                f"{self.species}: a SOURCED factor needs a locator - "
                "document, edition, table/section and the measured quantity"
            )


@dataclass(frozen=True)
class Activity:
    """A scheduled ICU activity that emits.

    `timing_source` must name the operational document. Physical plausibility is
    not evidence: an activity nobody documented does not happen on a schedule.
    """

    name: str
    start_h: float
    duration_h: float
    occupant_classes: Tuple[str, ...]
    timing_source: str
    emissions: Tuple[EmissionFactor, ...] = field(default_factory=tuple)

    def active_at(self, hour: float) -> bool:
        end = self.start_h + self.duration_h
        h = hour % 24.0
        if end <= 24.0:
            return self.start_h <= h < end
        return h >= self.start_h or h < (end - 24.0)

    def rate(self, species: str, n_bins: int) -> Tuple[float, ...]:
        for e in self.emissions:
            if e.species == species:
                if len(e.per_bin) != n_bins:
                    raise ValueError(
                        f"{self.name}/{species}: factor has {len(e.per_bin)} "
                        f"bins, state has {n_bins}. Re-binning a measured "
                        "distribution is not a units conversion and needs the "
                        "original channel boundaries"
                    )
                return e.per_bin
        return tuple(0.0 for _ in range(n_bins))


# Activity TYPES that plausibly emit PM in an ICU. This is a checklist of what
# to look for in the literature and the SOP - it is NOT a claim that each
# occurs, nor any statement about magnitude.
CANDIDATE_ACTIVITIES = (
    "bed making / linen change",
    "patient washing / bed bath",
    "floor and surface cleaning",
    "occupant walking and movement",
    "ward round",
    "visitor entry and door opening",
    "dressing change and bedside procedure",
)


@dataclass
class Schedule:
    activities: Tuple[Activity, ...]
    mode: Mode

    def validate(self) -> None:
        if not self.activities:
            raise BlockedInput(
                "no activity schedule supplied. Closes with: hospital ICU SOP "
                "or IPC manual event timing, plus an emission factor per "
                "species and activity"
            )
        for a in self.activities:
            if not a.timing_source:
                raise BlockedInput(f"activity {a.name!r} has no timing source")
            if self.mode is Mode.PREDICTION:
                if not a.emissions:
                    raise BlockedInput(
                        f"activity {a.name!r} has no emission factor; "
                        "prediction mode admits no zero-by-default"
                    )
                for e in a.emissions:
                    if e.basis is not Basis.SOURCED:
                        raise BlockedInput(
                            f"activity {a.name!r}, species {e.species}: factor "
                            "is DECLARED. Prediction mode requires an ICU "
                            "source locator; use SENSITIVITY mode instead"
                        )

    def source_series(self, species: str, n_bins: int,
                      hours: Sequence[float]) -> list:
        """Emission of `species` per bin at each hour. Sums concurrent activities."""
        self.validate()
        out = []
        for h in hours:
            total = [0.0] * n_bins
            for a in self.activities:
                if a.active_at(h):
                    for i, v in enumerate(a.rate(species, n_bins)):
                        total[i] += v
            out.append(tuple(total))
        return out

    @property
    def label(self) -> str:
        if self.mode is Mode.SENSITIVITY:
            return ("DECLARED SENSITIVITY SCENARIO - not representative ICU "
                    "data, not an ICU prediction")
        return "ICU prediction from sourced factors"
