# ICU model inputs — confirmed data only

**Purpose:** the single input file for the well-mixed ICU + HVAC model (master §12).
**Rule:** every value below is traceable to a named primary document with an exact
edition and locator. Nothing pending, inferred, or averaged appears here. Values
still missing are named in §7 and left to their owner, not filled in.

**Scenario coverage:** single-bed ICU room only. Multi-bed/open ICU has no
verified geometry in evidence and is therefore absent, not estimated (§7).

---

## 1. Room geometry and occupancy

Source: **Australasian Health Facility Guidelines, Room Data Sheet, "1 Bed Room -
Intensive Care", Room Code 1BR-ICU**, issue date 12.11.2025, Revision 2, page 1.

| Symbol | Quantity | Value | Basis |
|---|---|---|---|
| `A` | briefed floor area | 25.00 m² | stated, page 1 |
| `H` | ceiling height | 3.0 m | stated, page 1 |
| `V` | room air volume | **75.0 m³** | derived, `A × H` |
| — | beds | 1 | page 5, `MMBE-116`, QTY 1 |
| `N_base` | occupancy, listed base | 3–5 persons | page 1: 1 patient + 1–2 visitors + 1–2 staff |
| `N_max` | occupancy, listed maximum | 11 persons | page 1: base + 4–6 additional staff as required |

`V = 75.0 m³` is a **gross geometric volume**. It is not a measured effective
well-mixed air volume, and no displacement correction for furnishings or
equipment is applied.

Corroborating geometry, not merged into the above: **HBN 04-02, 2013**, §4.14
(p9) minimum bed space 25.5 m²; §4.17 (p9) ceiling height 3 m recommended in bed
areas.

---

## 2. Supply airflow

    Q_s = ACH · V ,  V = 75.0 m³

| ACH | `Q_s` (m³/h) | `Q_s` (m³/s) | Source of the rate |
|---|---|---|---|
| 6 | 450.0 | 0.125000 | ASHRAE 170-2025 minimum total; ISCCM 2020 total |
| 10 | 750.0 | 0.208333 | HTM 03-01:2021 Table 3 and Appendix 2; SHTM 03-01:2014 Table A1 |

Outdoor-air flow where a source states an absolute floor:

| `ACH_OA` | `Q_OA` (m³/h) | `Q_OA` (m³/s) | Source |
|---|---|---|---|
| 2 | 150.0 | 0.041667 | ASHRAE 170-2025 minimum outdoor; ISCCM 2020 outdoor |

---

## 3. Outdoor-air fraction

    Q_OA = f_OA · Q_s ,   Q_R = (1 − f_OA) · Q_s

`f_OA` is a swept design variable over **0.20 – 1.00**. It is a project
sensitivity range, not a cross-guideline requirement. Each swept point carries
its own source-scoped compliance label:

| Source | Constraint on `f_OA` |
|---|---|
| ASHRAE 170-2025; ISCCM 2020 | Absolute floor of 2 outdoor ACH. Minimum `f_OA = 2 / ACH_total`, so **0.333 at 6 total ACH**. At 6 total ACH, `f_OA < 0.333` fails the floor. |
| HTM 03-01:2021 Table 3 and Appendix 2; SHTM 03-01:2014 Table A1 | **Undefined.** These critical-care rows state supply ventilation and cascade path but no outdoor-air value. The ASHRAE/ISCCM 2 ACH floor must not be imported into UK rows. |
| Victoria HTG-2020-004, §4.172 | **`f_OA = 0.50`** for its own ICU/CCU scenario. |

Outdoor flow across the sweep at `V = 75.0 m³`:

| `f_OA` | at 6 ACH total | at 10 ACH total |
|---|---|---|
| 0.20 | 90.0 m³/h = 1.20 ACH — below the ASHRAE/ISCCM floor | 150.0 m³/h = 2.00 ACH |
| 0.333 | 150.0 m³/h = 2.00 ACH | 250.0 m³/h = 3.33 ACH |
| 0.50 | 225.0 m³/h = 3.00 ACH | 375.0 m³/h = 5.00 ACH |
| 0.75 | 337.5 m³/h = 4.50 ACH | 562.5 m³/h = 7.50 ACH |
| 1.00 | 450.0 m³/h = 6.00 ACH | 750.0 m³/h = 10.00 ACH |

A 20 % fraction at 10 total ACH satisfies 2 outdoor ACH only as a parametric
ASHRAE/ISCCM case in which total ACH has been raised to 10. It is not a UK
requirement.

---

## 4. Guideline scenarios for Stage A

One row per document. Not reconciled, not averaged. Where a source is silent the
cell reads `not stated` and no credit is taken.

| # | Document, edition, locator | Total ACH | Outdoor | Filter | Pressure | T | RH |
|---|---|---|---|---|---|---|---|
| G1 | **ANSI/ASHRAE/ASHE 170-2025**, Table 7-1, "Critical care patient care station (FGI 2.2-2.6.2)" | 6 min | 2 ACH min | MERV-14 min | N/R | 21–24 °C | 30–60 % |
| G2 | **HTM 03-01 Part A, 2021**, Table 3, "Level 2 or 3 critical care individual room/open bays", p64 print | ≥10 ac/h | not stated | BS EN 1822 EPA10, final | +5 Pa to general area | 20–25 °C | floating, max 60 % |
| G3 | **HTM 03-01 Part A, 2021**, Appendix 2, "Critical care areas (Level 2 and 3 care)", p147 print | 10 ac/h | not stated | BS EN 16798 SUP1, supply | +10 Pa | not stated | not stated |
| G4 | **SHTM 03-01 Part A, Version 2, February 2014 (ARCHIVED)**, Appendix 1, Table A1, "Critical Care Areas", p139 | 10 ac/h | not stated | F7, supply | +10 Pa | 18–25 °C | not stated |
| G5 | **ISCCM Consensus Statement on ICU Planning and Designing, 2020**, Environmental Requirements → HVAC system of ICU | 6 | 2 ACH | 99 % efficiency down to 5 µm | no numerical general-ICU differential; airflow clean to dirty | 16–25 °C, enclosed patient modules | not stated |
| G6 | **VHHSBA HTG-2020-004, May 2020**, §4.172 "ICU and CCU", p34 | not in this clause | `f_OA = 0.50` | remote HEPA in the AHU, sited outside the ICU | positive, beds toward adjoining circulation | not in this clause | not in this clause |
| G7 | **AusHFG RDS 1BR-ICU, Rev 2, 12.11.2025**, page 1 HVAC checklist | not stated | not stated | **none** — HEPA checkbox unticked | **none** — positive and negative both unticked | not stated | not stated |
| G8 | **NABH Accreditation Standards for Hospitals, Sixth Edition, January 2025**, COP.9 | absent | absent | absent | absent | absent | absent |

G2 and G3 are the same document and disagree on both pressure (+5 vs +10 Pa) and
filter designation (EPA10 vs SUP1). Carry both as separate scenarios; do not
collapse them.

G4 is archived Scottish evidence, retained as historical. It is not the current
UK comparison basis.

G6 is jurisdiction-specific Victorian evidence. It does not substitute for the
AusHFG Part E or AS 1668.2 entry, which is not in evidence.

G7 records that the AusHFG room data sheet imposes **no** filter, pressure or
ventilation-rate requirement: only `AIRCONDITIONING: general` is ticked. Its
value to the model is the geometry in §1, not a service requirement.

### 4.1 Constrained versus free control parameters

Derived directly from the G-rows above. This is the feasible space each
guideline leaves to the optimiser: a bound is a constraint, `free` means the
guideline's verified ICU row states nothing and therefore gives no credit and
imposes no limit.

| # | `ACH_total` | `f_OA` | Filter | Pressure | T | RH | Temporal |
|---|---|---|---|---|---|---|---|
| G1 | ≥ 6 | ≥ 2/`ACH_total` | ≥ MERV-14 | **free** (N/R) | 21–24 °C | 30–60 % | turndown permitted when unoccupied; room-unit recirculation prohibited |
| G2 | ≥ 10 | **free** | EPA10 | +5 Pa | 20–25 °C | ≤ 60 % (no lower bound) | — |
| G3 | 10 (stated) | **free** | SUP1 | +10 Pa | **free** | **free** | — |
| G4 | 10 (stated) | **free** | F7 | +10 Pa | 18–25 °C | **free** | archived |
| G5 | 6 (stated) | 2 ACH | 99 % @ 5 µm | **free** (no numerical value) | 16–25 °C | **free** | — |
| G6 | **free** (not in clause) | **= 0.50 (equality)** | remote HEPA | positive | **free** | **free** | — |
| G7 | **free** | **free** | **free** (none selected) | **free** (none selected) | **free** | **free** | — |
| G8 | absent | absent | absent | absent | absent | absent | — |

Three consequences for the optimisation:

1. **The minimum-energy compliant point of each guideline sits at the lower
   bound of its constrained ranges.** Fan power rises steeply with flow and
   outdoor-air conditioning duty rises with `Q_OA`, so for Stage A the
   as-written performance of a guideline is evaluated at its floors, not at a
   mid-range choice.

2. **G6 is the only equality constraint on `f_OA`.** Every other source either
   sets a floor (G1, G5) or is silent. An equality removes `f_OA` from the
   optimiser entirely for that scenario.

3. **G2, G3 and G4 place no lower bound on outdoor air in their verified
   critical-care rows.** A literal-compliance optimiser minimising energy inside
   those rows alone would drive `f_OA` toward zero while still meeting the stated
   10 ac/h, filter and pressure requirements. This is a property of the rows as
   verified, and it is exactly the kind of gap Stage A exists to expose.

   **Caveat, and it matters:** only the critical-care rows of HTM 03-01:2021 and
   SHTM 03-01:2014 are in evidence. Neither full document has been inspected
   here. A general minimum-fresh-air provision elsewhere in those documents would
   change this conclusion. The finding must be stated as scoped to the verified
   rows until the surrounding clauses are checked.

---

## 5. Room temperature and relative humidity

These are **room/space design conditions**. No source in evidence gives a
supply-air dry-bulb temperature, supply humidity ratio, supply dew point or
supply relative humidity for ICU. Supply state must be derived from room
sensible and moisture balances, or supplied as a separately sourced design or
experimental boundary condition. It must never be labelled a guideline
requirement.

Common room operating interval, by intersection of G1, G2, G4, G5:

    T: 21–24 °C

This is a **selected** common interval that is mathematically compatible with all
four, not a value stated identically by any of them.

For humidity: 60 % upper limit is corroborated by G1 and G2. The 30 % lower limit
comes from G1 alone. G3, G4 and G5 state no RH range.

Per master decision **D1**, T and RH feed the energy model. Direct T/RH
dependence of filter capture, deposition, microbial survival and UV
susceptibility is outside current contaminant-physics scope.

---

## 6. Pressure

Recorded as a guideline-compliance constraint only. Per master §13, pressure is
not converted into a pollutant-removal term, and no leakage coefficients
`C_L`, `n` are in evidence, so `Q_leak = C_L (ΔP)^n` is not evaluated.

Values as stated: G2 +5 Pa; G3 +10 Pa; G4 +10 Pa; G6 positive, beds toward
circulation; G1 N/R; G5 no numerical general-ICU differential; G7 none selected.

---

## 7. Required by the model, not supplied by this file

| Model term (§12) | Status | Owner |
|---|---|---|
| `P_i(t)` filter penetration, size-resolved | Guidelines give classes (MERV-14, EPA10, SUP1, F7, 99 %@5 µm), not efficiency curves. ASHRAE 170-2025 §6.4 topology is not in evidence, so it is not established whether MERV-14 applies to full supply, mixed air or recirculation only. | filter model |
| `S_i(t)` source terms | not in this file | source/generation model |
| `k_dep,i` deposition | not in this file | contaminant physics |
| `C_out,i` outdoor concentrations | not in this file | concentration evidence database |
| `Q_inf`, `Q_leak` | no leakage parameters in evidence | deferred, master §13 |
| supply-air state | no ICU supply condition in any source | energy model, from room balances |
| multi-bed geometry | no verified source | pending acquisition |

Standards still absent from evidence: AusHFG Part E; AS 1668.2:2012/2024;
FGI 2022 adult ICU room-area clause; ASHRAE 170-2025 §6.4; NBC 2016 Part 8
Section 3; DIN 1946-4:2018-09 + A1:2025-11; NF S 90-351 normative clauses;
CSA Z317.2 and CSA Z8000.

---

## 8. Sources

1. Australasian Health Infrastructure Alliance. *Australasian Health Facility Guidelines, Room Data Sheet, 1 Bed Room - Intensive Care, Room Code 1BR-ICU.* Revision 2, issue date 12.11.2025. Page 1 (area, height, occupancy, HVAC checklist); page 5 (bed).
2. ANSI/ASHRAE/ASHE. *Standard 170-2025, Ventilation of Health Care Facilities.* Table 7-1, "Critical care patient care station (FGI 2.2-2.6.2)".
3. NHS England. *Health Technical Memorandum 03-01: Specialised ventilation for healthcare premises, Part A.* 2021. Table 3, printed page 64; Appendix 2, printed page 147.
4. NHS Scotland. *SHTM 03-01 Part A – Design and Validation.* Version 2, February 2014, ARCHIVED. Appendix 1, Table A1, printed page 139.
5. NHS England. *Health Building Note 04-02: Critical care units.* 2013. §4.14 and §4.17, printed page 9.
6. Indian Society of Critical Care Medicine. *Experts Committee Consensus Statement on ICU Planning and Designing.* 2020. Environmental Requirements → HVAC system of ICU.
7. Victorian Health and Human Services Building Authority. *Engineering guidelines for healthcare facilities: Volume 4 – Heating, ventilation and air conditioning.* Health technical guideline HTG-2020-004, May 2020. §4.172, printed page 34.
8. NABH. *Accreditation Standards for Hospitals.* Sixth Edition, January 2025. COP.9.

Verification of source 1 was performed in this session by direct inspection of
the PDF, including rendering page 1 to resolve checkbox state. Sources 2–8 are
recorded from *ICU guideline archive verification*, 2026-08-29, held at
`docs/sources/`.
