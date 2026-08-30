# ICU model inputs and gap register

**Purpose:** the single input file for the well-mixed ICU + HVAC model.
**Rule:** every value is traceable to a primary document with an exact edition
and locator. Nothing pending, inferred or averaged appears as an input. Missing
quantities are named in Part I, never filled in.

**Scenario coverage:** single-bed ICU room only. Multi-bed has no verified
geometry and is absent, not estimated.

> **Revised 2026-08-30** per `docs/sources/ICU_MODEL_INPUTS_EVIDENCE_AUDIT.md`.
> Values now carry an admissibility class: **ACCEPTED** (stated in an identified
> primary document), **DERIVED** (arithmetic on accepted data plus
> researcher-defined geometry), **RESEARCHER-DEFINED** (a chosen boundary or
> scenario, not evidence), **BLOCKED** (no substitute inserted). Several earlier
> results are **WITHDRAWN**; see §16.

---

# PART I — GAP REGISTER

Revised 2026-08-30. Ordered by what each unblocks. Nothing here is filled by
assumption, proxy or placeholder.

## 0.1 Closed since the last revision

| Gap | Closed by |
|---|---|
| HTM general fresh-air provisions | **HTM 03-01:2021 §8.6 p41**, see also §9.120: fresh air ≥ 10 L/s·person; where recirculating, ≥ 20 % or the person-based figure, whichever is greater. **SHTM 03-01:2014 §2.37 p26** gives the 20 % fraction only. The two are not combined. |
| The unnamed Indian national guideline | **MoHFW, *Guidelines for HDU & ICU*, March 2022**, p24 and Annexure III p47 — carried as **G9**, not merged with ISCCM |
| ASHRAE critical-care row | **ANSI/ASHRAE/ASHE 170-2021, Table 7-1, Critical care patient care station**, on the researcher's attestation that the previously recorded figures are the 2021 row. They had been mislabelled 170-2025. **170-2025 is not in evidence and no scenario may claim it.** §6.4 topology is still not held for either edition |

## 0.2 Do these first

| # | Gap | Why it matters | What closes it |
|---|---|---|---|
| 1 | **Ventilator and breathing-circuit configuration for this ICU** | Decides whether patient VCO₂ is a room source **at all**, and gates patient-inclusive CO₂ entirely. | The specific ventilator model and circuit arrangement, and whether expired gas discharges to the room or to scavenging/exhaust. **A generic statement about ICU ventilators is not sufficient.** |
| 2 | **Observed staff/visitor composition** | A researcher declaration yields a **labelled sensitivity scenario**, not representative ICU data. An actual-ICU prediction needs the real thing. | Site roster composition plus activity categories and timing. |
| 3 | **Actual ICU room temperature and pressure** | Every CO₂ figure is currently evaluated at a *researcher-selected* 297.15 K / 101325 Pa. Until the room state is measured, no CO₂ result is source-backed. | Site measurement, or accept the molar route and report molar quantities. |
| 4 | **ASHRAE 170 §6.4 filter-bank topology** | The 170-2021 row gives MERV-14 but not **which airstream** it acts on — full supply, mixed air or recirculation only. | §6.4 of the edition held. |
| 5 | **Five-city climate data** (hourly T, RH, PM₂.₅, PM₁₀) | Turns conditioning ratios into absolute energy and supplies `C_out` for PM. You hold this. | Send the files with temporal resolution stated. |
| 6 | **Outdoor CO₂ baseline per zone** | Converts CO₂ **excess** to absolute ppm — the form any limit is written in. | A sourced value per zone. |
| 7 | **Victoria HTG-2020-004 Reference Table 1 and 2** (30 May 2020) | G6 has 50 % outside air and remote HEPA but **no air-change rate**; §4.173 points at this table. | The missing tables. |

## 0.3 Guideline rows still blocked

| Document | What is missing |
|---|---|
| **ASHRAE 170**, edition named | Table 7-1 critical-care row: pressure relationship, min outdoor ACH, min total ACH, all-air-exhausted, room-unit recirculation, RH, temperature. **Plus §6.4** for filter-bank topology and affected airstream |
| **FGI 2022**, §2.2-2.6.2.2 | the adult critical-care room-area clause. The "Major Additions and Revisions" extract is not the guideline, and a 2018 value must not be carried into 2022 |
| **AS 1668.2:2024** or **2012** | the healthcare/ICU entry. AusHFG Part E does **not** close this — Part E is a general services overview, retired in 2018 |
| **SP 7:2016 NBC India, Part 8 §3** | the normative ICU rows and notes |
| **NABH 6th ed., Jan 2025** | the complete relevant clauses. One COP.9 excerpt cannot prove HVAC values are absent throughout the edition |
| **DIN 1946-4:2018-09** + A1:2025-11 | Table 1, the intensive-care room class and its requirements. Only the 2008 edition is held, as history |
| **NF S 90-351**, edition named | the AFNOR normative filtration/air-treatment clauses. Secondary material is inadmissible |
| **CSA Z317.2 / Z8000**, editions named | ICU ventilation row; adult critical-care room area |
| **ISO 8996**, edition named | the activity table. Persily's activity examples must not be relabelled as ISO 8996 |

## 0.4 Filter — all of Tier 2 depends on this

The guidelines give **descriptors**, never curves: EPA10, SUP1, F7, "99 % down to
5 µm", "fine filters", remote HEPA. SUP1 is a supply-air designation, not a
product efficiency.

| Gap | What closes it |
|---|---|
| Fractional efficiency `η(dp)` | manufacturer curves at the project duty point |
| Clean ΔP and loading curve | manufacturer data at rated flow, plus dust-holding capacity |
| Airstream topology | ASHRAE §6.4 — which bank sits where relative to the recirculation path |

Constraints: **MERV E1/E2/E3 are reporting bands, not particle-state bins.** A
lower project face velocity does **not** by itself establish an efficiency or a
pressure drop — product data at the operating point is required.

## 0.5 Pollutant state

| Gap | Consequence while open |
|---|---|
| **ICU PM size distribution** `dM/dlogDp` | PM₂.₅ and PM₁₀ are mass metrics. No size-resolved filtration or deposition can touch PM. Kim's Andersen bins cover **viable aerosols only** and do not close this |
| **Deposition `k_dep`** | blocked under the no-proxy rule. Needs a directly applicable formulation **plus** this room's S/V ratio, surface conditions, airflow regime and a compatible size distribution |
| **TVOC** | no verified ICU concentration of any kind |
| **ICU allowable limits** | "how much must we reduce" has no target. Blocked *in the inspected evidence* — not a claim that none exists |

## 0.6 Temporal — Stage C

| Gap | What closes it |
|---|---|
| ICU SOP / IPC event schedule | hospital document with unit, number, revision, effective date, section, approval status. A generic schedule cannot substitute |
| Measured ICU CO₂ trace | trace **and** sensor metadata, outdoor CO₂, time-resolved outdoor airflow, and the exhaust path, all over the same intervals |
| Headcount mapping | heterogeneous source-rate information. Without it the inversion yields **equivalent occupants**, not people |
| Bacteria/fungi temporal route | direct pollutant-specific ICU evidence. The CO₂ shape must not be transferred |

## 0.7 Energy

| Gap | Consequence while open |
|---|---|
| System ΔP per duty point and loading state | no absolute fan power |
| Fan, motor and drive efficiency maps | **fan mechanical efficiency and motor IE class are different quantities** and cannot be combined |
| Chiller performance vs load and outdoor state | ECBC code minima are a compliance baseline, not plant performance |
| Coil, dehumidification and reheat configuration | reheat penalty invisible; it falls hardest on the 10–12 ACH rows |
| ICU sensible and latent loads | zero-load and high-load are **test cases**, not sourced inputs |

## 0.8 Capability gating

Input-level fail-closed is not enough: a capability can be unsafe even when each
number exists, because the *combination* is unsupported. `src/icu/capabilities.py`
disables whole classes of result and names the unmet prerequisites. It cannot be
bypassed by supplying a substitute — **no blocked quantity receives a default
value.**

| Capability | State | Gated on |
|---|---|---|
| Patient-inclusive CO₂ prediction | **DISABLED** | ventilator/circuit configuration; actual room T and P |
| Headcount from CO₂ inversion | **DISABLED** | observed composition; exhaust path |
| Tier 2 size-resolved filtration | **DISABLED** | ICU PM size distribution; §6.4 airstream |
| Deposition modelling | **DISABLED** | `k_dep` under the no-proxy rule; PM size distribution |
| Stage C responsive control | **DISABLED** | occupancy schedule; observed composition |
| Absolute energy | **DISABLED** | system ΔP; fan/motor/drive efficiency |
| Activity-based PM prediction | **DISABLED** | SOP timing; PM size distribution; `k_dep`. A **declared sensitivity scenario** is available instead |
| PM source inversion from a trace | **DISABLED** | `k_dep`; PM size distribution; filter penetration. PM has sinks, so outdoor airflow alone is not enough |

Still available: the guideline register, minimum outdoor-air arithmetic from
accepted provisions, **equivalent occupants** (explicitly not a headcount), and
relative fan power as conditional arithmetic on an assumed identical system
curve.

**Consequently withdrawn:** the patient-inclusive CO₂ figures of 356 / 505 / 514
/ 1356 ppm reported earlier. They remain withdrawn until gaps 1 and 3 close.

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


## 4. Guideline scenarios

One row per document. Not reconciled, not averaged. Revised 2026-08-30.

| # | Document, locator | Total ACH | Outdoor air | Filter descriptor | Pressure | T | RH |
|---|---|---|---|---|---|---|---|
| G1 | ASHRAE 170-2025, Table 7-1 + §6.4 | **BLOCKED — not in evidence** | | | | | |
| G2 | HTM 03-01 Part A 2021, Table 3, p64 | ≥10 ac/h | §8.6: ≥10 L/s·person, and ≥20 % if recirculating, **whichever is greater** | EPA10 final | +5 Pa | 20–25 °C | floating, max 60 % |
| G3 | HTM 03-01 Part A 2021, App 2, p147 | 10 ac/h | as G2 (same document) | SUP1 supply designation | +10 Pa | not stated | not stated |
| G4 | SHTM 03-01 v2 2014 (ARCHIVED), App 1 Table A1, p139 | 10 ac/h | §2.37: 20 % if recirculating (**no person term**) | F7 supply | +10 Pa | 18–25 °C | not stated |
| G5 | ISCCM 2020, Environmental Requirements | 6 min | 2 ACH | 99 % down to 5 µm | clean→less-clean; no numerical value | 16–25 °C | not stated |
| G6 | VHHSBA HTG-2020-004 §4.172 p34 | not in clause | `f_OA = 0.50` | remote HEPA outside the ICU | positive | not in clause | not in clause |
| G7 | AusHFG RDS 1BR-ICU Rev 2, p1 | not stated | not stated | **not selected in this room data sheet** | **not selected in this room data sheet** | not stated | not stated |
| G8 | NABH 6th ed., COP.9 excerpt | **BLOCKED — one excerpt cannot prove absence** | | | | | |
| G9 | **MoHFW India, March 2022**, p24; Annexure III p47 | **10–12 ac/h** | **4–5 fresh-air ACH** | AHU with "fine filters" | positive | 23 ± 2 °C | 45–65 % |

**G7 wording matters.** The unticked checkboxes show only that *this room data
sheet* does not select those services. They do **not** establish that no other
AusHFG document requires them.

**G2 and G3 are the same document.** Their difference on pressure and filter
descriptor is recorded as an **unreconciled difference between two rows**, not
as proven internal inconsistency.

### 4.1 Constrained versus free control parameters

| # | Total ACH | Outdoor air | Filter | Pressure | T | RH |
|---|---|---|---|---|---|---|
| G2 | ≥10 | **bounded below**, occupancy-dependent | EPA10 | +5 Pa | 20–25 | ≤60 |
| G3 | 10 | **bounded below** (same document) | SUP1 | +10 Pa | free | free |
| G4 | 10 | **bounded below** at 20 %, occupancy-independent | F7 | +10 Pa | 18–25 | free |
| G5 | 6 | 2 ACH | 99 %@5 µm | free | 16–25 | free |
| G6 | free | **= 0.50** | remote HEPA | positive | free | free |
| G9 | 10–12 | 4–5 ACH | "fine filters" | positive | 23 ± 2 | 45–65 |

No guideline in evidence specifies UVGI or any air-disinfection requirement,
scoped to the rows held.

## 5. Room temperature and relative humidity

These are **room/space design conditions**. No source in evidence gives a
supply-air temperature, humidity ratio, dew point or relative humidity for ICU;
supply state must be derived from room balances or declared as a separately
sourced boundary, never labelled a guideline requirement.

| Source | Temperature | RH |
|---|---|---|
| HTM 03-01:2021 Table 3 | 20–25 °C | floating, max 60 % |
| HTM 03-01:2021 Appendix 2 | not stated in this row | not stated |
| SHTM 03-01:2014 Table A1 (archived) | 18–25 °C | not stated |
| ISCCM 2020 | 16–25 °C, enclosed patient modules | not stated |
| **MoHFW India, March 2022** | **23 ± 2 °C** | **45–65 %** |
| AusHFG RDS 1BR-ICU | not stated | not stated |
| ASHRAE 170-2025 | **BLOCKED** | **BLOCKED** |

**The earlier "21–24 °C common window" is withdrawn.** It was the intersection
of four bands, one of which was the now-blocked ASHRAE row. Recomputing without
it gives 20–25 ∩ 18–25 ∩ 16–25 ∩ 21–25 = **21–25 °C**, but this remains a
*researcher-selected* common interval, not a requirement stated by any source.

RH is bounded by two sources that **disagree in kind**: HTM caps at 60 % with no
lower bound, while MoHFW requires 45–65 %. Their upper limits conflict — 65 %
exceeds HTM's 60 % maximum. They must not be reconciled.

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
flows and ppm at actual room conditions. **The actual ICU room temperature and
pressure are BLOCKED**, so the model evaluates at a **researcher-selected**
297.15 K / 101325 Pa. The resulting shift of roughly +8.5 to +8.8 % relative to
the source reference states is **researcher-defined arithmetic and must never be
presented as source data**. Prefer the molar route (`to_molar()`) until the room
state is measured.

### 7.2 Identifiability

The single-bed room fixes the patient count, so the patient term can be
subtracted:

    S_non-patient(t) = S_total(t) − S_patient

That is a **source strength**, not a headcount. Dividing by one reference rate
yields **"equivalent occupants"**, valid only if every non-patient shares that
rate — which Persily shows they do not. Label results accordingly.

Patient VCO₂ is a room source **only if** the ventilator discharges to room air
(§0.1, gap 1).

## 8. Deposition `k_dep` — BLOCKED

Reclassified 2026-08-30. Previously recorded as "not blocked, generic aerosol
literature applies". Under the project's no-proxy rule that is not admissible:
generic non-ICU aerosol literature cannot be inserted as an ICU-room input
merely because deposition is a general physical process.

Closing it requires a directly applicable deposition formulation **plus** the
actual room surface-to-volume ratio, surface and material conditions, the
airflow and turbulence regime, and a compatible particle-size distribution —
which is itself blocked (§0.4).

## 9. Energy reference values

| Quantity | Value | Source | Class |
|---|---|---|---|
| Air-cooled chiller COP, <260 kWr | 2.8 (IPLV 3.5) | ECBC 2017 §9.4.2.8 Table 9-5 | code minimum for the **standard design**, not plant performance |
| Air-cooled chiller COP, ≥260 kWr | 3.0 (IPLV 3.7) | ECBC 2017 §9.4.2.8 Table 9-5 | as above |
| Fan efficiency | **BLOCKED** | — | see below |

**Correction 2026-08-30.** The earlier row "65 % (IE3) / 70 % (IE4) / 75 % (IE4)"
conflated two different quantities: **fan mechanical efficiency and motor IE
efficiency class are not interchangeable** and cannot be combined into a single
number. The official ECSBC 2024 tables must be read directly for the
mechanical-efficiency requirement, and actual fan, motor and drive efficiency
must come from selected equipment or measured plant data.

Blocked for absolute energy: system pressure drop at each duty point and
loading state; fan, motor and drive efficiency maps; chiller performance versus
load and outdoor state; coil, dehumidification and reheat configuration; ICU
sensible and latent loads; hourly outdoor files per city.

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

### 11.2 Source-specific measurements

The earlier clean / moderate / India-high / event-tail table is **withdrawn**:
those were analyst-created categories, not classifications stated by the cited
studies, and several entries were misattributed. Only source-specific
observations are retained, each with its study scope.

| Study | Directly reported | Scope |
|---|---|---|
| Kim, Kim & Kim, *Ind Health* 48(2):236–243 (2010), Tables 2–3 | ICU bacteria **202** CFU/m³ total, **142** respirable; fungi **65** total, **47** respirable | five Seoul hospitals; six-stage Andersen; 28.3 L/min |
| Lokeshwari, Balajee & Premalatha, *IJCMAS* 9(9):2376–2389 (2020), Table 1 p2383; Table 2 p2384 | grouped ICU bacteria **93.85 ± 31.57** CFU/m³; grouped ICU fungi **2.62** CFU/m³ | Chennai quaternary care; ICU group = MICU/PICU/SICU/NICU/LMICU/CCU |
| Tang, Chung, Lin & Wan, *AJIC* 37:183–188 (2009), Results p184 | **21.2–25.8 °C**, **58–74 % RH**, **828–1570 ppm CO₂**, **4.2–43.7 µg/m³ PM₁₀** | four-bed medical ICU, northern Taiwan; weekly sampling around visiting |

### 11.3 Specific withdrawals

| Withdrawn entry | Reason |
|---|---|
| CO₂ 1822–2258 ppm "(Aligarh)" | attributed to Taushiba et al. (2023), which **did not measure CO₂** and was conducted in **Lucknow** |
| PM₂.₅ 20–35 and PM₁₀ 10–60 µg/m³ "(Tang)" | Tang reports PM₁₀ **4.2–43.7** µg/m³ and defines fine particles as **PM₂ (<2 µm), not PM₂.₅** |
| Bacteria 94–151 CFU/m³ as an Indian ICU range | the grouped ICU result is **93.85 ± 31.57**; the 151 value belongs to a separate **PICU isolation-room** category |
| Bacteria/fungi >1000 to ~7236 / ~11654 as "event tails" | month- and study-specific observations, not a validated event-tail distribution. Tang's before/after values are **plotted**; digitising them is not sourcing them |
| TVOC concentration | **BLOCKED** — no verified ICU source |
| Any ICU allowable limit | **BLOCKED** in the inspected evidence. This is not a claim that none exists anywhere |

### 11.4 Note on Tang's temperature and RH

Tang's 21.2–25.8 °C and 58–74 % RH are **measured room conditions in one
Taiwanese ICU**, not a requirement and not this project's setpoint. The upper RH
exceeds the 60 % maximum that HTM 03-01:2021 Table 3 states for critical care.

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

| A5 | **MODEL HYPOTHESIS, requires site validation.** Exhaust is taken off the return immediately before the duct inlet and is exactly balanced against outdoor air. `Q_exhaust = Q_OA`, so `Q_recirc = Q_s − Q_OA`. With no infiltration, room outflow equals `Q_s` and the room's outdoor-air exchange equals `Q_OA`. |
| A6 | **MODEL HYPOTHESIS, requires site validation.** Return concentration equals room concentration (perfect mixing at the return). |
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

- **Tier 1 — the least blocked tier, but not unblocked.** Room mass balance, ventilation,
  `f_OA` sweep, CO₂, fan energy and outdoor-air conditioning energy at
  code-referenced efficiency. This alone answers, for every guideline, what CO₂
  it delivers and at what ventilation energy — a complete Stage A result.
- **Tier 2 — needs generic, obtainable data.** `k_dep`, size-resolved PM and
  viable transport, filter efficiency curves.
- **Tier 3 — needs site or equipment data, Stage C only.** Occupancy schedule,
  measured fan/chiller performance, ICU thermal loads.

Stage A and Stage B are not blocked *by the occupancy schedule specifically*,
because every guideline sees the same occupancy. They are, however, blocked from
being reported as complete: CO₂ still depends on the ventilator exhaust path,
occupant composition and the actual room gas state, and energy on plant data.
"Tier 1 with nothing blocked" was an overstatement and is withdrawn.

---

## 14. Concentration model

### 14.1 State vector

**PM₂.₅ and PM₁₀ are not state variables.** Filter penetration is
size-dependent, so a mass metric cannot be penetrated. The state is carried in
size bins; the metrics are **integrals over those bins at reporting time**. A
bin is included only if it lies wholly at or below the cutoff — apportioning a
partial bin needs the within-bin distribution, which is part of the blocked
size-distribution evidence.

| Species | State | Filter | Deposition | UVGI | Dilution |
|---|---|---|---|---|---|
| CO₂ | scalar, ppm | no | no | no | **yes — the only lever** |
| TVOC | scalar | no | no | no | **yes — the only lever** |
| PM | size bins → PM₂.₅/PM₁₀ as outputs | yes | yes | no | yes |
| Bacteria | 6 Kim Andersen bins | yes | yes | **yes** | yes |
| Fungi | 6 Kim Andersen bins | yes | yes | **yes** | yes |

### 14.2 The balance, with the filter on mixed air

The main bank sits downstream of the mixing point, so it treats the whole
supply — **researcher-defined system topology**; ASHRAE §6.4 is still not held
and this must not be cited as an ASHRAE requirement. Then

    C_supply,i = P_i · Z_i · [ f_OA·C_out,i + (1 − f_OA)·C_room,i ]

Substituting into the room balance and collecting gives `dC/dt = A − B·C`:

    A_i = [ S_i + Q_s·P_i·Z_i·f_OA·C_out,i ] / V
    B_i = (Q_s/V)·(1 − P_i·Z_i·(1 − f_OA)) + k_dep,i

`P_i` is filter penetration and `Z_i` in-duct UV survival, both single-pass
fractions where 1.0 removes nothing. The exact recurrence applies unchanged per
species, so master D10 is preserved.

**Two structural consequences.**

*The form reduces exactly to the CO₂ case.* With `P = Z = 1` and `k_dep = 0`,
`B` collapses to `Q_OA/V` — verified to machine precision in the test suite.
That is why recirculation cannot touch CO₂ or TVOC, and why `f_OA` is their only
lever.

*In-duct UV is mathematically a filter on the viable bins.* `P` and `Z` enter as
a product, so a lamp is indistinguishable from a better filter acting on the
same bins. It is **not** a room removal term, and no equivalent-ACH credit is
taken. `P = 0.5, Z = 0.4` and `P = 0.2, Z = 1.0` give identical coefficients —
also tested.

At 10 ACH and `f_OA = 0.2`, single-pass removal maps to effective removal as:

| `P·Z` | `B` (1/h) |
|---|---|
| 1.0 (nothing removed) | 2.00 |
| 0.5 | 6.00 |
| 0.0 (perfect) | 10.00 |

The floor is the outdoor-air rate; the ceiling is the full supply rate.

### 14.3 Temporal drivers — what each species needs

The CO₂ temporal shape is **not** transferable to other species. Each needs its
own evidenced route.

| Species | Temporal driver | State |
|---|---|---|
| CO₂ | occupancy, via inversion (§14.4) or schedule | both routes **blocked** |
| TVOC | unknown; no ICU concentration of any kind | **blocked** |
| PM | `C_out,i(t)` from the climate files **plus** indoor sources and resuspension | outdoor part opens when the files arrive; indoor part **blocked** |
| Bacteria, fungi | no sourced route. Occupancy shaping is not evidenced, and magnitude calibration does not supply a profile | **blocked** |

**The only temporal driver currently reachable is outdoor climate, for PM.**
Every indoor driver is blocked. Until they close, runs are **declared
steady-state scenarios**, not a diurnal profile.

### 14.4 Activity-based PM emission

Occupants do emit PM through daily activity — bed making, washing, cleaning,
walking, rounds, visitor entry, dressing changes. The model supports this, in
**two modes that are kept strictly apart**, following the rule already set for
staff demographics: a researcher declaration yields a labelled sensitivity
scenario, not representative ICU data.

| Mode | Requires | Produces |
|---|---|---|
| **PREDICTION** | an ICU source locator on **every** emission factor, and SOP timing on every activity | a result about an ICU. **Currently unreachable** |
| **SENSITIVITY** | declared factors, SOP timing still required | a **labelled sensitivity scenario** — explicitly not an ICU prediction |

Enforcement, tested rather than documented: a `SOURCED` factor without a locator
is rejected at construction; prediction mode refuses a `DECLARED` factor and
refuses an activity with no factor at all, since zero-by-default is itself an
assumption; a factor whose bin count differs from the state is **refused, not
re-binned**, because re-binning a measured distribution needs the original
channel boundaries.

#### Why PM cannot be inverted the way CO₂ can

This shapes the acquisition order and is worth stating plainly.

CO₂ has **no sinks** in this system — no filter, no deposition, no UV — so its
balance contains only `Q_OA`, and a measured trace inverts to a source with
outdoor airflow alone.

PM has sinks. Its balance carries `P` and `k_dep` as well as `f_OA` and
`C_out(t)`. **A measured ICU PM trace therefore cannot be inverted into a source
until deposition and filter penetration are known.** Getting a PM time series
does not, by itself, unlock a PM source model the way a CO₂ trace unlocks
occupancy.

#### What would close prediction mode

For each activity and species: emission rate **per size bin**, the instrument
and its channel boundaries, sampling duration, the ICU's ventilation state
during measurement, and the activity definition used. Plus SOP timing, plus
`k_dep` and the bin structure to express any of it in.

### 14.4 Two routes to occupancy, when it opens



Occupancy `N(t)` carries the time variation; sources follow from it.

#### Routes

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

#### Propagation

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

#### Remaining limits

Route A is blocked on the SOP. Route B needs a measured ICU CO₂ trace *with its
ventilation conditions* — Tier A source-reconstruction studies qualify, Tier B
studies with incomplete HVAC metadata give shape but not magnitude. Until one of
those arrives the machinery is built and tested but unfed, and Stage A proceeds
on the steady-state occupancy levels of §1 instead.


---

---

# PART IV — RESULTS

## 15. Stage A status after the 2026-08-30 audit

`scripts/run_stage_a.py`; 26 tests pass.

### 15.1 Scenario admissibility

| | Document | Status |
|---|---|---|
| G1 | ASHRAE 170-2025 | **BLOCKED** — only Addendum h to 170-2021 in evidence |
| G2 | HTM 03-01 Part A 2021, Table 3 | usable, 10 ACH |
| G3 | HTM 03-01 Part A 2021, Appendix 2 | usable, 10 ACH |
| G4 | SHTM 03-01 v2 2014 (archived) | usable, 10 ACH |
| G5 | ISCCM 2020 | usable, 6 ACH / 2 OA |
| G6 | Victoria HTG-2020-004 | no rate stated; Reference Table 1/2 required |
| G7 | AusHFG RDS 1BR-ICU | no rate; services **not selected in this sheet** |
| G8 | NABH 6th ed. | **BLOCKED** — one excerpt cannot prove absence |
| G9 | **MoHFW India, March 2022** | usable, 10–12 ACH / 4–5 OA |

### 15.2 Corrected UK minimum outdoor air

ACCEPTED provisions, DERIVED arithmetic at `Q_supply = 750 m³/h`:

| Occupants | G2 (HTM, 20 % **or** 10 L/s·person) | G4 (SHTM, 20 % only) |
|---|---|---|
| 3 | 150 m³/h · 2.00 ACH · f_OA 0.200 | 150 m³/h · 0.200 |
| 5 | **180 m³/h · 2.40 ACH · 0.240** | 150 m³/h · 0.200 |
| 11 | **396 m³/h · 5.28 ACH · 0.528** | 150 m³/h · 0.200 |

### 15.3 CO₂ excess at the controlling minimum outdoor air

DERIVED, at a **researcher-selected** evaluation state (§7.1); the actual ICU
room state is blocked, so these are not source-backed concentrations.

| N | G2 (HTM) | G4 (SHTM) | G5 (ISCCM) | G9 (India 2022) |
|---|---|---|---|---|
| 3 | 356 | 356 | 356 | **178** |
| 5 | **505** | 606 | 606 | **303** |
| 11 | **514** | 1356 | 1356 | **678** |

## 16. Findings, and what was withdrawn

**16.1 A person-based fresh-air rule protects at high occupancy; a
fraction-only rule does not.** At 11 occupants G2 holds 514 ppm because
10 L/s·person forces 396 m³/h, while G4's 20 %-only rule stays at 150 m³/h and
reaches 1356 ppm — from the same 10 ACH supply. This replaces the withdrawn
finding and rests entirely on ACCEPTED provisions.

**16.2 The Indian national guideline is the most demanding on fresh air.**
G9's 4–5 outdoor ACH gives the lowest CO₂ of every usable scenario at every
occupancy.

**16.3 Guidelines specify filtration in incommensurable descriptors** — EPA10,
SUP1, F7, "99 % down to 5 µm", "fine filters", remote HEPA. None is a
fractional-efficiency curve. SUP1 is a supply-air designation, not a product
efficiency.

**16.4 HTM Table 3 and Appendix 2 differ** on pressure (+5 vs +10 Pa) and filter
descriptor (EPA10 vs SUP1). Recorded as an **unreconciled difference between two
rows**, not as proven internal inconsistency.

### 16.5 Withdrawn

| Withdrawn | Why |
|---|---|
| "UK outdoor air is undefined and could approach zero" | HTM §8.6 bounds it. The 5 % and 10 % sweep points are **noncompliant**, not design options |
| All G1 / ASHRAE 170-2025 values and anything derived from them | the 2025 row was never in evidence |
| **4.63× fan power** and **5× outdoor-air conditioning** as findings | the first is conditional on an identical system curve and unchanged efficiency; the second used the invalid unbounded-UK treatment. Retained only as clearly labelled conditional arithmetic |
| Response times (t95) | depended on the invalid UK outdoor-air treatment |
| "Four of eight guidelines are incomplete" | G1 and G8 are *blocked*, not known; not every named edition has been checked |
| The clean / moderate / India-high / event-tail regime table | analyst-created categories with several misattributions (§11) |

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
