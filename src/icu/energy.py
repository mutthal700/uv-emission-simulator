"""Energy terms available at Tier 1.

Absolute fan power needs a system pressure drop, which is blocked. Ratios
between scenarios do not: for a fixed system resistance characteristic the
pressure drop varies with the square of flow, so shaft power varies with the
cube. That is enough to rank guidelines on fan energy without any equipment
data.

The cube law assumes a fixed system curve. A filter's pressure drop is not
purely quadratic in flow and shifts as it loads, so this is a first-order
comparison, to be replaced once the filter model supplies dP(Q, loading).
"""


def fan_power_ratio(q_a_m3_s: float, q_b_m3_s: float) -> float:
    """Fan shaft power of A relative to B, fixed system curve."""
    return (q_a_m3_s / q_b_m3_s) ** 3


def fan_power_w(q_m3_s: float, pressure_drop_pa: float, efficiency: float) -> float:
    """Absolute fan power. Requires a sourced pressure drop."""
    if not 0 < efficiency <= 1:
        raise ValueError("efficiency must be in (0, 1]")
    return q_m3_s * pressure_drop_pa / efficiency


def oa_conditioning_ratio(q_oa_a_m3_s: float, q_oa_b_m3_s: float) -> float:
    """Outdoor-air conditioning duty of A relative to B at equal enthalpy difference.

    Duty is mass flow times enthalpy change, so at a common outdoor and room
    state the ratio is just the flow ratio. Absolute duty needs the climate data.
    """
    return q_oa_a_m3_s / q_oa_b_m3_s
