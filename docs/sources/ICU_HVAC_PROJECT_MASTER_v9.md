# ICU HVAC PhD Project — Master Research State

**Project owner:** Harshvardhan  
**Master file purpose:** Single restart point for the complete ICU HVAC research programme.  
**Update protocol:** Append a dated update after every substantive project discussion/model change. Never silently overwrite a locked decision; supersede it explicitly in the update log.  
**Current master update:** **Update 10 — 2026-08-16**  
**Status:** Active model development.

---

# 0. Core research objective

Develop and later experimentally validate a **climate- and location-specific ICU ventilation optimisation framework** that determines the most energy-efficient HVAC design/control strategy capable of maintaining acceptable ICU air quality.

The study is built around measured/literature-supported ICU concentrations of:

- CO₂
- PM₂.₅
- PM₁₀
- viable bacteria
- viable fungi

and ventilation/treatment variables:

- ACH
- outdoor-air/fresh-air fraction (FOA)
- filtration
- room pressure
- temperature
- relative humidity
- UVGI **for viable aerosols only**

The study must distinguish:

1. **what each guideline actually requires;**
2. **what air quality and energy use that requirement actually delivers;**
3. **the best solution still constrained by that guideline;**
4. **the project’s own adaptive climate/location-specific optimum.**

The proposed optimum is not simply a larger ACH/filter. It should use:

- room geometry and occupancy-dependent airflow,
- concentration-responsive / peak-following FOA,
- outdoor pollution and climate-aware OA filtration,
- indoor-source-aware recirculation filtration,
- UVGI only when viable aerosols warrant it,
- filter loading/age/pressure-drop physics,
- reliability/uncertainty rather than deterministic pass/fail alone.

---

# 1. Research story / motivation

## 1.1 ICU pollutant concentrations are not universal

The literature evidence assembled in `ICU_CONCENTRATION_EVIDENCE_DATABASE.xlsx` shows large differences among ICUs by ventilation condition, location, climate, activity, occupancy, season and measurement method.

Current evidence-supported regimes include approximately:

| Pollutant | Clean / low-load ICU | Moderate / stressed | India / high-load | Event tail |
|---|---:|---:|---:|---:|
| CO₂ | ~450–800 ppm | 828–1570 ppm (Tang medical ICU) | ~1822–2258 ppm means in Aligarh study | occupancy/visitation peaks |
| PM₂.₅ | ~1–5 µg/m³ | ~20–35 µg/m³ | ~50–98 µg/m³ | activity/cleaning peaks |
| PM₁₀ | ~0.9–10 µg/m³ | ~10–60 µg/m³ | ~57–118 µg/m³ | instantaneous peaks can be much higher |
| Bacteria | ~70–250 CFU/m³ | ~250–450 CFU/m³ | Indian active-sampler means broadly ~94–151 CFU/m³ | >1000 to ~7236 CFU/m³ in Tang |
| Fungi | ~2.6–70 CFU/m³ | — | Indian active-sampler means low single digits in current Chennai evidence | >1000 to ~11654 CFU/m³ in Tang |

These are **validation regimes, not regulatory limits and not source inputs**.

## 1.2 India-specific HVAC problem

The national Indian hospital evidence already assembled indicates substantially lower HVAC penetration in public hospitals and a large share of DX-type systems that do not inherently provide the outdoor-air, filtration-bank and pressure-control architecture assumed by many ICU standards.

Important correction to wording:

- Strong evidence exists for lower HVAC penetration in public hospitals.
- The current evidence does **not** justify a blanket claim that private Indian ICUs are fully compliant.
- ICU-level environmental compliance auditing remains a literature gap.

## 1.3 ICU energy benchmarking problem

Indian national hospital EPI is whole-hospital energy divided by gross floor area and is not an ICU-specific benchmark. A compliant 24/7 ICU with high airflow, OA conditioning, filtration and pressure control can legitimately have a much higher energy intensity.

A potential research output is therefore an **ICU-specific compliance-linked energy benchmark/range**, clearly labelled as study-derived unless a national benchmark is found.

---

# 2. Locked study structure

## Stage A — Guideline evaluation

For each guideline:

- use its own ACH/OA requirement,
- use its own filter requirement/topology,
- use its own pressure requirement,
- use its own T/RH requirement,
- do **not** add beneficial components that the guideline does not provide credit for,
- simulate pollutant reduction, energy consumption and reliability.

Question answered:

> If this guideline is applied as written, what air quality does it actually deliver under realistic ICU conditions, and at what energy cost?

## Stage B — Guideline-constrained optimisation

Optimise only inside that guideline’s allowable ranges/configurations.

This result is:

> the best operating/design point available **within the guideline**, not the project recommendation.

## Stage C — Project recommendation / original optimisation

Allow:

- ACH linked to geometry/occupancy,
- concentration-responsive FOA,
- outdoor pollution-aware OA filter selection,
- recirculation filter selection based on indoor source/size distribution,
- UVGI only for viable particles,
- UVGI configuration from the existing UVGI model,
- filter ageing/loading/service interval,
- climate/location dependence,
- reliability constraints.

---

# 3. Locked modelling decisions

| ID | Decision |
|---|---|
| D1 | T and RH affect the **energy model**. Direct T/RH dependence of filter capture, deposition, microbial survival and UV susceptibility is outside the current contaminant-physics scope unless explicitly reopened later. |
| D2 | FOA is fixed during guideline evaluation/optimisation; concentration-responsive/peak-following in the project’s own optimisation. |
| D3 | External literature/web research is allowed. Numerical model inputs need traceable citations/evidence status. |
| D4 | Carry **single-bed and multi-bed/open ICU** scenarios in parallel. Never average them before reporting. |
| D5 | OA-branch filter is guideline-dependent during guideline stages. If a guideline is silent, no OA-branch-filter credit is given. In the original optimisation it becomes a design variable. |
| D6 | No rig data yet. Literature validation is sufficient for current development; experimental validation comes later. |
| D7 | Generation validation is against **distributions/regimes** of measured ICU concentrations, not one anchor value. |
| D8 | UVGI model already exists and will **not** be rebuilt. It is connected later through an adapter/operator. |
| D9 | UVGI acts only on viable aerosol bins; it does not remove CO₂ or non-viable PM mass. |
| D10 | Preserve the existing exact exponential well-mixed recurrence rather than using Euler stepping. |
| D11 | Size-resolve PM and viable aerosols instead of representative single diameters. |
| D12 | Optimisation may remain exhaustive enumeration if the discrete design space is tractable; the optimiser itself is not the claimed novelty. |

---

# 4. ICU geometry and physical rig

## Numerical ICU

Two scenarios:

1. single-bed ICU room;
2. multi-bed/open ICU.

Geometry is parameterised by:

- bed count,
- area/bed or explicit room dimensions,
- ceiling height,
- occupied beds,
- staff/visitor activity.

Verified single-bed reference geometry and occupancy:

- **Australasian Health Facility Guidelines, Room Data Sheet, 1 Bed Room - Intensive Care, Room Code 1BR-ICU**, issue date 12.11.2025, Revision 2, page 1.
- briefed area: **25.00 m²**;
- ceiling height: **3.0 m**;
- gross geometric volume: **75.0 m³**, derived exactly as area × ceiling height;
- listed occupancy: 1 patient, 1-2 visitors and 1-2 staff, with 4-6 additional staff as required;
- base listed total: 3-5 occupants; maximum listed total with additional staff: 11.

The source does not use the word `steady`, and 75.0 m³ is a derived gross geometric volume, not a measured effective well-mixed air volume. Do not invent a displacement correction for furnishings or equipment.

Airflow follows:

\[
Q = ACH\,V
\]

and not one fixed laboratory flow rate.

## Physical duct

Existing rig:

- cross-section: **0.3048 m × 0.3048 m**
- total length: **6 m**
- inlet/mixing section
- filter section
- treatment/outlet section
- recirculated air + outdoor-air intake concept

The rig validates component physics at matched face velocity/residence-time conditions. It is not required to carry the full volumetric airflow of a large multi-bed ICU.

---

# 5. Guideline state

Primary/current evidence already established includes the following.

Mandatory comparison citation rule, locked 2026-08-29:

- Every pasted guideline requirement must repeat the **full document title**, **exact edition/year or dated revision**, and **table/section number plus named row or space** before listing values.
- `Same as above`, an undated standard number, or a country-only label is not an acceptable comparison citation.
- If the edition or locator is unavailable, the cell remains pending and the missing edition/table/section is named explicitly.

## ASHRAE 170-2025 — critical care patient care station

User-supplied Table 7-1 directly verifies:

- pressure: N/R
- minimum OA: **2 ACH**
- minimum total: **6 ACH**
- room-unit recirculation: No
- unoccupied turndown: Yes
- minimum filter efficiency: **MERV-14**
- RH: **30–60%**
- temperature: **21–24°C**

Important limitation:

- Table 7-1 closes the current room row.
- Detailed 2025 §6.4 filter-bank topology remains unverified.
- Do not silently relabel the separately verified 2021 two-bank/mixed-air clause as unchanged in 2025.

Archive verification, 2026-08-29:

- `170_2021_h_20220930 (1).pdf` is **ANSI/ASHRAE/ASHE Addendum h to ANSI/ASHRAE/ASHE Standard 170-2021**, approved September 2022.
- Addendum h revises Sections 8.1 and 8.2 and Tables 8-1 and 8-2 for specialised outpatient and residential spaces.
- It does **not** contain or revise the inpatient critical-care row in Table 7-1 and does not provide the requested §6.4/filter-bank requirements.
- It therefore cannot be used to validate or replace the separately verified 170-2025 Table 7-1 critical-care row.

## Australia / New Zealand

The uploaded archive does not contain AusHFG Part E or AS 1668.2:2012/2024. The requested Australia/NZ comparison row therefore remains blocked.

The archive does contain a separate Victorian primary guideline:

- **Engineering guidelines for healthcare facilities: Volume 4 - Heating, ventilation and air conditioning**, Health technical guideline **HTG-2020-004**, Victorian Health and Human Services Building Authority, May 2020.
- Section **4.172, ICU and CCU**, printed page 34, specifies remote HEPA filtration outside the ICU, 50% outside air to patient areas, and positive air movement from beds toward adjoining circulation space.
- Section 4.173 refers to `Reference table 1` for remaining conditions, but that table is not present in the supplied PDF.

These Victorian provisions are retained as **supplemental jurisdiction-specific primary evidence only**. They must not be substituted for the requested AusHFG Part E or AS 1668.2 entry.

The AusHFG room-data sheet must not be cited as a HEPA requirement. On page 1, only `AIRCONDITIONING: general` is selected. The checkboxes for HEPA filtered, positive pressure, negative pressure, exhaust, supply and natural ventilation are unselected. The direct HEPA requirement presently available is the separate Victorian HTG-2020-004 §4.172 remote-AHU provision.

## ACH and outdoor-air fraction interpretation

At the verified gross room volume of 75.0 m³:

- 6 h⁻¹ gives 450 m³/h total airflow;
- 10 h⁻¹ gives 750 m³/h total airflow.

For outdoor-air and total ACH defined on the same room-volume basis:

\[
f_{OA}=\frac{Q_{OA}}{Q_{total}}=\frac{ACH_{OA}}{ACH_{total}}.
\]

Therefore the ASHRAE 170-2025 and ISCCM 2020 minimum pair of 2 outdoor ACH and 6 total ACH implies a minimum outdoor-air fraction of 1/3 only when operating at exactly 6 total ACH. More generally, if the 2 outdoor ACH minimum is retained while total ACH is changed, the mathematical minimum is `2/ACH_total`.

Applicability is locked as follows:

- ASHRAE/ISCCM at 6 total ACH: FOA below 33.3% fails the 2 outdoor ACH minimum.
- A 20% FOA at 10 total ACH satisfies 2 outdoor ACH only in an ASHRAE/ISCCM parametric case where total ACH has been increased to 10. It is not a UK requirement.
- HTM 03-01:2021 Table 3/Appendix 2 and archived SHTM 03-01:2014 Table A1 provide no outdoor-air value in their critical-care rows. Their FOA is undefined by those rows; do not import the ASHRAE/ISCCM 2 ACH floor.
- Victorian HTG-2020-004 §4.172 specifies 50% outdoor air for its own ICU/CCU scenario.
- A 20-100% FOA sweep is a project sensitivity/design-variable range, not a cross-guideline requirement. Each point must retain its source-specific compliance label.

## Filter requirement interpretation

- ASHRAE 170-2025 Table 7-1 gives MERV-14, but current §6.4 topology remains required before assigning that filter to a specific full-supply, mixed-air or recirculation path.
- HTM 03-01:2021 Table 3 gives a final BS EN 1822 EPA10 filter.
- HTM 03-01:2021 Appendix 2 gives BS EN 16798 SUP1. Do not convert SUP1 to MERV, EPA or a size-resolved efficiency curve without direct normative mapping.
- Archived SHTM 03-01:2014 Appendix 1 Table A1 gives F7.
- ISCCM 2020 states 99% filtration down to 5 µm; this is not a complete size-resolved filter curve.
- AusHFG Room Data Sheet 1BR-ICU, Revision 2, does not select HEPA filtration.
- Victorian HTG-2020-004 §4.172 separately requires remote HEPA filtration.
- NABH Sixth Edition, January 2025, COP.9 has no numerical filter requirement.

## Room conditions versus supply-air state

The temperature and humidity entries in ASHRAE 170-2025 Table 7-1, HTM 03-01:2021 Table 3, archived SHTM 03-01:2014 Table A1 and the ISCCM 2020 HVAC section are room/space design conditions. None of these verified ICU entries provides a supply-air dry-bulb temperature, supply humidity ratio, supply dew point or supply relative humidity.

The common temperature overlap 21-24°C is mathematically compatible with:

- ASHRAE: 21-24°C;
- HTM: 20-25°C;
- archived SHTM: 18-25°C;
- ISCCM: 16-25°C for enclosed patient modules.

It is a selected common room operating interval, not a requirement stated identically by all four sources.

For humidity:

- ASHRAE specifies 30-60% RH;
- HTM Table 3 specifies floating RH with a maximum of 60%;
- the archived SHTM critical-care row and ISCCM primary HVAC section state no RH range.

Thus 60% is corroborated as an upper limit by ASHRAE and HTM, while the 30% lower limit comes from ASHRAE only.

Supply-state consequences must be derived conditionally from conservation balances, not copied from guideline room bands:

- If supply air alone removes a positive room sensible load, the required supply temperature is below the room temperature. This is not universal when separate sensible cooling or heating is present.
- If supply air removes a positive room latent load, the supply humidity ratio must be below the room humidity ratio. Supply and room relative humidity must not be compared directly because RH depends on temperature.
- With fixed room loads, total supply airflow and room targets, changing FOA changes the mixed-air entering state and coil/dehumidification/reheat duty. It does not by itself require a different final supply state.
- The final supply state changes only if total airflow, room sensible/latent load, infiltration/pressurisation, or the selected system/control constraints also change.

Pinning supply conditions directly is permitted only as an explicitly sourced design or experimental boundary condition. It must not be labelled as a guideline requirement.

## Indian standards/guidelines

The register demonstrates genuine disagreement, including:

- total ACH roughly 6 to 12 depending on document,
- OA approximately 2 ACH to 4–5 ACH depending on document,
- pressure can be equal / positive / negative depending on document.

Do not reconcile them into one “Indian ICU” value. Each document is its own scenario.

Archive verification, 2026-08-29:

- `s13054-020-02907-5.pdf` is Saran et al., **Heating, ventilation and air conditioning (HVAC) in intensive care unit**, *Critical Care* 2020;24:194.
- Its Table 4 is a peer-reviewed **secondary comparison**, not the ISCCM primary consensus statement.
- It corroborates the ISCCM general-ICU summary of 16-25°C, no RH value, 99% filtration efficiency down to 5 µm, and 2 outdoor/6 total ACH. Its Table 4 labels the general ICU `Neutral`, while the primary ISCCM narrative gives airflow from clean to dirty but no numerical general-ICU pressure differential.
- The temperature, filtration and ACH values remain attributable to the directly checked ISCCM 2020 primary consensus. The Saran pressure label is secondary interpretation only and must not be promoted into the primary row.
- The archive contains neither NABH Sixth Edition, January 2025, nor NBC 2016 Part 8 Section 3. Their prior evidence status is unchanged.

## HTM

Primary HTM contains an internal pressure inconsistency:

- Table 3 critical-care values use +5 Pa;
- another summary uses +10 Pa.

Preserve both as sensitivity/scenario values.

Direct archive verification:

- **Health Technical Memorandum 03-01: Specialised ventilation for healthcare premises, Part A**, 2021, Table 3, printed page 64: Level 2 or 3 critical-care individual room/open bays; supply only and cascade out; at least 10 ac/h; +5 Pa to general area; 35 dB(A); 20-25°C; floating RH with maximum 60%; final filter BS EN 1822 EPA10.
- Same document, Appendix 2, printed page 147: critical-care areas; supply ventilation; 10 ac/h; +10 Pa; SUP1; 35 dB(A); temperature not stated; isolation room may be negative pressure or PPVL.
- The archive also contains **SHTM 03-01 Part A - Design and Validation, Version 2, February 2014 (ARCHIVED)**. Appendix 1, Table A1, printed page 139 gives critical-care areas: supply; 10 ac/h; +10 Pa; F7; noise rating 30; 18-25°C; isolation room may be negative pressure. This is historical Scottish evidence and is not the current UK comparison basis.

## HBN 04-02

Direct archive verification from **Health Building Note 04-02: Critical care units**, 2013:

- §4.14, printed page 9: minimum bed space **25.5 m²**.
- §4.17, printed page 9: recommended ceiling height in bed areas **3 m**.

## FGI and SCCM adult ICU design guidance

- `2022-Hosp-Major-additions-and-revisions.pdf` is only the major-additions/revisions extract from the **2022 Guidelines for Design and Construction of Hospitals**. It confirms that the 2022 Hospital Guidelines incorporated the November 2021 issue of ASHRAE 170 with addenda c and d, but it contains no adult ICU patient-room area clause.
- `society-of-critical-care-medicine-2024-guidelines-on-adult.pdf` is **Society of Critical Care Medicine 2024 Guidelines on Adult ICU Design**, published in *Critical Care Medicine*, March 2025. It provides no numerical ICU room-area requirement and explicitly makes no recommendation between advanced and standard HVAC systems because of insufficient evidence.
- Neither document closes the requested **FGI 2022 adult critical-care room area**. The full applicable FGI primary clause remains required.

## DIN

The supplied DIN PDF is **DIN 1946-4:2008-12**, useful as historical primary evidence.

It does **not** replace:

- DIN 1946-4:2018-09
- A1:2025-11.

Current DIN remains a gap for final guideline simulation.

## NF S 90-351

The supplied France Air material is secondary explanatory evidence, not the normative AFNOR standard. Current filtration/topology clauses remain a gap.

Latest guideline register:

`GUIDELINES_UPDATED_2026-08-12_v2.md`

---

# 6. Concentration evidence state

Main database:

`ICU_CONCENTRATION_EVIDENCE_DATABASE.xlsx`

Important corrections already locked:

1. Kim et al. primary ICU totals are **202 CFU/m³ bacteria** and **65 CFU/m³ fungi**. Earlier local values 176/59 were sums of named predominant genera, not the full totals.
2. Lucknow **1389 CFU/m³** bacteria is general-ward/hospital evidence, not an ICU-specific calibration target.
3. A PM₂.₅ model value around 3.4 µg/m³ is not physically impossible; it represents a clean/high-ventilation regime. The old model failed because it did not span polluted/high-load scenarios.
4. Tang et al. 2009 full PDF closes a major stressed-ICU evidence gap:
   - CO₂ 828–1570 ppm,
   - 92% CO₂ samples >1000 ppm,
   - PM₁₀ 4.2–43.7 µg/m³,
   - PM₁₀ median 20.7 µg/m³,
   - Tang “fine PM” is **PM₂ (<2 µm), not PM₂.₅**,
   - bacterial peaks up to 7236 CFU/m³,
   - fungal peaks up to 11654 CFU/m³,
   - visitation changes several IAQ variables and coarse PM responds to visitor number.

---

# 7. Forward activity/source model state

Latest integrated workbook:

`ICU_GENERATION_AND_SCHEDULER_MODEL_v0.3.xlsx`

Executable scheduler:

`icu_activity_source_scheduler.py`

## 15-minute scheduler

- 96 intervals/day.
- Evidence-constrained activity fractions and recurring event frequencies.
- Unsupported universal clock times are not invented; events remain stochastic/configurable where required.

### Patient

- 1 patient per occupied bed.
- Continuous presence while the bed is occupied.
- Sleep/quiet baseline plus explicit care/respiratory events.

### Nursing

Headcount:

- organ-support / Level-3: approximately 1:1 direct-care nurse:patient;
- lower-intensity / Level-2: approximately 1:2 minimum.

Time-motion fractions currently implemented:

- direct care 51.27%
- documentation 17.91%
- communication 17.61%
- indirect care 7.31% derived remainder
- personal 2.42%
- miscellaneous 3.48%

NAS is used as a clinical-task taxonomy, not a pollutant source itself.

### Doctors / rounds

- two structured bedside rounds/day;
- duration configurable; ~15 min/patient retained as a literature central prior;
- round clock times are not universal standards.

### Cleaning

- routine ICU cleaning twice daily + as needed;
- terminal cleaning at discharge/transfer;
- duration remains configurable.

### Visitors

- local-policy scenario input;
- Tang validation case uses its observed 30-minute visitation structure.

---

# 8. Pollutant generation model state

## CO₂ — ready

Forward physiological source:

\[
S_{CO_2}(t) = \sum_j \dot V_{CO_2,j}(t)
\]

with basal metabolic rate + MET activity.

No inverse concentration calibration.

## PM — mechanism-based

PM generation is not one fixed ICU mg/person·h value.

\[
S_{PM,i} =
S_{\mathrm{occupancy},i}
+S_{\mathrm{bed/resusp},i}
+S_{\mathrm{movement},i}
+S_{\mathrm{cleaning},i}
\]

Outdoor PM is a separate OA boundary/import term.

Size-resolved resuspension form:

\[
S_{\mathrm{resusp},i}
=
R_i(a,t)L_iA_{\mathrm{disturbed}}
\]

where surface loading and event intensity remain uncertain/validation variables.

## Viable bacteria

Culture-based transfer priors now exist independently of ICU concentration targets.

Current uncertainty architecture uses activity-conditioned human source bands constrained by independent culture-based measurements, plus:

- resuspension,
- optional respiratory/procedure events,
- outdoor import where relevant.

Do not back-calculate source from target ICU CFU.

## Viable fungi

Fungal CFU is handled by source decomposition:

\[
S_F =
S_{F,\mathrm{human}}
+S_{F,\mathrm{resusp}}
+S_{F,\mathrm{HVAC}}
\]

while outdoor fungi are a separate boundary term.

Do **not** convert:

- qPCR genomes,
- cell equivalents,
- spore-equivalents,
- fluorescent biological particles

directly into CFU.

---

# 9. Kim size-resolved viable model

Keep the **native six-stage Andersen grid**:

| Stage | Aerodynamic size |
|---|---|
| 6 | 0.65–1.1 µm |
| 5 | 1.1–2.1 µm |
| 4 | 2.1–3.3 µm |
| 3 | 3.3–4.7 µm |
| 2 | 4.7–7.0 µm |
| 1 | >7.0 µm |

Kim exact ICU checks:

- bacteria total = 202 CFU/m³
- bacteria respirable (Stages 3–6) = 142 CFU/m³
- fungi total = 65 CFU/m³
- fungi respirable (Stages 3–6) = 47 CFU/m³

Current numerical approach:

- preserve native stage bins;
- carry figure-digitisation uncertainty explicitly;
- compare a figure-derived stage shape with a version constrained to exact table respirable fractions;
- default scheduler currently uses a blend for demonstration/sensitivity;
- Stage 1 is open-ended; any representative diameter is numerical only and must receive sensitivity rather than be treated as a Kim measurement.

---

# 10. UVGI state

**Existing model — do not rebuild.**

It contains ray-tracing / lamp configuration work and prior CFD-coupling assets.

Future coupling:

\[
C_{\mathrm{UV,out},i}
=
S_{\mathrm{UV},i}
C_{\mathrm{UV,in},i}
\]

for viable bins only.

For non-viable PM and CO₂:

\[
S_{\mathrm{UV}} = 1
\]

in the concentration-removal sense.

The filter/well-mixed work should expose a clean adapter to the UVGI model.

---

# 11. Filter model — locked architecture for current implementation

The filter is a **stateful component**, not a fixed efficiency.

State variables include:

- elapsed operating time,
- captured PM mass by size bin,
- mass loading per unit media area,
- depth-loading state,
- dust-cake state,
- electret charge state if applicable,
- pressure drop,
- size-resolved penetration/efficiency.

## 11.1 Clean size-resolved capture

Use single-fibre filtration mechanisms:

- Brownian diffusion,
- interception,
- inertial impaction,
- diffusion–interception interaction.

Physics predicts dependence on:

- particle diameter,
- fibre diameter,
- face/media velocity,
- media thickness,
- solidity,
- air viscosity/slip.

Commercial filters remain calibratable to:

- ASHRAE 52.2 / MERV fractional-efficiency information,
- manufacturer fractional-efficiency curves,
- experimental OPC curves.

## 11.2 MERV calibration rule

ASHRAE 52.2 groups:

- E1: 0.3–1.0 µm
- E2: 1.0–3.0 µm
- E3: 3.0–10.0 µm

A MERV rating is not itself a complete diameter-by-diameter physical curve.

Therefore:

- standard MERV minimum values may be used as a **conservative calibration envelope**;
- final product simulations should use measured/manufacturer fractional curves where available;
- never pretend a MERV number uniquely determines fibre diameter, solidity, media area or electret charge.

## 11.3 Clean pressure drop

Physics-based media resistance is calculated from fibrous-medium structure and velocity, then calibrated against rated clean pressure drop / measured flow-resistance data.

Pleated filters use:

\[
U_{\mathrm{media}} = Q/A_{\mathrm{media}}
\]

not duct velocity.

Frame/pleat/structural resistance is represented separately and calibrated from measured total pressure drop.

## 11.4 Loading

At each time step:

\[
\Delta m_i =
Q\,C_{in,i}\,\eta_i\,\Delta t
\]

Pressure-drop loading is driven by **PM mass**, not CFU count.

Early loading is treated as deposition within the depth medium, changing effective solidity/collector dimensions.

When depth-loading capacity is exceeded, excess mass forms a surface cake.

## 11.5 Dust cake

Cake pressure drop uses Darcy flow with a permeability relation such as Kozeny–Carman:

\[
\Delta P_{\mathrm{cake}}
=
\mu U_{\mathrm{media}}\frac{L_{\mathrm{cake}}}{K_{\mathrm{cake}}}
\]

with cake porosity/particle effective diameter carried as calibration/uncertainty parameters.

## 11.6 Loading effect on efficiency

Mechanical efficiency is recalculated from the loaded effective media structure.

This naturally allows mechanical efficiency to increase with deposited dust.

Electret filters include a separate charge-state variable so that electrostatic performance can decline with loading even while mechanical collection increases.

## 11.7 Electret

Do not hide electret loss inside an arbitrary time-age curve.

Use:

- an initial charged efficiency curve;
- a discharged/mechanical curve where available;
- charge-state decay versus captured mass, calibrated to loading data.

If a discharged curve is unavailable, the model may estimate it from mechanical theory but must flag the result as higher-uncertainty.

## 11.8 Service life

Replacement may be triggered by:

- terminal pressure drop,
- minimum required fractional efficiency,
- product/manufacturer loading limit,
- explicit maintenance interval when used as a practical constraint.

Output:

- filter age/hours,
- captured mass,
- pressure-drop trajectory,
- efficiency trajectory,
- fan-energy penalty,
- service-life/replacement count.

## 11.9 Energy

\[
P_{\mathrm{filter}}
=
\frac{Q\,\Delta P_{\mathrm{filter}}}
{\eta_{\mathrm{fan}}\eta_{\mathrm{motor}}}
\]

and is integrated over time.

---

# 12. Well-mixed ICU + HVAC model — next coupling architecture

The room and duct are distinct but coupled.

For pollutant/bin \(i\):

\[
V\frac{dC_i}{dt}
=
S_i(t)
+
Q_s C_{s,i}
+
Q_{\mathrm{inf}} C_{\mathrm{out},i}
-
Q_{\mathrm{out}} C_i
-
k_{\mathrm{dep},i}VC_i
\]

The supply concentration is calculated by the HVAC treatment train.

## Mixing

\[
Q_{OA}=f_{OA}Q_s
\]

\[
Q_R=(1-f_{OA})Q_s
\]

\[
C_{\mathrm{mix},i}
=
f_{OA}C_{\mathrm{OA,path},i}
+
(1-f_{OA})C_{\mathrm{return},i}
\]

If no guideline OA prefilter exists:

\[
C_{\mathrm{OA,path},i}=C_{\mathrm{out},i}
\]

If one exists:

\[
C_{\mathrm{OA,path},i}=P_{\mathrm{OAfilter},i}C_{\mathrm{out},i}
\]

## Main filters

For one filter:

\[
C_{out,i}=P_i(t)C_{in,i}
\]

For filters in series:

\[
P_{\mathrm{bank},i}=\prod_j P_{j,i}
\]

## UVGI

Insert the existing UVGI survival operator after the appropriate filtration/treatment stage for viable bins.

## Exact recurrence

Within a 15-minute interval, for piecewise-constant source/controls:

\[
\frac{dC_i}{dt}=A_i-B_iC_i
\]

so:

\[
C_i(t+\Delta t)
=
C_{ss,i}
+
[C_i(t)-C_{ss,i}]e^{-B_i\Delta t}
\]

Use this exact recurrence.

---

# 13. Pressure modelling

Do not treat “positive pressure” as an arbitrary pollutant-removal percentage.

Use airflow imbalance/leakage when quantitatively modelling pressure:

\[
Q_{\mathrm{leak}}
=
C_L(\Delta P)^n
\]

Until leakage parameters are supported, pressure can remain a guideline-compliance constraint rather than a fabricated contaminant term.

---

# 14. Validation gates

## Generation layer

Must reproduce, without inverse source fitting:

- clean ICU regimes,
- stressed ICU regimes,
- India high-load regimes,
- activity/seasonal event tails.

## Filter gate

Before full ICU coupling validate:

1. clean fractional efficiency vs particle size;
2. clean pressure drop vs flow;
3. pressure drop vs captured mass/time;
4. efficiency evolution with loading;
5. electret decline where relevant;
6. service-life/end-point behaviour.

## Room/HVAC gate

1. room/source transport without treatment;
2. OA/recirculation mixing;
3. filter treatment;
4. deposition;
5. existing UVGI for viable bins;
6. concentration distribution vs ICU literature.

## Only after these gates

Proceed to:

- guideline evaluation,
- guideline-constrained optimisation,
- project optimisation.

---

# 15. Experimental validation programme

Planned later:

| Experiment | Model component |
|---|---|
| Velocity traverse | duct/CFD/flow |
| OPC upstream/downstream | size-resolved filter efficiency |
| Differential pressure vs captured mass/time | filter loading / service life |
| Bioaerosol + UVGI at multiple velocities | existing UVGI |
| Tracer decay (CO₂ or SF₆) | well-mixed transport |
| Fan/chiller/heater power | energy model |

Filter experiment should measure at minimum:

- actual airflow/face velocity,
- upstream/downstream size concentrations,
- ΔP,
- elapsed time,
- captured/deposited mass if possible,
- filter grade/product and dimensions,
- clean and loaded condition.

---

# 16. Known traps / corrections that must not re-enter the project

1. Do not average incomplete outdoor-data days as full daily means.
2. Cross-station median must be a true median, not an upper median.
3. Do not report one data-coverage percentage for all pollutant bands.
4. Do not infer PM₂.₅/PM₁₀ ratio from mismatched outdoor time windows.
5. Do not use one low PM₂.₅/bioaerosol source condition for the entire ICU literature.
6. Do not call Tang PM₂ “PM₂.₅”.
7. Do not call Wainwright’s 5-minute cough-sampling count “CFU per cough”.
8. Do not convert qPCR/molecular biological counts directly to CFU.
9. Do not claim Lucknow 1389 CFU/m³ as ICU-specific.
10. Do not claim private Indian ICUs are generally compliant without an actual compliance audit.
11. Do not claim every guideline specifies an OA prefilter.
12. Do not claim ASHRAE 170-2025 two-bank topology until §6.4 is directly verified.
13. Do not justify an arbitrary UVGI maximum lamp number after the fact.
14. Do not optimise before source/filter/transport validation.

---

# 17. Current artefacts

Core source/project files:

- `00_PROJECT_BRIEF.md`
- `01_MODEL_PROPOSAL.md`
- `COMPLIANCE_AND_ENERGY.md`
- `LOCAL_DATA_INVENTORY.md`
- `GUIDELINES_UPDATED_2026-08-12_v2.md`

Evidence/model files:

- `ICU_CONCENTRATION_EVIDENCE_DATABASE.xlsx`
- `ICU_GENERATION_AND_SCHEDULER_MODEL_v0.3.xlsx`
- `icu_activity_source_scheduler.py`
- `scheduler_single_bed_15min.csv`
- `scheduler_multibed8_15min.csv`
- `scheduler_tang_validation_15min.csv`

User-supplied standards/evidence:

- Tang et al. 2009 PDF
- DIN 1946-4:2008-12 PDF
- France Air NF S 90-351 explanatory white paper
- ASHRAE 170-2025 Table 7-1 screenshots
- Archive.zip guideline verification set, received 2026-08-29:
  - VHHSBA HTG-2020-004, May 2020
  - SCCM 2024 Guidelines on Adult ICU Design, published March 2025
  - Saran et al. 2020 ICU HVAC review
  - SHTM 03-01 Part A, Version 2, February 2014 (archived)
  - HTM 03-01 Part A, 2021
  - FGI 2022 Major Additions and Revisions extract
  - ASHRAE Addendum h to Standard 170-2021
  - HBN 04-02, 2013
- Kim figure/image and primary literature references

---

# 18. Residual evidence/model gaps

## Standards

- AusHFG Part E or AS 1668.2:2012/2024 intensive-care ventilation entry
- DIN 1946-4:2018-09 + A1:2025-11
- NF S 90-351 normative filtration clauses
- FGI 2022 primary ICU geometry details
- ASHRAE 170-2025 §6.4 topology
- NBC 2016 Part 8 Section 3 ICU entries from Tables 4, 6 and 7
- CSA Z317.2 ICU row and CSA Z8000 ICU room-area clause, if Canada is retained

## Concentrations

- more high-quality Indian ICU CO₂/PM data across multiple cities/climates
- additional Indian active volumetric viable-aerosol studies

## Source model refinements

- culturable CFU per cough / cough-frequency distribution
- PPE/clothing-specific ICU viable shedding
- specific procedure-event viable emissions
- local Indian visitor/shift activity timing if available

## Filter

- real candidate filter/product data:
  - media/filter dimensions,
  - rated flow,
  - clean ΔP,
  - fractional efficiency curve,
  - electret status,
  - loading/terminal ΔP data,
  - dust-holding capacity.

The model must work without these using uncertainty/demo parameters, but final research conclusions should use real validated filter data where available.

---

# 19. Immediate development sequence from Update 1

1. **Build complete stateful physics-based filter module.**
2. Run numerical smoke tests:
   - efficiency remains 0–1,
   - ΔP rises with flow/loading,
   - captured mass conserves,
   - service-life trigger works,
   - electret can show decline then mechanical recovery.
3. Create filter validation/calibration data interface.
4. Couple filter module to:
   - OA filter switch,
   - mixed-air/main bank,
   - size-resolved PM and Kim viable bins.
5. Implement ICU room + HVAC exact well-mixed solver.
6. Validate baseline/source-driven concentrations before guideline simulation.
7. Then begin guideline evaluation.

---

# 20. Update log

## Update 1 — 2026-08-12

This update consolidates all project discussions and uploaded/project files through the start of the physics-based filter model.

Major state at this update:

- complete research objective clarified;
- guideline evaluation → guideline optimisation → original optimisation separated;
- two ICU geometries locked;
- concentration evidence database created and corrected;
- Tang 2009 fully integrated;
- current ASHRAE 170-2025 ICU Table 7-1 row verified from user screenshots;
- forward activity/source database created;
- evidence-constrained 15-minute single-/multi-bed scheduler implemented;
- Kim six-stage viable CFU harmonisation implemented;
- existing UVGI explicitly retained rather than rebuilt;
- filter model architecture locked;
- well-mixed ICU + HVAC coupling architecture locked as the next stage after filter validation.

**Next master update should append below this section rather than deleting Update 1.**


---

## Update 2 — 2026-08-12 — Physics-based filter model implemented

### New artefacts

- `icu_filter_model.py` — executable stateful filter model
- `test_icu_filter_model.py` — invariant/smoke tests
- `FILTER_MODEL_CALIBRATION_TEMPLATE.csv` — data-entry structure for literature/manufacturer/rig validation
- `filter_demo_loading_trajectory.csv` — illustrative loading trajectory for code verification only
- `filter_demo.json` — illustrative model output from the internal demonstration

### Implemented filter architecture

The filter is now a **stateful object**, usable independently as:

- outdoor-air prefilter,
- main/mixed-air MERV bank,
- HEPA/final bank,
- multi-stage filter bank.

Each physical stage retains its own loading and pressure-drop state.

### Implemented clean capture physics

Neutral-fibre mechanical capture includes:

- Brownian diffusion,
- direct interception,
- inertial impaction,
- diffusion–interception interaction.

The implementation uses a Kuwabara/single-fibre framework and converts single-fibre efficiency to full-media penetration.

Commercial clean performance is **not inferred solely from fibre geometry**. It is anchored by a clean fractional-efficiency curve and the physics then supplies flow/loading dependence.

### MERV handling

The code includes conservative screening envelopes for MERV 8–16 using the ASHRAE E-range structure:

- E1: 0.3–1 µm
- E2: 1–3 µm
- E3: 3–10 µm.

Important:

- these are **screening anchors**, not real product curves;
- where a MERV grade has no specified minimum for a range, the code falls back to mechanical physics rather than inventing an efficiency;
- final research conclusions should use actual manufacturer/ASHRAE/OPC fractional-efficiency curves whenever available.

### Implemented clean pressure-drop physics

Intrinsic fibrous-media resistance uses a Davies-type correlation.

For a real pleated element:

\[
U_{\mathrm{media}} = Q/A_{\mathrm{media}}
\]

not duct face velocity.

Rated commercial clean pressure drop is used to calibrate the total element resistance into:

- media component,
- structural/pleat/frame component.

This ensures the model does not claim false certainty from assumed microscopic media geometry.

### Implemented dynamic loading

For PM mass bin \(i\):

\[
\Delta m_i
=
Q C_{i,\mathrm{up}}\eta_i\Delta t
\]

Captured PM mass is stored by particle diameter.

Filter pressure-drop ageing is driven by **captured PM mass**, not viable CFU count.

### Implemented depth loading

Early deposited mass is distributed through the filter depth up to a configurable added-solidity capacity.

Effective solidity increases and an effective collector/fibre diameter is recalculated.

Mechanical efficiency and media resistance are then recomputed from the loaded media structure.

### Implemented surface cake

Mass above the depth-loading capacity forms a surface cake.

Cake pressure drop uses:

\[
\Delta P_{\mathrm{cake}}
=
\mu U_{\mathrm{media}}
\frac{L_{\mathrm{cake}}}{K_{\mathrm{cake}}}
\]

with Kozeny–Carman permeability.

Key calibration/uncertainty inputs include:

- cake porosity,
- particle material density,
- effective cake particle diameter,
- depth-loading capacity.

### Implemented electret ageing

Electret charge is represented as a separate state.

The model can use:

- charged initial fractional-efficiency curve;
- discharged/MERV-A/conditioned curve where available;
- deposited-mass characteristic charge-decay scale.

When no discharged curve is available, mechanical theory is used only as a higher-uncertainty surrogate.

The model therefore permits the physically important behavior:

1. initial charged efficiency;
2. charge shielding / small-particle efficiency decline;
3. increasing mechanical collection with deposited dust;
4. possible later efficiency recovery while ΔP keeps increasing.

### Implemented service life

A filter can be replaced when:

- terminal ΔP is reached;
- dust-holding capacity is reached, if known;
- a specified minimum fractional efficiency fails.

The state reports:

- elapsed h,
- captured mass,
- surface loading,
- depth/cake loading,
- effective solidity,
- effective fibre diameter,
- electret charge fraction,
- media/structural/cake/total ΔP,
- fan energy attributable to filter resistance,
- service-life status/reason.

### Implemented energy

Filter electrical fan-energy attribution uses:

\[
P_{\mathrm{elec,filter}}
=
\frac{Q\Delta P}
{\eta_{\mathrm{fan}}\eta_{\mathrm{motor}}}
\]

integrated over time.

### Implemented treatment interface

`FilterElement.treat_concentration()` applies current size-resolved penetration to **any concentration unit**, including:

- µg/m³,
- CFU/m³,
- particles/m³.

The unit is preserved.

Only PM mass concentration is supplied to the loading update.

This cleanly separates:

- removal physics,
- pressure-drop/loading physics.

### Implemented multi-stage bank

`FilterBank` applies multiple stages in series.

Every stage has an independent state.

The bank now uses one consistent pre-update filter state inside each time interval, so:

\[
m_{\mathrm{in}}
=
m_{\mathrm{captured,stage1}}
+
m_{\mathrm{captured,stage2}}
+\cdots+
m_{\mathrm{downstream}}
\]

is conserved numerically for the interval.

### Automated tests passed

`test_icu_filter_model.py` currently verifies:

1. rated clean ΔP is matched exactly;
2. clean ΔP rises monotonically with flow;
3. fractional efficiencies remain between 0 and 1;
4. staged-bank PM mass is conserved;
5. loading increases captured mass and ΔP;
6. electret charge declines with deposited mass;
7. terminal pressure-drop service-life trigger operates;
8. filter treatment never increases downstream concentration.

Current test output:

- clean-flow ΔP demonstration: 39.36, 63.36, 90.24, 120.0, 152.64 Pa over increasing flow;
- illustrative 7-day loaded ΔP: ~137.9 Pa;
- terminal service-life trigger successfully reached around 301 Pa in the synthetic stress test.

These demonstration numbers are **not research inputs**. They only verify numerical behavior.

### Remaining filter inputs needed for final research-grade calibration

For each candidate product/filter class, collect where possible:

- exact filter dimensions,
- media area / pleat geometry,
- rated airflow,
- clean ΔP versus flow,
- size-resolved efficiency curve,
- electret status,
- conditioned/discharged efficiency or MERV-A if available,
- loading test concentration/size distribution,
- ΔP versus captured mass/time,
- terminal ΔP,
- dust-holding capacity.

The code can run before these are available, but final quantitative comparison among MERV classes should not rely on the illustrative media defaults.

### Next model task after Update 2

Build the **ICU room + HVAC duct exact well-mixed model** and connect:

1. 15-minute activity/source scheduler;
2. outdoor-air and recirculated-air mixing;
3. optional OA filter;
4. one or more stateful filter stages;
5. existing UVGI operator for viable bins;
6. room deposition and return-air recirculation;
7. exact 15-minute exponential concentration recurrence.

The first coupled runs must be **validation runs, not optimisation runs**.


---

## Update 3 — 2026-08-12 — Filter model rebuilt and frozen at v1.0

### Trigger

A new uploaded document, **“HVAC Filter Physics Model — Comprehensive Report”**, was reviewed before proceeding to the well-mixed model.

The user explicitly instructed that **no downstream model work should continue until the filter model is complete**.

That instruction is now locked.

### Critical finding

Update 2’s filter code was useful structurally but **not complete enough to freeze** because it did not represent several important elements contained in the uploaded report:

- multi-/two-population fiber architecture;
- calibrated empirical impaction+bounce option;
- explicit media-area vs face-area pack geometry;
- frame/pack pressure-drop resistance;
- physical electret single-fiber capture;
- dual charged/discharged electret calibration;
- HEPA-specific diffusion treatment;
- explicit separation of accelerated KCl loading evidence from field ageing.

Therefore:

`icu_filter_model_v0_2_superseded.py`

is retained only for traceability.

The canonical filter engine is now:

`icu_filter_model_v1.py`

with identical current canonical copy:

`icu_filter_model.py`.

### Uploaded report: adopted versus corrected

The uploaded report is **not treated as fully verified**, consistent with the user’s warning.

#### Adopted

- two-population fiber structure;
- Britt reference anchor and fitted-parameter set as a **reference fit**;
- empirical Stokes impaction+bounce closure as a calibrated option;
- pack/media and frame pressure-drop separation;
- MERV-13 dual-state charged/discharged concept;
- electret surface-charge decay architecture;
- Freudenberg area-ratio / pack-resistance information as report-derived validation data;
- Camfil 30/30 M8 4-in known-geometry anchor as report-derived validation data;
- KCl accelerated-loading exponents as validation metadata;
- the report’s explicit underdetermination warnings.

#### Corrected / not copied literally

1. **Diffusion**

   The report’s written diffusion expression is not used as the main MERV equation.

   v1.0 retains the independently primary-source-checked Rudnick/Lee–Liu form:

   \[
   \eta_D =
   \frac{2.6}{\epsilon}
   \left(\frac{1-\alpha}{Ku}\right)^{1/3}
   Pe^{-2/3}.
   \]

2. **Impaction**

   The failed ODE trajectory model is not represented as validated physics.

   Two transparent alternatives exist:
   - published Stechkina correlation with domain flag;
   - report-calibrated empirical impaction+bounce closure.

3. **Accelerated KCl ageing**

   The report’s \(t^n\) loading exponents are not converted into universal field-age laws.

   Actual ICU ageing remains driven by captured PM mass.

4. **MERV-11**

   No MERV-13 loading curve is silently applied to MERV-11.

5. **HEPA**

   HEPA is a separate product-calibrated family.

   The general MERV fit is not forced to reproduce H13/HEPA.

6. **MERV labels**

   Britt’s reported E1/E2/E3 values diagnose as MERV 9; the code therefore calls it `BRITT_REFERENCE` rather than hard-coding the report section title “MERV-8 mechanical core.”

### v1.0 filter state

Every physical filter element now contains:

- elapsed operating time;
- captured mass by particle-size bin;
- surface mass loading;
- depth-loading mass;
- cake mass;
- effective loaded solidity;
- effective fiber scale;
- electret charge fraction;
- media pressure drop;
- frame/pack pressure drop;
- cake pressure drop;
- total pressure drop;
- fan-energy accumulation;
- service-life status and reason.

### v1.0 clean efficiency physics

For each fiber population \(j\):

- Brownian diffusion;
- direct interception;
- diffusion–interception interaction;
- inertial impaction;
- optional bounce;
- induced electret capture;
- Coulombic electret capture.

The macroscopic multi-fiber exponent is:

\[
E
=
1-
\exp\left[
-\frac{4\alpha L}{\pi(1-\alpha)}
\sum_j\frac{f_j\eta_{sf,j}}{d_{f,j}}
\right].
\]

### v1.0 electret architecture

Physical electret mode includes:

- fiber surface charge density;
- fiber/particle dielectric properties;
- induced capture;
- Coulombic capture;
- selectable particle charge distribution;
- mass-dependent charge decay.

Commercial electret mode can also use:

- measured clean fractional curve;
- measured discharged/conditioned curve;
- physics-derived velocity/loading change.

This dual-state hybrid is the **preferred research mode** when product curves exist.

### v1.0 pressure-drop architecture

Clean filter:

\[
\Delta P_{\rm clean}
=
k_{\rm media}U_{\rm media}
+
k_{\rm frame}U_{\rm face}.
\]

If measured \(k\) values are unavailable, the two-population Kuwabara media resistance provides the structure dependence and rated clean product ΔP calibrates the full element.

This explicitly respects:

\[
U_{\rm media}=Q/A_{\rm media},
\]

not duct velocity through the media.

### v1.0 loading

PM mass conservation drives state evolution:

\[
\Delta m_i
=
Q C_{i,\mathrm{up}}\eta_i\Delta t.
\]

Depth loading changes effective media structure.

After depth capacity is reached, the surface cake can use:

- Darcy + Kozeny–Carman; or
- a product-calibrated mass-power loading law.

The high-concentration accelerated KCl time exponents are stored for validation only unless a trustworthy mass calibration exists.

### v1.0 efficiency during ageing

Mechanical efficiency changes with loaded structure.

Electret efficiency can decline as charge decays.

A separate cake-capture term exists but its coefficient is **not invented**; it remains inactive unless loading-efficiency data justify/calibrate it.

Therefore the model can reproduce the physically important competition:

- electret decline;
- mechanical improvement with deposited mass;
- increasing ΔP;
- possible later overall-efficiency recovery.

### v1.0 HEPA

HEPA uses:

- product/test fractional curve for absolute performance;
- optional Payet-type fine-fiber slip correction for relative mechanical behavior;
- HEPA-specific loading calibration.

This closes the **model architecture** gap while retaining HEPA product data as a calibration requirement.

### v1.0 installation bypass

Overall installed penetration:

\[
P_{\rm installed}
=
b+(1-b)P_{\rm media}.
\]

This allows rack/filter leakage to limit the effective efficiency even when media efficiency is very high.

### v1.0 bank

Multiple stages in series retain independent state.

PM mass conservation is enforced step-wise:

\[
m_{\rm inlet}
=
\sum_jm_{\rm captured,j}
+
m_{\rm outlet}.
\]

### v1.0 service life

Replacement criteria supported:

- terminal ΔP;
- DHC;
- minimum fractional efficiency.

### v1.0 automated validation

`test_icu_filter_model_v1.py` contains 15 numerical tests.

**All 15 pass.**

Key exact checks:

- Britt ΔP = 93.4 Pa at rated point;
- Britt E1/E2/E3 = 17.5/58/77%;
- Britt diagnostic grade = MERV 9;
- MERV-13 clean E1/E2/E3 = 72.0/90.1/93.8%;
- isolated fully discharged MERV-13 E1 → 27%;
- staged-bank mass balance error ≈ \(7.6\times10^{-21}\) kg;
- filter loading increases ΔP;
- DHC trigger operates;
- fan-energy accumulation operates;
- electret collection collapses at zero charge;
- bypass leakage caps effective installed efficiency.

### What remains before publication-quality filter comparisons

These are **calibration-data needs**, not missing filter-model modules:

- product dimensions/media area;
- clean ΔP–flow data;
- full fractional-efficiency curves;
- discharged/conditioned curves for electrets;
- ΔP vs captured mass;
- efficiency vs captured mass;
- terminal ΔP;
- DHC;
- field electret decay calibration.

The actual candidate-filter database will be built from literature/manufacturer/rig data before final optimisation.

### Filter development gate

**FILTER CORE MODEL: FROZEN at v1.0.**

No room/HVAC well-mixed implementation should be started until the current filter-model completion state is accepted or a new filter-specific evidence problem is identified.

### New artefacts

- `icu_filter_model_v1.py`
- `icu_filter_model.py`
- `icu_filter_model_v0_2_superseded.py`
- `test_icu_filter_model_v1.py`
- `filter_model_v1_test_output.txt`
- `FILTER_MODEL_COMPLETION_STATUS_v1.md`
- `FILTER_PRODUCT_CALIBRATION_TEMPLATE_v1.csv`
- `filter_reference_data_v1.json`

---

## Update 4 — 2026-08-12 — Filter strategy simplified for thesis core

### Decision

The detailed v1.0 micro-mechanical filter model is **not** the preferred core model for the ICU optimisation study.

The preferred thesis-core filter model is now a **validated semi-empirical state model** because the project objective is ICU ventilation/IAQ/energy optimisation, not microscopic filter-media design. The detailed model remains useful as a mechanistic sensitivity/appendix tool.

### Thesis-core filter model

For each actual filter/product, use:

- measured clean fractional-efficiency curve η0(dp,Q);
- measured clean pressure-drop curve ΔP0(Q);
- captured PM mass as the state variable;
- pressure-drop loading law fitted to experimental/manufacturer/literature data;
- loaded/discharged efficiency curves where available;
- terminal pressure drop / dust-holding capacity / minimum-efficiency replacement criterion.

Captured mass:

ΔM_i = Q C_i,up η_i Δt

Pressure drop:

ΔP(Q,M) = ΔP0(Q) + ΔPload(Q,M)

Preferred loading forms are selected by validation, e.g.:

ΔPload = a(Q) M^b

or:

ΔPload = a U_media (M/A_media)^b

No universal a,b values are assumed across products.

Efficiency ageing:

- mechanical filters: interpolate η_i(M) from clean/loaded test curves if available;
- electret filters: interpolate between measured clean and discharged/aged curves using loading state;
- when loaded-efficiency data are unavailable, retain clean validated efficiency and treat ageing as a sensitivity case rather than inventing media microphysics.

Service life:

t_life = min[t(ΔP ≥ ΔPterminal), t(M ≥ MDHC), t(η_i < η_i,min)]

Filter fan energy:

P_filter(t) = Q(t) ΔP(t)/(ηfan ηmotor)

### Validation gate

Each candidate filter should be validated against:

1. clean fractional efficiency vs particle size;
2. clean pressure drop vs flow;
3. pressure drop vs captured mass/loading;
4. loaded/discharged efficiency if available;
5. terminal pressure drop / DHC / replacement criterion.

### Role of detailed v1.0 model

`icu_filter_model_v1.py` is retained for:

- mechanistic sensitivity analysis;
- interpretation of fibre/electret/cake physics;
- possible appendix or future publication;
- experimental-analysis support.

It should not drive the main ICU optimisation unless the microscopic media/loading parameters are independently validated for the actual filter product.

### Locked interpretation

A simple model is acceptable only if it remains **validated and stateful**.

The project should not revert to one constant MERV efficiency and one fixed clean pressure drop.

Preferred thesis-core formulation:

> measured size-resolved efficiency + captured-mass balance + empirical pressure-drop loading + evidence-based efficiency ageing + service life + fan energy.

---

## Update 5 - 2026-08-12 - Strict no-placeholder filter evidence policy implemented

### User constraint locked

No placeholder, assumed, proxy, analogous, or cross-product numerical data may be used anywhere in the project.

This now applies not only to final results but to the executable filter model itself.

### New thesis-core filter engine

`icu_filter_semiempirical.py`

replaces the detailed micro-mechanical model as the core optimisation filter engine.

The detailed `icu_filter_model_v1.py` remains an optional mechanistic/sensitivity tool only.

### Fail-closed behaviour

The core model now raises a hard evidence error when:

- efficiency is requested at a flow with no direct efficiency evidence;
- diameter lies outside a directly digitized/measured curve;
- pressure drop is requested outside a directly measured/digitized flow range;
- loaded pressure drop is requested without direct same-product ΔP-versus-captured-mass evidence;
- filter age is requested without a defensible same-product loading law.

No MERV grade is used as a synthetic full fractional-efficiency curve.

No accelerated KCl time exponent is converted to field age.

No MERV-13 ageing is transferred to MERV-11.

No classless "HEPA" requirement is silently mapped to H13 or H14.

### Direct product profiles now assembled

- Camfil Farr 30/30 MERV8/8A, 24x24x4, part 059413001;
- Camfil Hi-Flo ES MERV11, 24x24x22, 10 pocket;
- Camfil Hi-Flo ES MERV13, 24x24x22, 10 pocket;
- Camfil Hi-Flo ES MERV14, 24x24x22, 10 pocket;
- Camfil Absolute VGHF E10;
- Camfil Absolute VGHF H13;
- Camfil Absolute VGHF H14.

For MERV8/11/13/14, manufacturer fractional-efficiency graphs were digitized directly and remain labelled `DIRECT_DIGITIZED_PRIMARY_CURVE`.

For Hi-Flo ES MERV11/13/14, the manufacturer 22-inch clean pressure-drop/airflow graph was digitized directly and the exact 2000 cfm table values supersede graph digitization at that point.

For E10/H13/H14, the model uses EN1822/ISO29463 MPPS class efficiency only as a `CERTIFIED_MPPS_GLOBAL_LOWER_BOUND`, not as an exact diameter-resolved curve.

### Direct loading evidence retained separately

Huang, Jung & Boor (2025) provides direct accelerated KCl loading data for its own MERV8/MERV13/MERV14 test specimens.

At baseline 2000 cfm, terminal captured filter mass was:

- MERV8: 40.4 ± 2.8 g;
- MERV13: 79.4 ± 2.7 g;
- MERV14: 107 ± 15.5 g.

These values are NOT attached to the Camfil products.

The paper's continuous loading curves use loading time and salt-stick mass consumed, while actual filter captured mass is terminal gravimetric data. Therefore no false ΔP-versus-captured-mass fit is made.

### Filter-age status

Product-specific location/climate filter-age prediction remains **BLOCKED** at Update 5.

This is intentional.

The identified Purdue field-age sources contain the required type of evidence, but the full numerical same-product ΔP-versus-captured-mass trajectory has not yet been extracted. Until it is, the model will not calculate filter age.

### Current legitimate outputs

Available:

- clean size-resolved removal at source-supported flow;
- clean ΔP at source-supported flow/domain;
- clean filter fan power with externally supplied fan/motor efficiencies;
- captured PM mass bookkeeping;
- certified lower-bound HEPA/EPA removal where appropriate.

Blocked:

- loaded ΔP trajectory;
- numerical efficiency ageing;
- replacement age;
- annual replacement count;
- loading-related annual fan-energy trajectory.

### New files

- `filter_evidence_profiles_v1.json`
- `icu_filter_semiempirical.py`
- `test_icu_filter_semiempirical.py`
- `filter_semiempirical_test_output.txt`
- `FILTER_SEMIEMPIRICAL_MODEL_STATUS_v1.md`

The next filter task is **not** to invent a loading law. It is to obtain/extract direct product or field ΔP-versus-captured-mass evidence and only then unlock the age calculation.

---

## Update 6 — 2026-08-12 — Final filter strategy: calibrated state model, not endless product-specific mechanics

### Why the previous gate was wrong

The project was becoming blocked because numerical product-specific filter ageing was being treated as a prerequisite for calling the **filter model** complete.

That confuses:

1. the mathematical model structure; and
2. the calibration data for a specific commercial filter.

The filter model must be complete once its state equations, measurable parameters, validation procedure, service-life criterion and uncertainty rules are fixed. Missing calibration data for a particular product should not force a redesign of the filter model.

### Final thesis-core filter formulation

#### A. Clean size-resolved efficiency

For product \(j\):

\[
\eta_{j,i,0}(Q)
\]

comes directly from a manufacturer/standard test or project experiment.

No microscopic fibre model is required in the thesis core.

#### B. Captured PM mass — ageing state variable

\[
\frac{dM_j}{dt}
=
Q_j(t)
\sum_i
C_{j,i,\mathrm{up}}(t)\eta_{j,i}(t)
\]

or discretely:

\[
M_j^{n+1}
=
M_j^n
+
Q_j^n
\sum_i
C_{j,i,\mathrm{up}}^n\eta_{j,i}^n
\Delta t.
\]

This is the only mandatory dynamic filter state required for the ICU optimisation.

#### C. Pressure drop — validated semi-empirical form

The preferred model family is the Li et al. 2022 form:

\[
\boxed{
\Delta P_j(Q,M)
=
k_j Q^{a_j} b_j^{M}
}
\]

where:

- \(Q\) = airflow;
- \(M\) = captured dust loading mass in the calibration unit;
- \(k,a,b\) = experimentally identified coefficients for the selected filter.

At \(M=0\):

\[
\Delta P_{j,0}(Q)=k_j Q^{a_j}.
\]

Therefore:

- \(k_j,a_j\) are identified from the filter's clean \(\Delta P-Q\) curve;
- \(b_j\) is identified from direct loading evidence for that exact filter/product or the project duct experiment.

The model form is fixed; calibration values can be updated without changing the equations.

#### D. Minimal calibration requirement for \(b\)

A full continuous loading curve is preferred but is **not mathematically mandatory**.

If the same exact filter has:

- clean pressure drop at a known flow;
- a directly measured captured mass at a known loaded state;
- pressure drop at that same loaded state,

then:

\[
b_j
=
\left(
\frac{\Delta P_{\mathrm{loaded}}}
     {k_j Q^{a_j}}
\right)^{1/M_{\mathrm{loaded}}}.
\]

Thus one valid captured-mass/loading endpoint can identify \(b_j\); multiple points are used for validation and uncertainty.

This removes the previous unnecessary requirement that every selected product must have a published continuous \(\Delta P(M)\) curve before the model can exist.

#### E. Efficiency ageing

The thesis core will not invent a universal \(\eta(d,M)\) law.

Use this hierarchy:

1. direct clean + loaded/aged fractional curves -> interpolate using measured loading state;
2. direct clean + conditioned/discharged curve for electret -> use as measured lower/aged state;
3. direct manufacturer evidence that a mechanical filter maintains/increases efficiency -> clean curve may be retained explicitly as a conservative lower-bound removal curve;
4. otherwise -> hold efficiency ageing as an uncertainty/sensitivity layer, not a missing pressure-drop model.

The pressure-drop/service-life model can therefore be complete independently of a fully resolved efficiency-ageing curve.

#### F. Service life / filter age

Replacement is predicted from:

\[
\Delta P_j(Q(t),M_j(t))
\ge
\Delta P_{j,\mathrm{terminal}}
\]

or a directly specified product endpoint.

Therefore filter age is an **emergent output**:

\[
t_{\mathrm{life}}
=
\min\{t:\Delta P(t)\ge\Delta P_{\mathrm{terminal}}\}.
\]

Climate/location enters through the upstream PM concentration and particle-size distribution that drive \(M(t)\).

#### G. Filter energy

\[
P_{\mathrm{filter}}(t)
=
\frac{Q(t)\Delta P(t)}
{\eta_{\mathrm{fan}}\eta_{\mathrm{motor}}}.
\]

No separate empirical filter-energy model is required.

### Product-selection rule

Guidelines specify filter performance classes, not one universal commercial pressure drop.

For guideline simulations, choose one or more **fully characterized compliant real products** for each required class and report results as product-specific compliant cases.

Do not claim one selected product is numerically representative of every MERV-13 or every MERV-14 filter.

Filter product can later be a discrete design variable in the original optimisation.

### Role of Li et al. model evidence

Li et al. experimentally developed a pressure-drop equation using airflow and dust-loading mass and reported high regression accuracy. The paper explicitly highlights that the model avoids difficult-to-measure fibre thickness/diameter/packing-density inputs and was checked against other filter-loading datasets.

This is the preferred thesis-core loading model architecture.

### Role of detailed micro-mechanics

`icu_filter_model_v1.py` remains archived as:

- optional mechanistic sensitivity work;
- interpretation;
- appendix/future publication;
- experimental-analysis support.

It is no longer allowed to block the ICU system model.

### New completion criterion

The **filter model is complete** when:

1. the clean efficiency interface is fixed;
2. captured-mass balance is fixed;
3. \(\Delta P(Q,M)=kQ^a b^M\) is implemented;
4. coefficient fitting/validation routines are implemented;
5. service-life and fan-energy equations are implemented;
6. uncertainty and evidence status are reported.

The model does **not** need every final commercial filter coefficient before the ICU room/HVAC coupling can be implemented.

Product-specific coefficients are calibration inputs populated progressively from direct literature/manufacturer/project experiments.

### Immediate consequence

The project should stop redesigning filter mechanics.

Next filter implementation task:

- build the final calibrated-state code around \(k,Q,a,b,M\);
- include clean-curve and loaded-endpoint fitting;
- validate it first against Li et al. and any directly available captured-mass datasets;
- then freeze the filter equations permanently.

After that, the ICU + HVAC well-mixed coupling can proceed while remaining product calibrations are added independently.

---

## Update 7 — 2026-08-12 — Pease et al. 2021 well-mixed filtration treatment reviewed

Paper:

Leonard F. Pease et al., **“Investigation of potential aerosol transmission and infectivity of SARS-CoV-2 through central ventilation systems,”** Building and Environment 197 (2021) 107633. DOI: 10.1016/j.buildenv.2021.107633.

### What the paper does

Pease et al. use a **multiroom well-mixed contaminant model** connected by a central AHU.

Each room is treated as well mixed.

Virus is generated in a source room and can:

- leave the source room through return air;
- enter the central AHU/plenum;
- mix with outdoor air;
- pass through a central filter;
- return via supply air to the source and connected rooms.

### Filtration treatment

The filter is **not** a separate ageing/pressure-drop physics model.

It is a **single-pass contaminant-removal operator** in the AHU.

The paper explicitly defines a filter efficiency \(\varepsilon\), with examples:

- no filter: 0%;
- MERV 8: 75%;
- MERV 11: 94%;
- MERV 13: 98%.

These are used as fixed single-pass efficiencies for the modeled virus-containing aerosol case.

The filtration operation is equivalent to:

\[
C_{\mathrm{after\,filter}}
=
(1-\varepsilon)\,
C_{\mathrm{before\,filter}}.
\]

The supply concentration is therefore determined by:

1. room return-air concentration;
2. outdoor-air dilution/mixing;
3. single-pass filter penetration.

### Important modeling consequence

Pease et al. do **not** model:

- filter loading;
- filter pressure-drop growth;
- filter age/service life;
- time-varying filter efficiency;
- detailed media physics;
- duct deposition mechanisms such as thermophoresis/turbophoresis.

Thus their filtration treatment is a contaminant-transport boundary/operator inside the well-mixed HVAC mass balance.

### Relevance to this PhD

This paper supports keeping the **room/HVAC contaminant solver** simple:

\[
C_{\rm filtered,i}
=
P_i C_{\rm mixed,i},
\qquad
P_i=1-\eta_i.
\]

The difference in this project is that \(P_i\) will come from the separate filter submodel/evidence database, potentially changing with filter state where direct evidence supports it.

Therefore the architecture should be:

\[
\text{room return}
\rightarrow
\text{OA/return mixing}
\rightarrow
\text{filter operator}
\rightarrow
\text{UVGI operator for viable bins}
\rightarrow
\text{supply}
\rightarrow
\text{room well-mixed balance}.
\]

Filter pressure drop and filter age remain **energy/service-state calculations running in parallel**. They do not need to complicate the well-mixed concentration differential equation itself.

### Key lesson

For the system model, filtration can be represented by a single-pass penetration operator while the filter lifecycle model is kept modular.

This is a useful precedent for the final ICU architecture and reinforces the decision to stop embedding fibre-scale mechanics directly inside the room concentration solver.

---

## Update 8 — 2026-08-14 — Compact activity-based ICU generation methodology

### Core source philosophy

The ICU pollutant source is generated **forward from occupancy and activity**, not back-calculated from a target room concentration.

\[
\boxed{
\text{beds/occupancy/staffing}
\rightarrow
\text{15-min activity scheduler}
\rightarrow
\text{pollutant-specific source}
\rightarrow
\text{size bins}
\rightarrow
\text{ICU + HVAC well-mixed model}
}
\]

### Scenarios and scheduler

- Single-bed ICU and multi-bed/open ICU are simulated separately.
- Time step = 15 min (96 intervals/day).
- Patient presence follows occupied beds.
- Nurse headcount follows ICU acuity/staffing evidence.
- Nurse person-time fractions are preserved:
  - direct care 51.27%
  - documentation 17.91%
  - communication 17.61%
  - indirect care 7.31%
  - personal 2.42%
  - miscellaneous 3.48%
- NAS is used as a task taxonomy, not as an emission factor.
- Doctor rounds, cleaning and visitation are explicit events.
- Unsupported universal clock times are not invented; where only frequency/fraction is known, event timing remains stochastic/configurable.

### CO2

\[
S_{CO_2}(t)=\sum_j \dot V_{CO_2,j}(t)
\]

with each person's source based on BMR and MET/activity state.

### PM

\[
S_{PM,i}
=
S_{\rm occupancy,i}
+
S_{\rm movement/resuspension,i}
+
S_{\rm bed,i}
+
S_{\rm cleaning,i}
\]

with resuspension represented through:

\[
S_{\rm resusp,i}=R_i(a,t)L_iA_{\rm disturbed}.
\]

Outdoor PM is an HVAC boundary term, not internal generation.

### Viable bacteria

\[
S_{B,i}
=
S_{B,\rm human}f_{B,i}
+
S_{B,\rm resusp,i}
+
S_{B,\rm event,i}.
\]

The human term uses independent culture-based source evidence and activity state. Respiratory/procedure events remain separate.

### Viable fungi

\[
S_{F,i}
=
S_{F,\rm human}f_{F,i}
+
S_{F,\rm resusp,i}
+
S_{F,\rm HVAC,i}.
\]

Outdoor fungi are handled separately through the OA path. qPCR/genome/spore-equivalent values are never converted directly into CFU.

### Viable aerodynamic bins

Kim et al. ICU six-stage Andersen bins are retained:

- Stage 6: 0.65–1.1 µm
- Stage 5: 1.1–2.1 µm
- Stage 4: 2.1–3.3 µm
- Stage 3: 3.3–4.7 µm
- Stage 2: 4.7–7.0 µm
- Stage 1: >7.0 µm

Kim ICU concentration values are validation evidence, not generation inputs.

### Validation rule

Generated concentrations are compared independently against clean, stressed, India/high-load and event-tail ICU literature regimes.

The source term is never tuned simply to force agreement with a target concentration.

### HVAC handoff

Every 15-min interval supplies:

- \(S_{CO_2}(t)\)
- \(S_{PM,i}(t)\)
- \(S_{B,i}(t)\)
- \(S_{F,i}(t)\)

to the room/HVAC model.

The treatment chain is:

\[
\text{return}
\rightarrow
\text{OA/return mixing}
\rightarrow
\text{filter}
\rightarrow
\text{UVGI for viable bins}
\rightarrow
\text{supply}
\rightarrow
\text{ICU}.
\]

The filter pressure-drop/age/energy model runs in parallel; the well-mixed solver only needs the current size-resolved penetration.

### Main contribution

The project therefore does not assume one fixed ICU source rate. It generates pollutant load from:

- who is present,
- how many people are present,
- what activity they perform,
- when events occur,
- pollutant-specific generation/resuspension mechanisms,
- aerodynamic particle-size distribution.

This makes the source responsive to occupancy, acuity, ICU size and activity pattern before HVAC control is applied.

---

## Update 9 — 2026-08-14 — Activity-specific generation deprioritized; empirical ICU concentration/source framework adopted

### Problem identified

The previously developed activity-based scheduler is too scenario-specific for the thesis core because robust ICU-specific time-resolved activity/emission data are not available for patients, nurses, doctors, visitors and cleaners across all pollutants.

A detailed activity schedule would therefore introduce more assumptions than evidence.

### Revised principle

The thesis core should be **evidence-driven from measured ICU pollutant concentration behavior**, with activity-generation retained only as an optional mechanistic sensitivity layer.

The measured ICU literature shows very wide concentration variation across hospitals and operating conditions. For example:

- Keyvani et al. (2020), Kashan ICU:
  - indoor PM2.5 mean = 54.32 µg/m³;
  - indoor PM10 mean = 210.96 µg/m³;
  - outdoor PM2.5 mean = 66.43 µg/m³;
  - outdoor PM10 mean = 312.32 µg/m³;
  - indoor and outdoor PM were significantly positively associated.
- Vahidmoghadam et al. (2023), Kashan intensive-care wards:
  - one-hour PM2.5 means across PICU/ICU-OH/NICU ≈21.53–28.52 µg/m³;
  - one-hour PM10 means ≈47.10–60.88 µg/m³;
  - ICU-OH ventilation was reported as exhaust fan rather than central HVAC.

This variation should not be collapsed into one universal minimum/maximum range without stratifying measurement and ventilation conditions.

### Final recommended evidence hierarchy

#### Tier A — source-reconstruction studies

Use studies/data with:

- time-resolved indoor concentration \(C_i(t)\);
- simultaneous outdoor concentration \(C_{out,i}(t)\);
- known HVAC operating condition / ACH / airflow / FOA / filtration where available;
- room volume.

For these studies, reconstruct an empirical net source/disturbance:

\[
S_{net,i}(t)
=
V\frac{dC_i}{dt}
-
Q_sC_{s,i}
+
Q_{out}C_i
+
k_{dep,i}VC_i
\]

with only directly supported terms included.

This source captures the total unresolved effect of occupancy, care activity, resuspension and other indoor events without requiring activity labels.

#### Tier B — time-resolved concentration studies with incomplete HVAC metadata

Use these to derive:

- normalized fluctuation profiles;
- peak frequency;
- percentile ranges;
- event amplitudes;
- temporal variability.

Do not inverse-calculate a source if airflow/treatment terms are unknown.

#### Tier C — summary-statistic studies

Studies reporting only mean/SD/min/max are used to define independent ICU concentration regimes:

- low/clean;
- moderate;
- high/stressed;
- extreme/event-tail.

They are not converted directly into generation rates.

#### Tier D — contextual studies

Data from non-comparable wards, non-HVAC ventilation, passive sampling, mismatched averaging periods, or insufficient metadata are kept for context/validation only.

### Scenario construction

Do not use raw global minimum and maximum alone.

For each pollutant build a stratified evidence distribution by:

- ICU type;
- ventilation system;
- location/climate;
- season;
- measurement averaging time;
- indoor/outdoor relationship;
- sampling method;
- HVAC operating state where reported.

Preferred scenario levels:

- P10/P25 = clean/low;
- P50 = typical;
- P75/P90 = high/stressed;
- P95/event maximum = extreme tail,

only when enough comparable observations exist. Otherwise use study-specific empirical scenarios rather than artificial percentiles.

### How concentration data enter the model

Measured room concentration should **not** be inserted as the generation term.

It can enter in three defensible ways:

1. **Initial-condition / clearance scenario**
   \[
   C_i(0)=C_{i,\mathrm{measured}}
   \]
   to test how quickly a guideline HVAC configuration clears a known ICU pollution load.

2. **Empirical net-source reconstruction**
   infer \(S_{net,i}(t)\) from measured concentration dynamics only where the HVAC mass-balance terms are adequately known.

3. **Independent validation envelope**
   run the forward room/HVAC model and compare predicted concentration distributions with the literature distribution.

### Recommended thesis-core source model

The strongest framework is a **hybrid empirical source model**:

\[
\boxed{
\text{measured ICU concentration dynamics}
\rightarrow
\text{empirical net-source / fluctuation library}
\rightarrow
\text{well-mixed HVAC model}
}
\]

rather than:

\[
\text{assumed nurse/patient activity schedule}
\rightarrow
\text{poorly validated emission factors}.
\]

Activity-based generation remains useful for explanation/sensitivity but is no longer the primary source engine.

### Validation strategy

Use split evidence:

- calibration/source-reconstruction studies;
- independent validation studies.

Do not validate on the same study used to infer the source without a hold-out check.

### Important distinction

Differences between ICU studies are not treated as random noise only. They may arise from:

- outdoor PM loading;
- ventilation type;
- filtration;
- door/window opening;
- traffic/occupancy;
- climate and meteorology;
- season;
- sampling duration and method.

The model database must retain these metadata so scenario differences remain physically interpretable.

### Immediate next task

Rebuild the pollutant-input database around this hierarchy and classify every ICU concentration study as Tier A/B/C/D.

Then:

1. identify which pollutants have genuine time-resolved HVAC-operation data;
2. extract normalized fluctuation profiles where possible;
3. reconstruct empirical net source only for Tier A cases;
4. define low/typical/high/extreme concentration regimes from comparable studies;
5. use these regimes as initial/validation cases in the coupled ICU + HVAC well-mixed model.

---

## Update 10 — 2026-08-16 — Chiller COP and fan-efficiency evidence gate clarified

### Why this update matters

The energy ranking is presently gated by two numerical inputs:

1. chiller efficiency/COP under the applicable equipment and operating condition;
2. fan total electrical efficiency at the selected duty point.

No assumed, proxy, cross-product or silently inferred value is permitted.

### Consultant statement checked

The consultant statement that “TSECBC gives COP 2.9 for an air-cooled chiller under 300 TR” is **not accepted as stated and has not been entered**.

The capacity boundary is the problem:

- An official Government of Rajasthan publication reproducing the ECBC-era table gives air-cooled chiller COP 2.90 only for **<530 kW (<150 TR)** and COP 3.05 for **≥530 kW (≥150 TR)**, with corresponding IPLV 3.16 and 3.32 under ARI 550/590-1998.
- A Telangana-focused technical comparison reproduces the same TSECBC split, but the currently accessible copy is not the primary Telangana code document. It therefore corroborates the table but does not by itself satisfy the project's primary-evidence rule.
- Consequently, “2.9 for under 300 TR” appears to conflate the <150 TR air-cooled category with the separate 150–300 TR bands used for some water-cooled chiller categories.

Evidence links:

- Government of Rajasthan ECBC directive, Table 4.1: https://environment.rajasthan.gov.in/content/dam/raj/energy/common/ECB%20Directives%20dated%2028.03.2011.pdf
- Telangana comparison sheet citing the TSECBC guideline: https://www.scribd.com/document/750178172/EDS-Chiller-VRF-Tip-sheet-for-India

### ECBC 2017 evidence

The official BEE ECBC 2017 text, with amendments up to 2020, gives the following relevant requirements:

- Section 5.2.2.1 requires chillers to meet the BEE Standards and Labelling programme and requires at least a 1-star chiller for ECBC compliance.
- It permits air-cooled chillers for building cooling load below 530 kW; at or above 530 kW, air-cooled capacity is restricted to 33% of installed chilled-water capacity unless required by the authority having jurisdiction.
- For the **standard-design model** in the whole-building method, Table 9-5 gives air-cooled chiller COP/IPLV of **2.8/3.5 for <260 kWr** and **3.0/3.7 for ≥260 kWr**.

These Table 9-5 numbers are standard-design benchmarks, not evidence of the actual operating COP of an unspecified chiller and not a licence to use COP 3.0 as a product input.

Official source: https://beeindia.gov.in/WriteReadData/L45218/1734417634.pdf

### ECSBC 2024 evidence

The official BEE ECSBC 2024 code provides the newer national-code framework for current comparison; its legal applicability still depends on adoption by the relevant state/local authority:

- Section 6.3.2 / Table 6.12 expresses chiller requirements by BEE star class and requires ratings at both full and part load in accordance with IS 16590; it does not provide one universal operating COP for the proposed ICU system.
- Section 6.3.1 / Tables 6.9–6.11 separates fan **mechanical efficiency** from **motor efficiency class**:
  - ECSBC: 65% mechanical efficiency + IE3 motor;
  - ECSBC+: 70% mechanical efficiency + IE4 motor;
  - Super ECSBC: 75% mechanical efficiency + IE4 motor.
- Centrifugal and axial fans with shaft power ≥2.5 kW must additionally satisfy Fan Energy Index requirements: FEI ≥1.1 for centrifugal fans and FEI ≥1.0 for axial fans.

Official BEE landing page and ECSBC 2024 download: https://beeindia.gov.in/show_content.php?lang=1&level=2&lid=327&ls_id=201

### Fan total-efficiency decision

The code does **not** directly provide the single numeric fan total electrical efficiency required by

\[
P_{fan}=\frac{Q\Delta P}{\eta_{total}}.
\]

Mechanical efficiency and motor IE class are not interchangeable with total efficiency. For a direct-drive fan, the duty-point total electrical efficiency must at minimum resolve the applicable fan mechanical efficiency and the exact motor efficiency; if a VFD or transmission is present, its efficiency must also be included consistently.

Therefore:

\[
\eta_{total}
=
\eta_{fan,duty}\,\eta_{motor,duty}\,\eta_{drive,duty}
\]

where every factor must be taken from the exact selected fan/motor/drive data at the applicable airflow, pressure, speed and load. An IE3 or IE4 label alone is insufficient because the numerical motor efficiency depends on rated power, pole count and operating load.

### Model-entry rule

Keep two evidence levels separate:

1. **Code/reference case:** use only the explicitly applicable code benchmark or compliance calculation, labelled as a standard/reference case.
2. **Equipment/energy-ranking case:** require an exact manufacturer selection sheet or certified datasheet giving chiller full-load and part-load performance at defined rating/operating conditions, plus the fan curve/selection output and motor/VFD efficiencies at the chosen duty point.

No code minimum may be relabelled as actual product operating performance.

### Current gate status

| Input | Status | What closes it |
|---|---|---|
| TSECBC COP 2.9 claim | Rejected as phrased; not entered | Primary TSECBC clause showing the exact equipment category and capacity band |
| ECBC standard-design air-cooled COP | Verified as 2.8 (<260 kWr) or 3.0 (≥260 kWr), with corresponding IPLV 3.5 or 3.7 | Already closed for the ECBC standard-design/reference case only |
| Actual chiller operating COP | Blocked | Exact selected chiller model, capacity, certified performance at required outdoor/chilled-water and load conditions, preferably a full performance map |
| ECSBC fan mechanical efficiency | Verified for code comparison: 65% / 70% / 75% by level | Already closed as a code mechanical-efficiency requirement |
| Fan total electrical efficiency | Blocked | Exact fan duty-point efficiency + numerical motor efficiency + VFD/transmission efficiency, or certified total input power at the duty point |

### Immediate next action

Obtain or nominate the exact chiller and fan selections. Required minimum fields are:

- chiller manufacturer/model, cooling type, compressor type, nominal capacity, refrigerant, leaving/entering chilled-water temperatures, outdoor design dry-bulb, full-load input power/COP and part-load performance;
- fan manufacturer/model, fan type, airflow, total/static pressure, speed, shaft power, fan total/static efficiency, motor rated kW/poles/IE class and efficiency, and VFD/transmission efficiency if present.

Until those fields are supported, the final equipment energy ranking remains deliberately fail-closed.

---

## Update 11 - 2026-08-29 - Archive.zip guideline evidence verified

### Input reviewed

Eight substantive PDFs in `Archive.zip` were extracted, text-screened and visually checked at the relevant pages:

1. VHHSBA HTG-2020-004, May 2020;
2. SCCM 2024 Guidelines on Adult ICU Design, published March 2025;
3. Saran et al. 2020 ICU HVAC review;
4. SHTM 03-01 Part A, Version 2, February 2014, archived;
5. HTM 03-01 Part A, 2021;
6. FGI 2022 Major Additions and Revisions extract;
7. ASHRAE Addendum h to Standard 170-2021;
8. HBN 04-02, 2013.

### Requirements closed or strengthened

- HBN 04-02 §4.14: minimum bed space 25.5 m².
- HBN 04-02 §4.17: 3 m ceiling height recommended in bed areas.
- HTM 03-01 Part A 2021 Table 3: critical-care individual room/open bay design factors directly verified.
- HTM Appendix 2: the separate +10 Pa summary row directly verified, confirming the +5/+10 Pa internal inconsistency.
- Historical SHTM 2014 Table A1 row retained with an explicit archived status.
- Victorian HTG-2020-004 §4.172 retained as supplemental Australian primary evidence only.

### False closures prevented

- ASHRAE Addendum h does not contain the inpatient critical-care Table 7-1 row or §6.4 filter-bank requirements.
- The FGI major-revisions extract does not contain the adult ICU area clause.
- The SCCM adult ICU design guideline gives neither a numerical room area nor numerical HVAC requirements.
- The Saran ICU HVAC article is a secondary comparison and cannot replace the named primary standards.
- No DIN 2018, NBC 2016 Part 8, CSA, AusHFG Part E, or AS 1668.2 source is present in the archive.

### Locked consequence

Only the verified direct clauses may populate the guideline comparison. Unsupported cells remain pending or absent. No secondary, archived, alternative-jurisdiction, or wrong-scope source may be promoted into a current primary-standard input.

---

## Update 12 - 2026-08-29 - Geometry, FOA, filters and thermal-state interpretation corrected

Direct visual inspection of the AusHFG 1BR-ICU Room Data Sheet, issue 12.11.2025, Revision 2, verified the 25.00 m² area, 3.0 m height and listed occupancy. The gross geometric volume is 75.0 m³; the base occupancy total is 3-5 and the maximum listed total is 11. `Steady` is not source language.

The same visual inspection showed that the HEPA checkbox is unselected. The room sheet cannot be cited as a HEPA requirement; only general air conditioning is selected. The Victorian HTG-2020-004 §4.172 remote-HEPA provision remains a separate jurisdiction-specific requirement.

The outdoor-air fraction rule is now source-scoped. The 2/6 ACH pair implies 33.3% only for ASHRAE/ISCCM at their minimum total airflow. A 20% fraction at 10 ACH is valid only in a parametric ASHRAE/ISCCM case retaining the 2 outdoor ACH floor; it is not imported into the UK rows. HTM/SHTM outdoor fraction remains undefined by their critical-care rows, while Victoria is fixed at 50%.

Temperature and RH guideline bands are locked as room conditions. Supply state is derived from room sensible and moisture balances or supplied as a separately sourced experimental/design boundary. FOA changes mixed-air state and conditioning duty; it does not automatically change the final supply state when room loads, total supply flow and room targets are fixed.
