"""Stage A, Tier 1: what each guideline delivers for CO2, and at what relative energy.

Reports CO2 as an excess above outdoor, so no unsourced outdoor baseline is
needed. Energy is reported as ratios, so no equipment data is needed.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from icu import inputs as I
from icu import room, energy
from icu.scenarios import GUIDELINES

V = I.ROOM_VOLUME_M3
MET_STAFF = 1.2  # DECLARED scenario parameter: ISO 8996 is blocked
# Persily Table 4 male 21-<30 is a declared demographic SCENARIO, not a generic
# staff/visitor class. Sources are converted to the declared room state.


def co2_source(n_total: int, met: float = MET_STAFF) -> float:
    """One patient at the measured ICU rate, the remainder at Persily."""
    others = max(n_total - I.BED_COUNT, 0)
    patient = I.source_at_room_state(I.VCO2_PATIENT_KAGAN)
    other = I.source_at_room_state(I.VCO2_MALE_21_30_BY_MET[met])
    return patient + others * other


def main() -> None:
    print("=" * 78)
    print("STAGE A / TIER 1 - single-bed ICU, V = %.1f m3" % V)
    print("CO2 excess above outdoor (ppm). Patient at Kagan measured rate;")
    print("others as Persily Table 4 MALE 21-<30 at %.1f met - a declared" % MET_STAFF)
    print("demographic scenario, not a generic staff class. Sources converted")
    print("from their gas reference states to %.2f K / %.0f Pa." % (I.ROOM_EVAL_T_K, I.ROOM_EVAL_P_PA))
    print("=" * 78)

    occ = [("base min", I.OCCUPANCY_BASE_MIN),
           ("base max", I.OCCUPANCY_BASE_MAX),
           ("surge", I.OCCUPANCY_SURGE_MAX)]

    print("\n%-4s %-9s %6s %8s %8s %s" % ("", "ACH", "f_OA", "Q_s", "Q_OA", "CO2 excess ppm"))
    print("%-4s %-9s %6s %8s %8s %s" % ("", "", "", "m3/h", "m3/h",
                                        "  ".join(f"{n:>9}" for n, _ in occ)))
    print("-" * 78)

    rows = []
    for g in GUIDELINES:
        if not g.simulatable:
            print(f"{g.key:<4} {'-- no air-change rate stated --':<40} {g.document}")
            continue
        f = g.min_f_oa()
        label = f"{f:.3f}" if f is not None else "undef"
        # Where the source states no outdoor-air value, evaluate at the sweep
        # bounds instead of importing another guideline's floor.
        f_eval = f if f is not None else 1.0
        s = room.streams_from_ach(g.ach_total, f_eval, V)
        vals = [room.co2_excess_steady_state(co2_source(n), s.outdoor) for _, n in occ]
        rows.append((g, s))
        print("%-4s %-9.1f %6s %8.1f %8.1f %s" % (
            g.key, g.ach_total, label, s.supply * 3600, s.outdoor * 3600,
            "  ".join(f"{v:9.0f}" for v in vals)))

    print("\nG2/G3/G4 state no outdoor-air value, so f_OA is undefined by those")
    print("rows; they are evaluated at f_OA = 1.0 (the sweep's upper bound).")
    print("Their CO2 result is therefore a best case, not a requirement.")

    # --- energy ratios -------------------------------------------------------
    base = next(s for g, s in rows if g.key == "G1")
    print("\n" + "=" * 78)
    print("RELATIVE ENERGY, referenced to G1 (ASHRAE 170-2025 at its floors)")
    print("=" * 78)
    print("%-4s %10s %14s %18s" % ("", "Q_s ratio", "fan power x", "OA conditioning x"))
    print("-" * 78)
    for g, s in rows:
        print("%-4s %10.3f %14.2f %18.2f" % (
            g.key,
            s.supply / base.supply,
            energy.fan_power_ratio(s.supply, base.supply),
            energy.oa_conditioning_ratio(s.outdoor, base.outdoor)))
    print("\nFan ratio uses the cube law for a fixed system curve; a loading filter")
    print("departs from it. OA conditioning ratio is at equal enthalpy difference;")
    print("absolute duty needs the five-zone climate data.")

    # --- what "undefined f_OA" actually spans --------------------------------
    print("\n" + "=" * 78)
    print("UK ROWS: f_OA IS UNDEFINED, SO THE RESULT IS A RANGE")
    print("G2/G3/G4 at 10 ACH, CO2 excess (ppm) across the sweep")
    print("=" * 78)
    print("%-8s %10s %12s %12s %12s" % ("f_OA", "Q_OA m3/h", "base min", "base max", "surge"))
    print("-" * 78)
    for f in (0.05, 0.10, 0.20, 0.333, 0.50, 1.00):
        s = room.streams_from_ach(10.0, f, V)
        vals = [room.co2_excess_steady_state(co2_source(n), s.outdoor) for _, n in occ]
        print("%-8.3f %10.1f %12.0f %12.0f %12.0f" % (f, s.outdoor * 3600, *vals))
    print("\nNothing in the verified UK rows forbids the top of this table.")
    print("A literal-compliance optimiser minimising energy would sit there.")

    # --- flush-out times -----------------------------------------------------
    print("\n" + "=" * 78)
    print("TIME CONSTANTS (time to close 95% of the gap to steady state)")
    print("=" * 78)
    for g, s in rows:
        t = room.time_to_fraction(0.95, s.outdoor, V)
        v = room.duct_velocity(s.supply, I.DUCT_AREA_M2)
        print("%-4s  t95 = %6.1f min   duct velocity = %.3f m/s   transit = %.2f s"
              % (g.key, t / 60, v, room.duct_transit_time(s.supply, I.DUCT_AREA_M2,
                                                          I.DUCT_LENGTH_M)))


if __name__ == "__main__":
    main()
