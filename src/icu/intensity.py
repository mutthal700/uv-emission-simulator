"""Activity intensity profile: shape separated from magnitude.

The point of this module is to reduce how much unsourced content the source term
carries.

Specifying an absolute emission rate for every activity needs N unsourced
numbers, none of which any ICU study reports. Specifying a low/medium/high
INTENSITY profile instead needs:

  * a dimensionless shape phi(t), normalised so its time-mean is exactly 1; and
  * ONE magnitude scalar S_bar per species, being the daily-mean source.

    S_i(t) = S_bar_i * phi(t)

That is a much weaker assumption: the shape says only "cleaning emits more than
a quiet night", while the single scalar carries all the units. And S_bar is
CALIBRATED against a measured mean concentration rather than declared, which is
exactly the distribution-validation rule (master D7) rather than an invented
emission factor.

Because the room balance is linear in S, the time-mean concentration depends on
the time-mean source alone, so the calibration is exact for the mean and does
not depend on the shape.
"""

import math
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Optional, Sequence, Tuple

from .inputs import BlockedInput


class Level(Enum):
    QUIET = "quiet"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass(frozen=True)
class Block:
    """A period of the day at one intensity level."""

    start_h: float
    duration_h: float
    level: Level
    driver: str = ""   # which activities put it at this level

    def covers(self, hour: float) -> bool:
        end = self.start_h + self.duration_h
        h = hour % 24.0
        if end <= 24.0:
            return self.start_h <= h < end
        return h >= self.start_h or h < (end - 24.0)


@dataclass
class IntensityProfile:
    """A 24-hour intensity shape, normalised to unit mean.

    `weights` are DECLARED dimensionless ratios between levels. They are not
    sourced ICU data, and every result carries that label.
    """

    blocks: Tuple[Block, ...]
    weights: Dict[Level, float]
    baseline: Level = Level.QUIET

    def __post_init__(self):
        if not self.blocks:
            raise BlockedInput(
                "no intensity blocks supplied. Closes with: an ICU SOP or IPC "
                "schedule giving when each activity occurs"
            )
        for b in self.blocks:
            if not b.driver:
                raise BlockedInput(
                    f"block at {b.start_h:g}h has no driver; name the "
                    "activities that place it at this level"
                )
        for lvl in set(b.level for b in self.blocks) | {self.baseline}:
            if lvl not in self.weights:
                raise BlockedInput(f"no declared weight for level {lvl.value!r}")
        if any(w < 0 for w in self.weights.values()):
            raise ValueError("weights cannot be negative")

    def raw(self, hour: float) -> float:
        for b in self.blocks:
            if b.covers(hour):
                return self.weights[b.level]
        return self.weights[self.baseline]

    def _mean_raw(self, steps_per_hour: int = 4) -> float:
        n = 24 * steps_per_hour
        return sum(self.raw(i / steps_per_hour) for i in range(n)) / n

    def phi(self, hour: float, steps_per_hour: int = 4) -> float:
        """Normalised shape. Time-mean is exactly 1 by construction."""
        m = self._mean_raw(steps_per_hour)
        if m <= 0:
            raise ValueError("profile has zero mean; cannot normalise")
        return self.raw(hour) / m

    def series(self, hours: Sequence[float], steps_per_hour: int = 4) -> list:
        m = self._mean_raw(steps_per_hour)
        return [self.raw(h) / m for h in hours]

    @property
    def label(self) -> str:
        return ("DECLARED intensity shape - dimensionless and normalised. "
                "Not sourced ICU activity data.")


def calibrate_mean_source(target_mean_excess: float, b_per_s: float,
                          volume_m3: float) -> float:
    """Daily-mean source `S_bar` that reproduces a measured mean concentration.

    At steady state C = A/B with A = S/V, so S_bar = target * B * V. The room
    balance is linear in S, so the time-mean concentration depends only on the
    time-mean source: this is exact for the mean and independent of the shape.

    `target_mean_excess` is the measured mean concentration ABOVE the supply
    contribution, in the species' own units.
    """
    if b_per_s <= 0:
        raise ValueError("removal coefficient must be positive to calibrate")
    return target_mean_excess * b_per_s * volume_m3
