"""24-hour activity-driven scenario through each guideline's control parameters.

DECLARED SENSITIVITY SCENARIO. The intensity shape and the filter penetration
are researcher-declared; only the calibration target and the guideline control
parameters are sourced. This is NOT an ICU prediction.
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from icu import inputs as I, room
from icu.intensity import Block, IntensityProfile, Level, calibrate_mean_source
from icu.scenarios import BY_KEY

V = I.ROOM_VOLUME_M3
DT = 900.0                    # 15 min, master scheduler
STEPS = 96                    # one day
TARGET_MEAN = 202.0           # CFU/m3, Kim 2010 ICU bacteria total - SOURCED

# DECLARED intensity shape. Drivers name the activities; weights are ratios.
PROFILE = IntensityProfile(
    blocks=(
        Block(6.0, 2.0, Level.HIGH,   "bed bath, linen change, morning cleaning"),
        Block(8.0, 1.5, Level.MEDIUM, "ward round"),
        Block(13.0, 0.5, Level.LOW,   "afternoon obs"),
        Block(16.0, 2.0, Level.MEDIUM, "visiting hours"),
        Block(20.0, 1.0, Level.LOW,   "evening obs and linen"),
    ),
    weights={Level.QUIET: 1.0, Level.LOW: 2.0, Level.MEDIUM: 4.0, Level.HIGH: 8.0},
)


def occupancy_f_oa(g, n=5):
    """Outdoor-air fraction this guideline requires at occupancy n."""
    q = g.ach_total * V
    if g.fresh_air_rule:
        return g.fresh_air_rule.controlling_m3_h(q, n) / q
    if g.ach_outdoor:
        return g.ach_outdoor / g.ach_total
    return None


def removal(g, penetration):
    f = occupancy_f_oa(g)
    st = room.streams_from_ach(g.ach_total, f, V)
    _, b = room.coefficients(0.0, st.supply, f, V, penetration=penetration)
    return f, b


def run(g, penetration, s_bar):
    """One guideline, driven by a source that does NOT depend on the guideline.

    The source is a property of the room and its occupants. Calibrating it per
    scenario would give every guideline its own emission and normalise away the
    difference being tested.
    """
    f, b = removal(g, penetration)
    phi = PROFILE.series([i * DT / 3600.0 for i in range(STEPS)])

    c = TARGET_MEAN
    for _ in range(5):                     # settle to a periodic steady state
        trace = []
        for k in range(STEPS):
            a = s_bar * phi[k] / V
            c = room.step(c, a, b, DT)
            trace.append(c)
    return f, b, trace


def main():
    print("=" * 76)
    print("24-HOUR ACTIVITY SCENARIO — DECLARED SENSITIVITY, NOT A PREDICTION")
    print("=" * 76)
    print(PROFILE.label)
    print(f"Magnitude calibrated so the daily mean reproduces {TARGET_MEAN:.0f} CFU/m3")
    print("(Kim 2010 ICU bacteria total — SOURCED). Filter penetration is DECLARED.")
    print("k_dep = 0 because deposition is BLOCKED; this understates removal.\n")

    for pen, lbl in ((1.0, "no filter credit"), (0.15, "declared P = 0.15")):
        # Calibrate ONCE, at a declared reference condition, then hold the
        # source fixed across every guideline.
        ref = BY_KEY["G1"]
        _, b_ref = removal(ref, pen)
        s_bar = calibrate_mean_source(TARGET_MEAN, b_ref, V)
        print(f"--- {lbl} " + "-" * (66 - len(lbl)))
        print(f"  source calibrated once at the G1 reference condition, then "
              f"held fixed")
        print(f"  {'':4} {'ACH':>5} {'f_OA':>6} {'B 1/h':>7} {'mean':>7} "
              f"{'peak':>7} {'at':>6} {'trough':>7} {'peak/mean':>10}")
        for key in ("G1", "G2", "G5", "G9"):
            g = BY_KEY[key]
            if not g.simulatable:
                continue
            f, b, tr = run(g, pen, s_bar)
            mean = sum(tr) / len(tr)
            peak, trough = max(tr), min(tr)
            at = tr.index(peak) * DT / 3600.0
            print(f"  {key:4} {g.ach_total:>5.0f} {f:>6.3f} {b*3600:>7.2f} "
                  f"{mean:>7.0f} {peak:>7.0f} {at:>5.2f}h {trough:>7.0f} "
                  f"{peak/mean:>10.2f}")
        print()

    print("The source is identical across scenarios, so the differences are")
    print("entirely the doing of the guideline control parameters. A higher")
    print("removal coefficient B lowers both mean and peak, and also tracks the")
    print("source more closely, so the day becomes peakier in relative terms")
    print("even as absolute concentration falls.")


if __name__ == "__main__":
    main()
