"""Occupancy profile: by schedule, or recovered from a measured CO2 trace.

Two independent routes to N(t):

1. `profile_from_events` - a schedule of named events. Needs the hospital ICU
   SOP or IPC manual, which is blocked, so it fails closed on an empty schedule.

2. `co2_inversion` - runs the room CO2 balance backwards on a measured trace.
   Needs no schedule at all: occupancy is already encoded in the CO2 signal.

The inversion uses the exact solution of the balance rather than a finite
difference, so it is consistent with the forward recurrence and round-trips to
machine precision.
"""

import math
from dataclasses import dataclass
from typing import Sequence

from .inputs import BlockedInput


@dataclass(frozen=True)
class Event:
    """A scheduled ICU activity that changes occupancy.

    `delta_n` is the number of people added for the duration. Timing must come
    from an approved operational document, never from a generic assumption.
    """

    name: str
    start_h: float
    duration_h: float
    delta_n: int
    source: str  # document, section, revision - required

    def active_at(self, hour_of_day: float) -> bool:
        end = self.start_h + self.duration_h
        if end <= 24.0:
            return self.start_h <= hour_of_day < end
        return hour_of_day >= self.start_h or hour_of_day < (end - 24.0)


def profile_from_events(baseline_n: int, events: Sequence[Event],
                        hours: Sequence[float]) -> list:
    """Occupancy at each hour from a baseline plus scheduled events."""
    if not events:
        raise BlockedInput(
            "no ICU event schedule supplied. Closes with: hospital ICU SOP or "
            "IPC manual giving visiting hours, shift changeover, ward rounds, "
            "cleaning and bed-bath timing, each with unit, document number, "
            "revision, effective date, section and approval status."
        )
    for e in events:
        if not e.source:
            raise BlockedInput(f"event {e.name!r} has no source document")
    return [baseline_n + sum(e.delta_n for e in events if e.active_at(h % 24.0))
            for h in hours]


def co2_inversion(trace_ppm: Sequence[float], q_oa_m3_s: float, volume_m3: float,
                  dt_s: float, outdoor_ppm: float) -> list:
    """Recover the CO2 source term, m3/s, from a measured concentration trace.

    Inverts C(t+dt) = C_ss + (C(t) - C_ss) exp(-B dt) for S, assuming S is
    piecewise constant over each interval. Returns one value per interval, so
    len(result) == len(trace) - 1.
    """
    if q_oa_m3_s <= 0:
        raise ValueError("outdoor airflow must be positive to invert")
    if len(trace_ppm) < 2:
        raise ValueError("need at least two samples")
    a = math.exp(-q_oa_m3_s / volume_m3 * dt_s)
    out = []
    for c0, c1 in zip(trace_ppm, trace_ppm[1:]):
        excess_ss = (c1 - a * c0 - outdoor_ppm * (1 - a)) / (1 - a)
        out.append(q_oa_m3_s * excess_ss / 1e6)
    return out


def occupancy_from_source(source_m3_s: Sequence[float], patient_rate_m3_s: float,
                          per_person_m3_s: float, n_patients: int = 1) -> list:
    """Split an inverted CO2 source into patient and non-patient occupancy.

    The single-bed room fixes the patient count, so the patient contribution is
    known and can be subtracted. Staff and visitors are not separable from CO2
    alone; they are returned as one non-patient count.
    """
    if per_person_m3_s <= 0:
        raise ValueError("per-person rate must be positive")
    patient = n_patients * patient_rate_m3_s
    return [max((s - patient) / per_person_m3_s, 0.0) for s in source_m3_s]
