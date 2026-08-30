"""Well-mixed room mass balance for the single-bed ICU.

For CO2 the balance reduces to outdoor air alone. Starting from the general form
with supply and return:

    V dC/dt = S + Q_s*C_supply - Q_s*C_room
    C_supply = f_OA*C_out + (1 - f_OA)*C_return,   C_return = C_room   (A6)

substituting gives

    V dC/dt = S + Q_OA*(C_out - C_room)

so recirculation cancels exactly: only the outdoor-air flow exchanges CO2.
Filtration and UV do not act on CO2, so this holds for every scenario.
"""

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class Streams:
    """Airflows for one operating point, all m3/s."""

    supply: float
    outdoor: float

    @property
    def recirculated(self) -> float:
        return self.supply - self.outdoor

    @property
    def exhaust(self) -> float:
        # A5: exhaust is balanced against outdoor air.
        return self.outdoor

    @property
    def f_oa(self) -> float:
        return self.outdoor / self.supply


def streams_from_ach(ach_total: float, f_oa: float, volume_m3: float) -> Streams:
    supply = ach_total * volume_m3 / 3600.0
    return Streams(supply=supply, outdoor=f_oa * supply)


def co2_prediction_patient_inclusive(*args, **kwargs):
    """Patient-inclusive CO2 prediction. GATED — see capabilities."""
    from .capabilities import require
    require("co2_patient_inclusive")
    raise AssertionError("unreachable while the capability is disabled")


def co2_excess_steady_state(source_m3_s: float, q_oa_m3_s: float) -> float:
    """Steady-state CO2 excess above outdoor, in ppm.

    Reported as an excess so that no unsourced outdoor baseline is required.
    """
    if q_oa_m3_s <= 0:
        return math.inf
    return 1e6 * source_m3_s / q_oa_m3_s


def co2_excess_step(excess_ppm: float, source_m3_s: float, q_oa_m3_s: float,
                    volume_m3: float, dt_s: float) -> float:
    """Advance the CO2 excess by dt using the exact exponential recurrence.

    Preserves master decision D10: no Euler stepping.
    """
    ss = co2_excess_steady_state(source_m3_s, q_oa_m3_s)
    b = q_oa_m3_s / volume_m3
    return ss + (excess_ppm - ss) * math.exp(-b * dt_s)


def time_to_fraction(fraction: float, q_oa_m3_s: float, volume_m3: float) -> float:
    """Seconds to close `fraction` of the gap to steady state."""
    if not 0 < fraction < 1:
        raise ValueError("fraction must be in (0, 1)")
    return -math.log(1 - fraction) * volume_m3 / q_oa_m3_s


def duct_velocity(q_supply_m3_s: float, duct_area_m2: float) -> float:
    return q_supply_m3_s / duct_area_m2


def duct_transit_time(q_supply_m3_s: float, duct_area_m2: float, length_m: float) -> float:
    return length_m / duct_velocity(q_supply_m3_s, duct_area_m2)
