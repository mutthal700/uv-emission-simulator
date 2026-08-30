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


# --- general multi-species balance -------------------------------------------
#
# With the main filter on MIXED air (researcher-defined system topology), the
# supply concentration for species i is
#
#     C_supply,i = P_i * Z_i * [ f_OA * C_out,i + (1 - f_OA) * C_room,i ]
#
# where P_i is filter penetration and Z_i is in-duct UV survival. Substituting
# into the room balance and collecting terms gives dC/dt = A - B*C with
#
#     A_i = [ S_i + Q_s * P_i * Z_i * f_OA * C_out,i ] / V
#     B_i = (Q_s / V) * (1 - P_i * Z_i * (1 - f_OA)) + k_dep,i
#
# so the exact recurrence applies unchanged, per species.
#
# Note the structure: in-duct UV enters as a multiplier alongside filter
# penetration. Mathematically an in-duct lamp IS a filter acting on the viable
# bins only. It is not a room removal term.


def coefficients(source_m3_s: float, q_supply_m3_s: float, f_oa: float,
                 volume_m3: float, penetration: float = 1.0,
                 uv_survival: float = 1.0, k_dep_per_s: float = 0.0,
                 c_outdoor: float = 0.0):
    """Return (A, B) for dC/dt = A - B*C, for one species.

    `penetration` and `uv_survival` are single-pass fractions in [0, 1]:
    1.0 means the stage removes nothing. Concentration units are arbitrary but
    must be consistent between `source_m3_s`/volume and `c_outdoor`.
    """
    for label, x in (("penetration", penetration), ("uv_survival", uv_survival)):
        if not 0.0 <= x <= 1.0:
            raise ValueError(f"{label} must be in [0, 1]")
    if not 0.0 <= f_oa <= 1.0:
        raise ValueError("f_oa must be in [0, 1]")
    pz = penetration * uv_survival
    a = (source_m3_s + q_supply_m3_s * pz * f_oa * c_outdoor) / volume_m3
    b = (q_supply_m3_s / volume_m3) * (1.0 - pz * (1.0 - f_oa)) + k_dep_per_s
    return a, b


def steady_state(a: float, b: float) -> float:
    if b <= 0:
        return math.inf
    return a / b


def step(c: float, a: float, b: float, dt_s: float) -> float:
    """Exact exponential advance. No Euler stepping (master D10)."""
    if b <= 0:
        return c + a * dt_s
    ss = a / b
    return ss + (c - ss) * math.exp(-b * dt_s)
