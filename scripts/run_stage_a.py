"""Stage A — status after the evidence audit of 2026-08-30.

Admissibility classes follow the audit:
  ACCEPTED   directly stated in an identified primary document
  DERIVED    arithmetic only, on accepted data plus researcher-defined geometry
  BLOCKED    the primary evidence is unavailable; no substitute inserted
  WITHDRAWN  previously reported, now unsupported
"""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from icu import inputs as I
from icu import room, energy
from icu.scenarios import GUIDELINES, BY_KEY

V = I.ROOM_VOLUME_M3
OCC = [("min listed", I.OCCUPANCY_BASE_MIN),
       ("max listed", I.OCCUPANCY_BASE_MAX),
       ("with additional staff", I.OCCUPANCY_SURGE_MAX)]
W = 78


def hdr(t):
    print("\n" + "=" * W + f"\n{t}\n" + "=" * W)


def main() -> None:
    hdr("STAGE A STATUS — single-bed ICU, V = 75.0 m3 (DERIVED, 25.00 x 3.0)")

    print("\nScenario admissibility:")
    print("-" * W)
    for g in GUIDELINES:
        if g.blocked:
            print(f"  {g.key}  BLOCKED   {g.document}")
            print(f"          {g.blocked}")
        elif g.simulatable:
            rng = f"{g.ach_total:g}" + (f"-{g.ach_total_max:g}" if g.ach_total_max else "")
            print(f"  {g.key}  usable    {rng} ACH   {g.document}")
        else:
            print(f"  {g.key}  no rate   {g.document}")

    # --- HTM/SHTM minimum outdoor air ---------------------------------------
    hdr("CORRECTED UK OUTDOOR AIR — ACCEPTED provisions, DERIVED arithmetic")
    print("HTM 03-01:2021 §8.6: fresh air >= 10 L/s/person; where air is")
    print("recirculated, minimum fresh air is 20% or the person-based")
    print("requirement, whichever is greater.")
    print("SHTM 03-01:2014 §2.37 supplies only the 20% fraction at its edition")
    print("date. The English and Scottish documents are NOT combined.\n")
    for key in ("G2", "G4"):
        g = BY_KEY[key]
        q = g.ach_total * V
        print(f"  {key} ({g.document.split(',')[0]}), Q_supply = {q:.0f} m3/h")
        print(f"      {'occupants':<24} {'controlling OA':>15} {'ACH_OA':>8} {'f_OA':>7}")
        for label, n in OCC:
            oa = g.fresh_air_rule.controlling_m3_h(q, n)
            print(f"      {label + f' (N={n})':<24} {oa:>11.0f} m3/h {oa/V:>8.2f} {oa/q:>7.3f}")
        print()

    print("WITHDRAWN: the earlier finding that UK outdoor air is undefined and")
    print("could approach zero. It rested on the critical-care rows alone; the")
    print("general provisions bound it. The 5% and 10% sweep points are")
    print("NONCOMPLIANT with HTM 03-01:2021, not permissible design options.")

    # --- CO2 at the controlling minima --------------------------------------
    hdr("CO2 EXCESS ABOVE OUTDOOR at the controlling minimum outdoor air")
    print("DERIVED. Patient = Kagan cohort mean (Draeger STPD); non-patients =")
    print("Persily male 21-<30 at 1.2 met — a researcher-defined demographic")
    print("scenario, not a generic staff rate. Evaluated at a RESEARCHER-SELECTED")
    print(f"state of {I.RESEARCHER_EVAL_T_K} K / {I.RESEARCHER_EVAL_P_PA:.0f} Pa; the actual ICU room state is")
    print("BLOCKED, so these are not source-backed concentrations.\n")
    patient = I.source_at_eval_state(I.VCO2_PATIENT_KAGAN)
    other = I.source_at_eval_state(I.VCO2_MALE_21_30_BY_MET[1.2])

    print(f"  {'scenario':<8} {'N':>3} {'OA m3/h':>9} {'CO2 excess ppm':>16}")
    print("  " + "-" * (W - 4))
    for key in ("G2", "G4", "G5", "G9"):
        g = BY_KEY[key]
        q = g.ach_total * V
        for label, n in OCC:
            if g.fresh_air_rule:
                oa = g.fresh_air_rule.controlling_m3_h(q, n)
            elif g.ach_outdoor:
                oa = g.ach_outdoor * V
            else:
                continue
            s = patient + max(n - I.BED_COUNT, 0) * other
            exc = room.co2_excess_steady_state(s, oa / 3600.0)
            print(f"  {key:<8} {n:>3} {oa:>9.0f} {exc:>16.0f}")
        print()

    # --- conditional arithmetic ---------------------------------------------
    hdr("RELATIVE ENERGY — DERIVED, CONDITIONAL, NOT A FINDING")
    print("Withdrawn as evidence-backed results. The fan ratio holds only for an")
    print("identical system curve and unchanged efficiency, which no equipment")
    print("data supports; the earlier 5x outdoor-air figure additionally used the")
    print("invalid unbounded-UK treatment and is void.\n")
    q6 = room.streams_from_ach(6.0, 1 / 3, V).supply
    q10 = room.streams_from_ach(10.0, 1 / 3, V).supply
    print(f"  10 ACH vs 6 ACH supply ratio      : {q10/q6:.3f}")
    print(f"  fan power ratio IF cube law holds : {energy.fan_power_ratio(q10, q6):.2f}x")
    print("  absolute fan power                : BLOCKED (system dP, fan/motor/drive)")
    print("  absolute conditioning energy      : BLOCKED (climate files, coil config, loads)")

    hdr("ALSO WITHDRAWN")
    for line in (
        "'Four of eight guidelines are incomplete' — not every named edition has",
        "  been checked, and G1 and G8 are blocked rather than known.",
        "Response-time (t95) results — they depended on the invalid UK outdoor",
        "  air treatment for the 10 ACH rows.",
        "The clean/moderate/India-high/event-tail pollutant regime table —",
        "  analyst-created categories with several misattributions.",
    ):
        print("  " + line)


if __name__ == "__main__":
    main()
