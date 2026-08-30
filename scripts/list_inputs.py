"""Print the complete input register: what is held, its units, and its source."""

import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from icu import inputs as I
from icu.scenarios import GUIDELINES

W = 96
def hdr(t): print("\n" + "=" * W + f"\n{t}\n" + "=" * W)
def row(*c): print("%-30s %-16s %-12s %s" % c)

hdr("1. ROOM GEOMETRY AND OCCUPANCY")
row("PARAMETER", "VALUE", "UNIT", "SOURCE")
print("-" * W)
src1 = "AusHFG RDS 1BR-ICU Rev2 12.11.2025 p1"
row("Floor area A", f"{I.FLOOR_AREA_M2:.2f}", "m2", src1)
row("Ceiling height H", f"{I.CEILING_HEIGHT_M:.1f}", "m", src1)
row("Room volume V", f"{I.ROOM_VOLUME_M3:.1f}", "m3", "derived A x H (gross geometric)")
row("Bed count", f"{I.BED_COUNT}", "-", "AusHFG RDS p5 MMBE-116 QTY 1")
row("Occupancy base min", f"{I.OCCUPANCY_BASE_MIN}", "persons", src1)
row("Occupancy base max", f"{I.OCCUPANCY_BASE_MAX}", "persons", src1)
row("Occupancy surge max", f"{I.OCCUPANCY_SURGE_MAX}", "persons", src1)

hdr("2. DUCT")
row("PARAMETER", "VALUE", "UNIT", "SOURCE")
print("-" * W)
row("Duct side", f"{I.DUCT_SIDE_M:.4f}", "m", "researcher, fixed")
row("Duct face area", f"{I.DUCT_AREA_M2:.6f}", "m2", "derived (= 1.000 sq ft)")
row("Duct length", f"{I.DUCT_LENGTH_M:.1f}", "m", "physical rig, master section 4")

hdr("3. CO2 GENERATION PER PERSON")
row("PARAMETER", "VALUE", "UNIT", "SOURCE")
print("-" * W)
row("Patient (Kagan mean)", f"{I.VCO2_PATIENT_KAGAN:.4e}", "m3/s", "Kagan Crit Care 22:186 (2018) 244.5 mL/min")
row("  +/- 1 SD", f"{I.VCO2_PATIENT_KAGAN_SD:.4e}", "m3/s", "same, 85.9 mL/min")
row("Patient (Rousing)", f"{I.VCO2_PATIENT_ROUSING:.4e}", "m3/s", "Ann Intensive Care 6:16 (2016) 273 mL/min")
row("Patient (Altunalan)", f"{I.VCO2_PATIENT_ALTUNALAN:.4e}", "m3/s", "BMC Anesthesiol 26:89 (2026) 188.362 mL/min")
for met, v in sorted(I.VCO2_STAFF_BY_MET.items()):
    row(f"Staff/visitor @ {met} met", f"{v:.4e}", "m3/s", "Persily Indoor Air 27:868 (2017) Table 4, M21-30")
print("\n  NOTE: met level is a DECLARED parameter with a sensitivity range,")
print("        not a sourced ICU value. ISO 8996:2021 is blocked.")
print("  NOTE: Persily is stated at 273 K / 101 kPa; clinical calorimetry")
print("        reports STPD or BTPS. Reference conditions need reconciling.")

hdr("4. VIABLE AEROSOL BINS AND ICU TOTALS")
vb = I.ViableBins
print("  Andersen stages (um):", ", ".join(
    f"{lo}-{hi}" if hi else f">{lo}" for lo, hi in vb.edges_um))
row("Bacteria, ICU total", f"{vb.icu_bacteria_total_cfu_m3}", "CFU/m3", "Kim Ind Health 48(2):236 (2010) Table 2")
row("Bacteria, respirable", f"{vb.icu_bacteria_respirable_cfu_m3}", "CFU/m3", "same, stages 3-6")
row("Fungi, ICU total", f"{vb.icu_fungi_total_cfu_m3}", "CFU/m3", "Kim (2010) Table 3")
row("Fungi, respirable", f"{vb.icu_fungi_respirable_cfu_m3}", "CFU/m3", "same, stages 3-6")
print("\n  NOTE: stage 1 open-ended above 7.0 um; any representative diameter")
print("        is a modelling choice. Stage distributions are graphical only.")

hdr("5. ENERGY REFERENCE VALUES (code minima, not measured)")
row("PARAMETER", "VALUE", "UNIT", "SOURCE")
print("-" * W)
row("Chiller COP <260 kWr", f"{I.CHILLER_COP_LT_260KW}", "-", "ECBC 2017 9.4.2.8 Table 9-5")
row("Chiller COP >=260 kWr", f"{I.CHILLER_COP_GE_260KW}", "-", "ECBC 2017 9.4.2.8 Table 9-5")
for k, v in I.FAN_MECH_EFF.items():
    row(f"Fan mech eff, {k}", f"{v:.2f}", "-", "ECSBC 2024 6.3.1 Tables 6.9-6.11")

hdr("6. GUIDELINE SCENARIOS")
print("%-4s %-6s %-9s %-9s %-22s %-9s %-10s %s" %
      ("KEY", "ACH", "OA ACH", "min f_OA", "FILTER", "PRESSURE", "T degC", "RH %"))
print("-" * W)
for g in GUIDELINES:
    f = g.min_f_oa()
    print("%-4s %-6s %-9s %-9s %-22s %-9s %-10s %s" % (
        g.key,
        g.ach_total if g.ach_total else "-",
        g.ach_outdoor if g.ach_outdoor else "-",
        f"{f:.3f}" if f is not None else "undef",
        (g.filter_class or "-")[:22],
        g.pressure or "-",
        f"{g.temp_c[0]}-{g.temp_c[1]}" if g.temp_c else "-",
        f"{g.rh_pct[0] or ''}-{g.rh_pct[1]}" if g.rh_pct else "-"))

hdr("7. BLOCKED - FAIL CLOSED, RAISES ON USE")
for b in (I.OUTDOOR_CO2_PPM, I.SYSTEM_PRESSURE_DROP_PA,
          I.ICU_PM_SIZE_DISTRIBUTION, I.OCCUPANCY_SCHEDULE):
    print(f"  {b.name}\n      closes with: {b.closes_with}")
