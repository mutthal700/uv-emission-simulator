# ICU model inputs and gap register

**Purpose:** the single input file for the well-mixed ICU + HVAC model.
**Rule:** every value is traceable to a primary document with an exact edition
and locator. Nothing pending, inferred or averaged appears as an input. Missing
quantities are named in Part I, never filled in.

**Scenario coverage:** single-bed ICU room only. Multi-bed has no verified
geometry and is absent, not estimated.

---

# PART I — GAPS TO CLOSE

Ordered by what each unblocks, not by how hard it is. The seven in §0.1 are
cheap and unblock the most.

## 0.1 Do these first

| # | Gap | Why it matters | What closes it |
|---|---|---|---|
| 1 | **Patient ventilator exhaust path** | Decides whether patient VCO₂ is a room source **at all**. If the expiratory limb is scavenged, the largest single CO₂ term disappears and every CO₂ result changes. | One line of site documentation: does the ventilator discharge expired gas to room air, or to a scavenging/exhaust connection? |
| 2 | **Staff/visitor demographic scenario** | Persily Table 4 varies by sex and age; the male 21–<30 row cannot stand for nurses, doctors, visitors and cleaners. This is a **declaration you make**, not data to find. | State the sex/age/met composition you want to model, and it becomes a declared scenario with a sensitivity range. |
| 3 | **Five-city climate data** (hourly T, RH, PM₂.₅, PM₁₀) | Turns every outdoor-air conditioning **ratio** into absolute kWh, and supplies `C_out` for PM. You already hold this. | Send the files, with temporal resolution stated. |
| 4 | **Outdoor CO₂ baseline per zone** | Converts CO₂ **excess** to absolute ppm, which is what any allowable limit is written against. | A sourced outdoor CO₂ value per climate zone. |
| 5 | **Locators for the master §1.1 regime table** | Those CO₂/PM/bacteria/fungi ranges are the validation targets for D7. Without full locators they cannot be promoted under your own citation rule. | Document title, edition/year, table/section with named row for the Tang, Aligarh and Chennai entries. |
| 6 | **Victoria HTG-2020-004 "Reference table 1"** | §4.173 points to it; it very likely carries the air-change rate. G6 is currently unsimulatable for want of one number. | The missing table from the Victorian guideline. |
| 7 | **HTM 03-01 Part A general fresh-air clauses** | Settles the **headline Stage A finding** (§20.2). If a general minimum-fresh-air provision exists elsewhere in the document, that finding is void. | The sections of HTM 03-01 Part A outside Table 3 and Appendix 2 that address minimum outdoor air. |

## 0.2 Guideline completeness

| Gap | Status | What closes it |
|---|---|---|
| AusHFG Part E, or AS 1668.2:2012/2024 | **Australia has geometry but no ventilation requirement at all** | the intensive-care ventilation entry with its table/section |
| ASHRAE 170-2025 §6.4 filter topology | blocks knowing whether MERV-14 applies to full supply, mixed air or recirculation only | §6.4 of the 2025 edition, plus 2026 errata |
| Other Indian documents (6–12 ACH, OA 2 to 4–5 ACH spread) | named in the master without locators, so they cannot become scenarios | document title, edition, table/section per document |
| NBC India 2016 Part 8 §3 | absent | ICU rows of Tables 4, 6, 7 |
| DIN 1946-4:2018-09 + A1:2025-11 | absent; only the 2008 edition is held, as history | Table 1 room classification and the intensive-care row |
| NF S 90-351 | only secondary explanatory material held | the AFNOR normative filtration/topology clauses |
| FGI 2022 adult ICU area clause | absent | the room-area clause (geometry is already closed, so this is corroboration) |
| CSA Z317.2 / Z8000 | optional | ICU row; critical-care room area, with edition named |

## 0.3 Filter — the whole of Tier 2 depends on this

The guidelines give filter **classes**, never efficiency curves. MERV-14, EPA10,
SUP1, F7 and "99 % down to 5 µm" cannot produce `P_i(dp)`.

| Gap | What closes it |
|---|---|
| **Fractional efficiency η(dp)** for candidate products | manufacturer curves at the duty point. This is the real requirement — test standards define *how* to measure, products define *what* the curve is |
| Clean ΔP and loading curve | manufacturer data at rated flow, plus dust-holding capacity |
| Class definitions, for compliance checking only | ASHRAE 52.2, BS EN 1822, ISO 16890, EN 779 |

Two constraints that must not be violated:

- **MERV E1/E2/E3 are reporting bands, not model bins.** Substituting them for
  the PM state bins is a category error.
- Curves measured at a rated face velocity do not apply directly here: at
  6 and 10 ACH this duct runs at **0.53 and 0.88** of a 2.54 m/s reference, so
  efficiency is higher and ΔP lower than rated.

## 0.4 Pollutant state

| Gap | Consequence while open |
|---|---|
| **ICU PM size distribution** `dN/dlogDp` or `dM/dlogDp` | PM₂.₅ and PM₁₀ are mass metrics, not distributions. No size-resolved filtration or deposition can be applied to PM at all |
| **TVOC ICU concentration** | no evidence of any kind; TVOC cannot be modelled |
| **ICU allowable limits** | **"how much must we reduce" has no sourced target.** The study can only report delivered concentration against validation regimes |
| Deposition model + room S/V | obtainable from generic aerosol literature — not ICU-specific, so not truly blocked |

## 0.5 Temporal — Stage C only

Stage A and Stage B are **not blocked** by these, because every guideline sees
the same occupancy.

| Gap | What closes it |
|---|---|
| ICU SOP / IPC event schedule | hospital document with unit, number, revision, effective date, section, approval status |
| Measured ICU CO₂ trace **with its ventilation conditions** | a Tier A source-reconstruction study; Tier B gives shape but not magnitude |
| ISO 8996:2021 activity values | licensed pages of the activity table; no substitute may be relabelled as ISO 8996 |
| Bacteria/fungi temporal route | direct ICU evidence that viable emission tracks occupancy. Magnitude calibration does **not** supply this |

## 0.6 Energy

| Gap | Consequence while open |
|---|---|
| System pressure drop at a duty point | only fan power **ratios** are available, not absolute watts |
| Room thermal loads | the reheat penalty is invisible, and it falls hardest on the 10 ac/h rows |
| Actual fan and chiller performance | not required for a comparison — code minima serve, since the same plant serves every scenario |

## 0.7 Not blocking

Rousing's numeric pressure basis (GE states STPD and 0 °C dry but no pressure).
Kagan is fully referenced and sufficient; Rousing simply cannot be
pressure-harmonised and is carried unconverted.

---

# PART II — CONFIRMED INPUTS

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

---

## 7. CO₂ source classes

Volumetric rates are meaningless without their gas reference state, so each
carries one. **Altunalan et al. (2026) is excluded**: the article's Results
prose and Table 2 contradict each other on VCO₂ versus VO₂ and the source
permits no defensible choice.

| Class | Source-reported | m³/s (unit conversion) | Reference state |
|---|---|---|---|
| Patient — Kagan et al., *Critical Care* 22:186 (2018) | 244.5 ± 85.9 mL/min | 4.075e-06 ± 1.432e-06 | **Dräger Evita 4 STPD**, 0 °C, 1013 hPa, dry |
| Patient — Rousing et al., *Ann Intensive Care* 6:16 (2016) | 273 ± 63 mL/min | 4.550e-06 ± 1.050e-06 | GE E-CAiOVX, 0 °C dry; **numeric pressure not stated** |
| Occupant scenario — Persily & de Jonge (2017) Table 4, **male 21–<30**, p875 | 0.0039 / 0.0048 / 0.0056 / 0.0064 L/s at 1.0 / 1.2 / 1.4 / 1.6 met | 3.90 / 4.80 / 5.60 / 6.40 e-06 | 273 K, 101 kPa |

Both patient values are **cohort means, not universal emission factors**. The
Persily row is a **declared demographic scenario**, not a generic staff class,
and the met level is a declared parameter — ISO 8996:2021 is blocked.

### 7.1 Gas-basis reconciliation

Persily converts exactly to the Dräger basis with no empirical input:

    V_Dräger = V_Persily × (273.15/273) × (101/101.3) = V_Persily × 0.997586322858

reproduced by the model to 1e-12. Rousing is **not** pressure-harmonised.

Sources are held as `GasState` objects carrying their own reference `T` and `P`,
with `to_molar()` for reference-state-independent work. The room balance uses
flows and ppm at actual room conditions, so every source is converted to a
**declared** evaluation state of 297.15 K / 101325 Pa before entering it.

**This is material, not cosmetic:** the conversion raises the CO₂ source by
**+8.8 %** (patient) and **+8.5 %** (Persily scenario).

### 7.2 Identifiability

The single-bed room fixes the patient count, so the patient term can be
subtracted:

    S_non-patient(t) = S_total(t) − S_patient

That is a **source strength**, not a headcount. Dividing by one reference rate
yields **"equivalent occupants"**, valid only if every non-patient shares that
rate — which Persily shows they do not. Label results accordingly.

Patient VCO₂ is a room source **only if** the ventilator discharges to room air
(§0.1, gap 1).

## 8. Deposition `k_dep`

Now in scope. It is **not** blocked: deposition depends on particle size, room
surface-to-volume ratio and near-surface turbulence, not on the room being an
ICU, so the generic aerosol literature applies. Required: a size-resolved
deposition model with this room's S/V ratio, plus a sensitivity band.

`k_dep` does not cancel across scenarios — at low ACH it is relatively more
important, so it bends the shape of the concentration-versus-ACH response.

---

## 9. Energy reference values

| Quantity | Value | Source |
|---|---|---|
| Air-cooled chiller COP, <260 kWr | 2.8 (IPLV 3.5) | ECBC 2017, §9.4.2.8, Table 9-5 |
| Air-cooled chiller COP, ≥260 kWr | 3.0 (IPLV 3.7) | ECBC 2017, §9.4.2.8, Table 9-5 |
| AHU fan mechanical efficiency | 65 % (IE3) / 70 % (IE4) / 75 % (IE4) | ECSBC 2024, §6.3.1, Tables 6.9–6.11 |

These are **code-referenced minima, not measured equipment performance**, and
must be labelled as such. For a comparison between guidelines that is
sufficient, because the same equipment serves every scenario. Applicability of
ECSBC 2024 to a hospital must be established separately — its title states
commercial and office buildings.

---

## 10. Room thermal loads

Now in scope. No ICU load data is in evidence, and loads matter to the guideline
comparison through **one mechanism only**: reheat. A latent load in a humid
climate drives the coil below dewpoint; the air must then be reheated to avoid
overcooling the room, and that penalty grows with supply flow — so it falls
hardest on the 10 ac/h scenarios.

Recommended treatment, pending data: run each scenario at zero load and at a
plausible high load across the five climate zones, and report whether the
**ranking** of guidelines changes. If it does not, the comparison stands at zero
load with the insensitivity reported as a result. If it does, the load becomes a
required input. This converts a missing measurement into a bounded finding.

---

## 11. ICU pollutant concentrations, type and size

Per master §1.1 these are **validation regimes, not regulatory limits and not
source inputs**. They are what a simulated distribution is checked against
(D7), never what is fed in. Provenance tiers are kept apart.

### 11.1 Physical character — this decides which removal terms apply

| Pollutant | Type | Size basis | Removal available |
|---|---|---|---|
| CO₂ | gas | not applicable | dilution only |
| TVOC | gas mixture, lumped surrogate | not applicable | dilution; adsorption only if a carbon stage is fitted |
| PM₂.₅ | particulate **mass metric** | mass below 2.5 µm — *not a size distribution* | filtration, deposition |
| PM₁₀ | particulate **mass metric** | mass below 10 µm — *not a size distribution* | filtration, deposition |
| Bacteria | viable particulate | six Andersen stages, 0.65 µm to >7 µm | filtration, deposition, **UVGI** |
| Fungi | viable particulate | six Andersen stages, 0.65 µm to >7 µm | filtration, deposition, **UVGI** |

Two consequences that constrain the whole model:

- **Neither gas is touched by the filter or the lamp.** CO₂ and TVOC are
  dilution-controlled, so `f_OA` is the only lever on them. UVGI cannot help.
- **PM₂.₅ and PM₁₀ are mass metrics, not size bins.** A size-resolved filter
  efficiency cannot be applied to them directly; that needs `dN/dlogDp`, which
  is blocked (§0.4). The viable species are the only ones with a verified size
  structure.

### 11.2 Verified concentrations

Kim, Kim & Kim, *Industrial Health* 48(2):236–243 (2010), ICU rows:

| Quantity | Value | Locator |
|---|---|---|
| Airborne bacteria, ICU total | 202 CFU/m³ | Table 2 |
| Airborne bacteria, respirable | 142 CFU/m³ | Table 2, stages 3–6 |
| Airborne fungi, ICU total | 65 CFU/m³ | Table 3 |
| Airborne fungi, respirable | 47 CFU/m³ | Table 3, stages 3–6 |

### 11.3 Reported in the project master, not yet locator-complete

Carried from master §1.1 with partial attribution. Under the citation rule
locked on 2026-08-29 these **cannot be promoted** until a full document title,
edition and table/section with named row is supplied.

| Pollutant | Clean | Moderate | India high | Event tail |
|---|---|---|---|---|
| CO₂ (ppm) | 450–800 | 828–1570 (Tang) | 1822–2258 (Aligarh) | occupancy/visitation peaks |
| PM₂.₅ (µg/m³) | 1–5 | 20–35 | 50–98 | activity/cleaning peaks |
| PM₁₀ (µg/m³) | 0.9–10 | 10–60 | 57–118 | can be much higher instantaneously |
| Bacteria (CFU/m³) | 70–250 | 250–450 | 94–151 (Indian active sampler) | >1000 to ~7236 (Tang) |
| Fungi (CFU/m³) | 2.6–70 | — | low single digits (Chennai) | >1000 to ~11654 (Tang) |
| **TVOC** | **BLOCKED — no ICU concentration evidence held at all** | | | |

### 11.4 Allowable limits

No ICU-specific allowable limit for any pollutant is in evidence. Until one is
found, "how much must be reduced" has no sourced target and the study can only
report delivered concentration against the validation regimes above.

---

---

# PART III — MODEL ARCHITECTURE

## 12. Duct geometry and model architecture

### 12.1 Duct (design input, fixed by the researcher)

| Quantity | Value |
|---|---|
| Cross-section | 0.3048 m × 0.3048 m (square) |
| Face area `A_d` | 0.092903 m² (exactly 1.000 ft²) |
| Rig length | 6 m (master §4, physical rig) |
| Sections | inlet/mixing → filter → coils → UVGI → outlet |

Derived duct velocity and transit time at the guideline flows, `v = Q_s / A_d`:

| ACH | `Q_s` (m³/s) | `v` (m/s) | `v` (fpm) | transit over 6 m | transit per 1 m |
|---|---|---|---|---|---|
| 6 | 0.125000 | 1.345 | 265 | 4.46 s | 0.74 s |
| 10 | 0.208333 | 2.242 | 441 | 2.68 s | 0.45 s |

These velocities are low for a supply duct. Two consequences: if the filter spans
the full duct face, its face velocity is 0.53 and 0.88 of a 2.54 m/s (500 fpm)
reference rating at 6 and 10 ACH respectively, which raises capture efficiency
and lowers clean pressure drop relative to rated conditions; and UV residence
time is set by these transit times, so the dose available per metre of lamp
section is fixed by the ACH scenario.

### 12.2 Architecture decisions

| # | Decision |
|---|---|
| A1 | **Room is solved as a state variable and the loop is closed.** The room mass balance of master §12 runs; the recirculated-air concentration at the duct inlet is the room concentration at time `t`; the duct outlet is the room supply. |
| A2 | **Duct sections are plug flow with residence time.** UV dose is irradiance × residence time, consistent with the ray-tracing dose profile. The room remains well-mixed; the duct does not. |
| A3 | **T and RH guideline bands are room targets; the supply state is additionally bounded.** Supply state is derived from the room sensible and latent balance, subject to a separately stated supply constraint. The supply bound is not a guideline value and must be sourced or declared as a design choice. |
| A4 | **Temporal variation is outdoor climate plus an occupancy profile.** Five Indian climate zones supply outdoor `T`, `RH`, `PM2.5`, `PM10`. The occupancy profile is not yet sourced; see §10. |

| A5 | **Exhaust is taken off the return immediately before the duct inlet, and is exactly balanced against outdoor air.** `Q_exhaust = Q_OA`, so `Q_recirc = Q_s − Q_OA`. With no infiltration, room outflow equals `Q_s` and the room's outdoor-air exchange equals `Q_OA`. |
| A6 | **Return concentration equals room concentration** (perfect mixing at the return). |
| A7 | **CO₂ is controlled by outdoor-air fraction alone** — no filter or UV credit. TVOC is in scope and, absent a gas-phase stage, is governed by the same dilution-only mechanism. |
| A8 | **Guideline runs carry no OA pre-filter** until ASHRAE 170-2025 §6.4 topology is in evidence. The pre-filter is reserved for the independent optimisation. |
| A9 | **Victoria's remote HEPA is the main filter bank**, not an OA-branch pre-filter. |

Stream balance under A5, at `V = 75.0 m³`:

| ACH | `f_OA` | `Q_s` (m³/h) | `Q_OA` = `Q_exhaust` | `Q_recirc` |
|---|---|---|---|---|
| 6 | 0.333 | 450.0 | 150.0 | 300.0 |
| 6 | 0.50 | 450.0 | 225.0 | 225.0 |
| 6 | 1.00 | 450.0 | 450.0 | 0.0 |
| 10 | 0.20 | 750.0 | 150.0 | 600.0 |
| 10 | 0.50 | 750.0 | 375.0 | 375.0 |

### 12.3 Transport delay

Plug flow in the duct implies a delay between duct outlet and room inlet. Its
magnitude against the 15-minute scheduler:

| ACH | 6 m transit | as fraction of a 15-min step |
|---|---|---|
| 6 | 4.46 s | 0.50 % |
| 10 | 2.68 s | 0.30 % |

The delay is retained in the model structure because it is physically real and
costs nothing to carry, but it is **unresolvable at 15-minute resolution** and
will not change any annual result. It becomes significant only in a
rig-matched transient validation at sub-minute resolution.

---

## 13. Build strategy under incomplete ICU evidence

The study is **comparative**. That fact decides how much data each term needs:

> A term requires accurate data only if it can change the **ranking** of the
> guidelines. A term that shifts every scenario by the same amount needs a
> defensible constant and a sensitivity check, not a precise ICU measurement.

Applying that test:

| Term | Interacts with the control variables? | Data burden |
|---|---|---|
| Room mass balance, `Q_s`, `f_OA` | yes — they *are* the control variables | already closed (§1–§4) |
| CO₂ | yes, via `f_OA` only | closed for the patient class (§11) |
| Fan and OA-conditioning energy | yes, via `Q_s` and `Q_OA` | code-referenced values suffice (§13) |
| `k_dep` | yes — relatively more important at low ACH, so it bends the ACH response | generic aerosol literature, not ICU-specific (§12) |
| Filter `P_i` and PM size distribution | yes — filter classes differ mainly in the fine range, so ranking depends on it | bounding across plausible distributions |
| Room loads / reheat | only through reheat, which is climate- and latent-driven | bounding analysis (§14) |
| Occupancy schedule | Stage C only — it is what concentration-responsive control responds to | site-specific, currently blocked |
| Actual fan and chiller performance | no — same equipment across all scenarios | not required for comparison |

### 13.1 Consequent build order

- **Tier 1 — buildable now, nothing blocked.** Room mass balance, ventilation,
  `f_OA` sweep, CO₂, fan energy and outdoor-air conditioning energy at
  code-referenced efficiency. This alone answers, for every guideline, what CO₂
  it delivers and at what ventilation energy — a complete Stage A result.
- **Tier 2 — needs generic, obtainable data.** `k_dep`, size-resolved PM and
  viable transport, filter efficiency curves.
- **Tier 3 — needs site or equipment data, Stage C only.** Occupancy schedule,
  measured fan/chiller performance, ICU thermal loads.

Stage A and Stage B are **not blocked** by the missing occupancy schedule,
because every guideline sees the same occupancy. Only Stage C, where control
responds to occupancy, requires it.

---

## 14. Diurnal model

Occupancy `N(t)` carries the time variation; sources follow from it.

### 14.1 Two routes to `N(t)`

**Route A — schedule.** `occupancy.profile_from_events` builds `N(t)` from named
events, each carrying a `source` field naming the document, section and
revision. It **fails closed** on an empty schedule and rejects any event without
a source, so the blocked SOP cannot be quietly replaced by a generic profile.

**Route B — CO₂ inversion.** `occupancy.co2_inversion` runs the room balance
backwards on a measured trace. No schedule is needed: occupancy is already
encoded in the CO₂ signal. Inverting the exact solution rather than a finite
difference:

    a = exp(-(Q_OA / V) · Δt)
    S_k = Q_OA · [C_{k+1} − a·C_k − C_out·(1 − a)] / (1 − a) / 10⁶

Then, because the single-bed room fixes the patient count and the patient rate
is measured (§7):

    N_non-patient(t) = (S(t) − S_patient) / G_person

Round-tripped to 1e-9 on a noiseless synthetic trace, including at a coarse
1-hour step that a finite-difference inversion would not survive. **This is an
implementation test, not validation** against independent occupancy, ventilation
or CO₂ measurements.

Two limits on what the inversion returns. It is exact only where `Q_OA`, `C_out`
and `S` are constant across the interval; where the source varies within an
interval the result is an exponentially weighted interval **average**, so a
one-hour interval cannot resolve events inside that hour. And the recoverable
quantity is non-patient **source strength**, not headcount — dividing by one
reference rate yields **"equivalent occupants"**, valid only if every
non-patient shares that rate, which Persily shows they do not.

### 14.2 Propagating `N(t)` to the other pollutants

**Corrected 2026-08-29.** The CO₂-derived temporal profile is used **for CO₂
only**. It is not transferred to bacteria, fungi, PM or TVOC without direct ICU
evidence supporting that pollutant-specific relationship. Calibrating a
bacterial or fungal *magnitude* against a reported concentration does not
validate an occupancy-shaped *temporal profile* for it.

| Pollutant | Route | Status |
|---|---|---|
| CO₂ | patient at the measured ICU rate plus a declared non-patient scenario | machinery closed; inputs blocked (§0.5) |
| Bacteria, fungi | **no sourced temporal route** | occupancy-shaped profile is not evidenced; magnitude calibration alone does not supply one |
| PM | needs pollutant-specific outdoor penetration, indoor sources, resuspension, deposition, filtration and size-resolved removal | blocked |
| TVOC | dilution only | blocked, no evidence at all |

Steady occupancy values may be used **only as explicitly declared simulation
scenarios**. They must not be described as a validated diurnal occupancy
profile.

### 14.3 What the diurnal model cannot yet do

Route A is blocked on the SOP. Route B needs a measured ICU CO₂ trace *with its
ventilation conditions* — Tier A source-reconstruction studies qualify, Tier B
studies with incomplete HVAC metadata give shape but not magnitude. Until one of
those arrives the machinery is built and tested but unfed, and Stage A proceeds
on the steady-state occupancy levels of §1 instead.


---

---

# PART IV — RESULTS SO FAR

## 15. Stage A, Tier 1

Computed by `scripts/run_stage_a.py`; 21 tests pass. CO₂ is reported as an
**excess above outdoor**, which removes the need for the unsourced outdoor
baseline; energy is reported as **ratios**, which removes the need for equipment
data.

### 15.1 CO₂ excess above outdoor, ppm

Patient at the Kagan measured rate; others as the Persily male 21–<30 scenario
at 1.2 met; all converted to the declared room state.

| | ACH | f_OA | Q_s m³/h | Q_OA m³/h | 3 occ | 5 occ | 11 occ |
|---|---|---|---|---|---|---|---|
| G1, G5 | 6 | 0.333 | 450 | 150 | **356** | **606** | **1356** |
| G2, G3, G4 | 10 | undefined | 750 | — | see §15.3 |
| G6, G7, G8 | — | — | — | — | not simulatable, no rate stated |

### 15.2 Relative energy, referenced to G1 at its floors

| | Q_s ratio | fan power | OA conditioning |
|---|---|---|---|
| G1, G5 | 1.00 | 1.00× | 1.00× |
| G2, G3, G4 | 1.67 | **4.63×** | **5.00×** |

Fan ratio is the cube law for a fixed system curve; a loading filter departs
from it. OA ratio is at equal enthalpy difference.

### 15.3 The UK rows are a range, not a number

Because G2/G3/G4 state no outdoor-air value, their result spans the sweep:

| f_OA | Q_OA m³/h | 3 occ | 5 occ | 11 occ |
|---|---|---|---|---|
| 0.05 | 37.5 | **1425** | 2425 | **5425** |
| 0.10 | 75.0 | 713 | 1213 | 2713 |
| 0.20 | 150 | 356 | 606 | 1356 |
| 0.333 | 249.8 | 214 | 364 | 815 |
| 0.50 | 375 | 143 | 243 | 543 |
| 1.00 | 750 | 71 | 121 | 271 |

### 15.4 Response speed

t95, the time to close 95 % of the gap to steady state, is set by outdoor
airflow, not total supply: **89.9 min** at G1's 150 m³/h, **18.0 min** at
750 m³/h. This is the response available to any concentration-responsive control
in Stage C.

## 16. Findings

**16.1 Four of eight guidelines are incomplete as ventilation specifications.**
G6, G7 and G8 state no air-change rate; G2, G3 and G4 state no outdoor-air
value. Only G1 and G5 specify both.

**16.2 The verified UK rows place no lower bound on outdoor air.** An optimiser
minimising energy under literal compliance could drive `f_OA` toward zero while
still meeting the stated 10 ac/h, filter and pressure requirements — paying
4.63× the fan power of G1 while delivering **worse** CO₂. *Scoped strictly to
the verified rows; see §0.1 gap 7.*

**16.3 Guidelines disagree on ACH by a factor of 1.67**, which propagates to
4.63× in fan power and 5× in outdoor-air conditioning.

**16.4 Filtration is specified in four incommensurable systems**, one of which
(SUP1) is an air-quality category rather than a filter class.

**16.5 HTM 03-01:2021 is internally inconsistent in two places** — +5 vs +10 Pa,
and EPA10 vs SUP1 — between Table 3 and Appendix 2 of the same document.

**16.6 No ICU-specific allowable limit exists in evidence** for any pollutant.

---

# PART V — PROVENANCE

## 17. Sources

1. AHIA, *AusHFG Room Data Sheet, 1 Bed Room – Intensive Care, 1BR-ICU*, Rev 2, 12.11.2025 — read in full in session, including page-1 checkbox state resolved by rendering.
2. ANSI/ASHRAE/ASHE *Standard 170-2025*, Table 7-1, critical care patient care station.
3. NHS England, *HTM 03-01 Part A*, 2021 — Table 3 p64; Appendix 2 p147.
4. NHS Scotland, *SHTM 03-01 Part A* v2, Feb 2014, ARCHIVED — Appendix 1 Table A1 p139.
5. NHS England, *HBN 04-02*, 2013 — §4.14, §4.17, p9.
6. ISCCM, *Consensus Statement on ICU Planning and Designing*, 2020 — Environmental Requirements.
7. VHHSBA, *HTG-2020-004 Vol 4 HVAC*, May 2020 — §4.172 p34.
8. NABH, *Accreditation Standards for Hospitals*, 6th ed., Jan 2025 — COP.9.
9. Kagan et al., *Critical Care* 22:186 (2018). Dräger *IfU Evita 4 SW 4.n*, Ed. 5, 2015-01, doc 9039485, p176.
10. Rousing et al., *Ann Intensive Care* 6:16 (2016). GE *CARESCAPE Clinical Reference* 2040384-003A, ch.12.
11. Persily & de Jonge, *Indoor Air* 27(5):868–879 (2017), Table 4, p875.
12. Kim, Kim & Kim, *Industrial Health* 48(2):236–243 (2010), Tables 2–3.
13. BEE, *ECBC 2017* §9.4.2.8 Table 9-5; *ECSBC 2024* §6.3.1 Tables 6.9–6.11.

Audits held at `docs/sources/`: guideline archive verification, Q2/Q4/Q11/Q19
audit, CO₂ generation audit, project master v9.

## 18. Corrections log

| Date | Correction |
|---|---|
| 2026-08-29 | **AusHFG HVAC is a checklist.** Only `AIRCONDITIONING: general` is ticked. The sheet is not a HEPA requirement, mandates no pressure regime, and does not select natural ventilation. Checkbox glyphs sit at x≈553 pt and are invisible to text extraction; resolved by rendering page 1 at 7×. |
| 2026-08-29 | **HBN bed space is 25.5 m², not 26 m²**; **ISCCM is 6 ACH total / 2 outdoor, not ≥12**. Both earlier figures came from search summaries. |
| 2026-08-29 | **Altunalan excluded** — Results prose and Table 2 contradict each other on VCO₂ vs VO₂. |
| 2026-08-29 | **Gas reference states separated.** Kagan is Dräger STPD, Persily is 273 K/101 kPa, Rousing's pressure basis is unstated and blocked. Conversion to room state raises CO₂ sources 8.5–8.8 %. |
| 2026-08-29 | **Persily relabelled** a male 21–<30 demographic scenario, not a generic staff class. |
| 2026-08-29 | **Occupancy output relabelled** "equivalent occupants"; the recoverable quantity is source strength, not headcount. |
| 2026-08-29 | **CO₂ temporal profile is for CO₂ only.** An occupancy-shaped profile for bacteria, fungi, PM or TVOC is not evidenced; magnitude calibration does not supply one. |
| 2026-08-29 | **Round-trip is an implementation test**, not validation against independent measurement. |
