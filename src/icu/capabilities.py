"""Capability gating.

Input-level fail-closed is not enough: a capability can be unsafe to run even
when each individual number exists, because the *combination* is unsupported.
This module disables whole classes of result until their prerequisites close.

No blocked quantity ever receives a default value. Nothing here can be bypassed
by passing a substitute; the only way to enable a capability is to close its
prerequisites in `inputs`.
"""

from . import inputs as I


class CapabilityDisabled(RuntimeError):
    """A whole class of result is unsupported by the current evidence."""


def _unmet(*blocked) -> list:
    out = []
    for b in blocked:
        try:
            float(b)
        except I.BlockedInput as e:
            out.append(str(e))
        except TypeError:
            out.append(f"{b} is unavailable")
    return out


CAPABILITIES = {
    "co2_patient_inclusive": (
        "Patient-inclusive CO2 prediction",
        lambda: _unmet(I.PATIENT_EXHAUST_PATH, I.ROOM_ACTUAL_T_P),
        "Patient VCO2 is a room source only if expired gas discharges to the "
        "room, and a volumetric balance needs the actual room gas state.",
    ),
    "headcount_inversion": (
        "Headcount from CO2 inversion",
        lambda: _unmet(I.STAFF_VISITOR_OBSERVED, I.PATIENT_EXHAUST_PATH),
        "The inversion recovers non-patient SOURCE STRENGTH. Converting it to "
        "people needs heterogeneous per-person rates; a single reference rate "
        "yields 'equivalent occupants', which is not a headcount.",
    ),
    "filtration_size_resolved": (
        "Tier 2 size-resolved filtration",
        lambda: _unmet(I.ICU_PM_SIZE_DISTRIBUTION),
        "Filter classes are not efficiency curves. Needs manufacturer eta(dp) "
        "at the duty point, and ASHRAE 170 section 6.4 for the airstream the "
        "filter acts on.",
    ),
    "deposition": (
        "Deposition modelling",
        lambda: _unmet(I.K_DEPOSITION, I.ICU_PM_SIZE_DISTRIBUTION),
        "Blocked under the no-proxy rule: generic non-ICU aerosol literature "
        "may not be inserted as an ICU-room input.",
    ),
    "stage_c_control": (
        "Stage C concentration-responsive control",
        lambda: _unmet(I.OCCUPANCY_SCHEDULE, I.STAFF_VISITOR_OBSERVED),
        "Control that responds to occupancy needs an evidenced occupancy "
        "history, not a declared scenario.",
    ),
    "absolute_energy": (
        "Absolute energy results",
        lambda: _unmet(I.SYSTEM_PRESSURE_DROP_PA, I.FAN_EFFICIENCY),
        "Needs system pressure drop per duty point and loading state, and fan, "
        "motor and drive efficiency. Motor IE class is not fan efficiency, and "
        "code minima are a compliance baseline, not plant performance.",
    ),
}


def status() -> dict:
    """Every capability with its unmet prerequisites."""
    return {k: (title, why, probe()) for k, (title, probe, why) in CAPABILITIES.items()}


def enabled(name: str) -> bool:
    title, probe, why = CAPABILITIES[name]
    return not probe()


def require(name: str) -> None:
    """Raise unless the capability's prerequisites are all closed."""
    title, probe, why = CAPABILITIES[name]
    unmet = probe()
    if unmet:
        detail = "\n  - ".join(unmet)
        raise CapabilityDisabled(
            f"{title} is DISABLED.\n{why}\nUnmet prerequisites:\n  - {detail}"
        )
