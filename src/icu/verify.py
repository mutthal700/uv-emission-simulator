"""Independent verification of the concentration solver.

These checks do not re-use the stepper's own formula. Each derives the expected
result a second way, so a mistake in `room.step` cannot hide.

For dC/dt = A - B*C with C(0) = C0:

    C(t)          = C_ss + (C0 - C_ss) * exp(-B t),      C_ss = A/B
    integral_0^dt = C_ss*dt + (C0 - C_ss) * (1 - exp(-B dt)) / B

and integrating the ODE directly gives the accumulation identity

    C(dt) - C0 = A*dt - B * integral_0^dt C dt

which is an independent statement of mass conservation over the interval.
"""

import math


def concentration_integral(c0: float, a: float, b: float, dt_s: float) -> float:
    """Exact time-integral of C over one interval, in concentration-seconds."""
    if b <= 0:
        return c0 * dt_s + 0.5 * a * dt_s ** 2
    c_ss = a / b
    return c_ss * dt_s + (c0 - c_ss) * (1.0 - math.exp(-b * dt_s)) / b


def accumulation_residual(c0: float, c1: float, a: float, b: float,
                          dt_s: float) -> float:
    """Residual of the conservation identity. Should be ~0 for a correct step."""
    return (c1 - c0) - (a * dt_s - b * concentration_integral(c0, a, b, dt_s))


def flux_balance_residual(c0: float, c1: float, source_m3_s: float,
                          q_supply_m3_s: float, f_oa: float, volume_m3: float,
                          dt_s: float, penetration: float = 1.0,
                          uv_survival: float = 1.0, k_dep_per_s: float = 0.0,
                          c_outdoor: float = 0.0, a: float = None,
                          b: float = None) -> float:
    """Mass balance stated in FLUXES rather than in A and B.

    Accumulation must equal generation, plus what the supply brings in, minus
    what the return carries out, minus deposition - each integrated over the
    interval. This is built from the physical streams, not from the collected
    coefficients, so it catches an error in that collection step.
    """
    integral = concentration_integral(c0, a, b, dt_s)
    pz = penetration * uv_survival

    accumulation = volume_m3 * (c1 - c0)
    generated = source_m3_s * dt_s
    supplied = q_supply_m3_s * pz * (f_oa * c_outdoor * dt_s
                                     + (1.0 - f_oa) * integral)
    removed = q_supply_m3_s * integral
    deposited = k_dep_per_s * volume_m3 * integral

    return accumulation - (generated + supplied - removed - deposited)
