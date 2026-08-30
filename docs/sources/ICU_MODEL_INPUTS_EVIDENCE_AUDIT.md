# ICU model inputs — primary-source evidence audit

**Audit date:** 2026-08-30  
**Audited file:** `ICU_MODEL_INPUTS.md`  
**Scope:** single-bed adult ICU room, ventilation, indoor-air contaminants, CO₂ source terms, and energy-model inputs  
**Evidence rule:** no assumed, analogous, proxy, averaged-across-sources, or placeholder value is admitted as source data.

The uploaded master has **not** been overwritten. This file identifies what is directly supported, what must be corrected, and what remains blocked.

## 1. Audit verdict

The present master is **not yet a source-clean model input file**. It contains valid source data, transparent arithmetic, researcher-defined geometry and control variables, conditional model hypotheses, and several unsupported or misinterpreted values under one “confirmed inputs” heading. Those categories must be separated before simulation results are reported as evidence-based.

The main corrections are:

1. HTM 03-01:2021 does contain minimum fresh-air provisions. The UK outdoor-air input is therefore not undefined and cannot approach zero in a compliant recirculating design.
2. A Government of India guideline from March 2022 directly supports the previously unnamed Indian case of 10–12 total air changes per hour and 4–5 fresh-air changes per hour.
3. The ASHRAE 170-2025 critical-care row and §6.4 filtration topology are not present in the supplied ASHRAE file. All 2025 ASHRAE values and downstream calculations that rely on them remain blocked.
4. The pollutant “clean/moderate/India high/event tail” table is not a direct transcription of the cited studies. Several entries are misassigned or invented groupings and must be withdrawn.
5. The CO₂ generation values are cohort or demographic-specific values, not generic patient, staff, or visitor factors. Existing CO₂ results also depend on an undocumented ventilator exhaust path, occupant composition/activity, and gas-state conversion.
6. Code-minimum chiller/fan entries do not establish actual equipment performance. Absolute energy, and some relative-energy claims, remain blocked.

## 2. Admissibility classes used in this audit

| Status | Meaning |
|---|---|
| **Accepted source datum** | Directly stated in an identified primary or official document, with edition/year and locator. |
| **Derived** | Arithmetic only, using accepted source data and an explicitly identified researcher-defined geometry or scenario. It is not presented as a quoted requirement. |
| **Researcher-defined** | A geometry, operating point, model boundary, or sensitivity domain chosen by the researcher. It may be used only when labelled as such; it is not evidence about an ICU or a standard. |
| **Blocked** | The exact primary/official evidence or site/equipment datum is unavailable. No substitute is inserted. |
| **Withdraw** | A current input or result is unsupported, incorrectly attributed, or depends on an open prerequisite. |

## 3. Directly verified room and ventilation data

### 3.1 Room geometry and occupancy

| Document, edition/year, locator | Directly stated | Status and use |
|---|---|---|
| **Australasian Health Infrastructure Alliance, _Australasian Health Facility Guidelines: Room Data Sheet — 1 Bed Room – Intensive Care_, room code 1BR-ICU, Revision 2, issue date 12.11.2025, p. 1** | Briefed area **25.00 m²**; ceiling height **3.0 m**; occupancy **1 patient, 1–2 visitors, 1–2 staff, with 4–6 additional staff as required**; 24-hour operation; “AIRCONDITIONING: general” selected. | **Accepted source data.** The title establishes one bed. The source does not call 3–5 occupants “steady” or the additional staff a timed “surge”; those temporal labels require an ICU SOP or measured occupancy record. Unselected HEPA/positive/negative-pressure checkboxes show only that the room data sheet does not select those services; they do not establish that no other governing document requires them. |
| **NHS England, _Health Building Note 04-02: Critical care units — Planning and design_, 2013, §4.14 and §4.17, printed p. 9** | Minimum bed space **25.5 m²**; **3.0 m** ceiling height is recommended in bed areas. | **Accepted corroborating source data.** It is a separate UK requirement and must not be merged with the 25.00 m² AusHFG room sheet. [Official publication](https://www.england.nhs.uk/publication/critical-care-units-planning-and-design-hbn-04-02/) |

For the AusHFG room sheet, **75.0 m³** is a transparent geometric calculation (`25.00 m² × 3.0 m`). It is a gross geometric volume, not a measured effective mixing volume. Similarly, **3–5 occupants** and a maximum arithmetic count of **11** follow from the listed occupancy components, but no source establishes how long any count persists.

### 3.2 Ventilation and environmental requirements

Each row below is kept source-specific. Values from different editions or jurisdictions are not averaged or reconciled by substitution.

| Document, edition/year, exact locator | Space/row | Directly stated requirements |
|---|---|---|
| **NHS England, _Health Technical Memorandum 03-01: Specialised ventilation for healthcare premises — Part A: The concept, design, specification, installation and acceptance testing of healthcare ventilation systems_, 2021, Table 3, printed p. 64** | “Level 2 or 3 critical care individual room/open bays” | Supply/cascade-out system; **≥10 air changes/h**; **+5 Pa** to the general area; room **20–25 °C**; floating RH with **60% maximum**; **EPA10 final filter**. [Official publication and PDF](https://www.england.nhs.uk/publication/specialised-ventilation-for-healthcare-buildings/) |
| **Same document, Appendix 2, printed p. 147** | “Critical care areas (Level 2 and 3 care)” | System designation **S**; **10 air changes/h**; **+10 Pa**; supply-filter designation **SUP1**; **35 dB(A)**. Temperature and RH are not stated in this row. The row notes that an isolation room may use a different pressure arrangement. |
| **Same document, §8.6, printed p. 41; see also §9.120** | General fresh-air sizing provisions applicable when sizing the occupied space/system | Fresh air must be at least **10 L/s per person**. Where air is recirculated, the minimum fresh air is **20%**, or the applicable regulatory/person-based requirement, whichever is greater. This closes the master’s “HTM general fresh-air clause” gap. |
| **NHS Scotland, _Scottish Health Technical Memorandum 03-01 Part A: Design and validation_, Version 2, February 2014 (archived), Appendix 1, Table A1, printed p. 139** | “Critical Care Areas” | System **S**; **10 air changes/h**; **+10 Pa**; **F7 supply filter**; **30 dB(A)**; **18–25 °C**. RH is not stated in this row. [Official archive](https://www.nss.nhs.scot/publications/ventilation-for-healthcare-premises-shtm-03-01-and-shtm-2025-archived/) |
| **Same document, §2.37, printed p. 26** | Recirculation provision | If recirculation is considered, the minimum fresh-air volume required by the Building (Scotland) Regulations is to be provided; the document states this as **20%** at that edition date. This is a lower bound for a recirculating design, not proof that the critical-care row requires exactly 20% or 100% outdoor air. |
| **N. Rungta et al., _Indian Society of Critical Care Medicine Experts Committee Consensus Statement on ICU Planning and Designing, 2020_, Indian Journal of Critical Care Medicine 24(Suppl 1):S43–S60, “Environmental Requirements” → “Heating, Ventilation and Air-conditioning (HVAC) system of ICU”** | ICU HVAC | Minimum **6 total air changes/h**, including **2 outside-air changes/h**; airflow from clean to less-clean areas; central air conditioning/recirculation through appropriate filters; air filtration with **99% efficiency down to 5 µm**; adjustable **16–25 °C** for enclosed patient modules. The text does not provide a numerical pressure differential for a general ICU. [Primary full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC7085818/) |
| **Ministry of Health & Family Welfare, Government of India, _Guidelines for High Dependency Unit (HDU) & Intensive Care Unit (ICU)_, March 2022, “Physical Infrastructure” → “ICU and HDU beds,” item 6, printed p. 24** | ICU/HDU HVAC | **10–12 air changes/h**, including **4–5 fresh-air changes/h**; AHU with **fine filters** and continuous air circulation; room **23 ± 2 °C** and **45–65% RH**. “Fine filters” is not a fractional-efficiency curve or a recognized product selection by itself. [Official NHSRC/MoHFW source page](https://nhsrcindia.org/guidelines-critical-care-and-support-services-under-iphs-2022) |
| **Same document, Annexure III, “Quality Checklist for HDU/ICU,” item 3.2, printed p. 47** | HDU/ICU quality check | Positive pressure, **45–65% RH**, and **23 ± 2 °C** are to be maintained with the AHU and recorded. |
| **Victorian Health and Human Services Building Authority, _Engineering guidelines for healthcare facilities: Volume 4 — Heating, ventilation and air conditioning_, HTG-2020-004, May 2020, §4.172, printed p. 34** | “ICU and CCU” | AHUs serving the ICU pressurised patient zone incorporate **remote HEPA filtration outside the ICU**, **50% outside air**, heat recovery, and positive air movement from bed areas toward adjoining circulation. §4.173 sends other conditions to Reference Table 1. [Official publication](https://www.vhba.vic.gov.au/guideline/engineering-guidelines-healthcare-facilities) |

### 3.3 Corrected UK outdoor-air calculation

This subsection contains arithmetic, not an additional standard requirement. It uses the accepted 2021 HTM provisions, the AusHFG-derived gross volume of 75.0 m³, and the room-sheet occupancy counts.

At 10 air changes/h:

`Q_supply = 10 × 75.0 = 750 m³/h`

For a recirculating HTM system, the lower bound is:

`Q_OA,min = max(0.20 × 750, 10 L/s/person × N × 3.6)`

| Occupancy count used | 20% minimum | 10 L/s/person | Controlling minimum outdoor air | Derived minimum outdoor fraction |
|---:|---:|---:|---:|---:|
| 3 | 150 m³/h | 108 m³/h | **150 m³/h = 2.00 ACH** | **0.200** |
| 5 | 150 m³/h | 180 m³/h | **180 m³/h = 2.40 ACH** | **0.240** |
| 11 | 150 m³/h | 396 m³/h | **396 m³/h = 5.28 ACH** | **0.528** |

Therefore the current master’s UK cases at 5% and 10% outdoor air are noncompliant with the cited 2021 HTM provisions. A 20% outdoor-air case is compliant at three occupants but not at five or eleven occupants under the person-based requirement. The actual outdoor fraction remains a design outcome at or above the controlling minimum; the source does not set it to an arbitrary sweep point.

For SHTM 03-01:2014, the verified general recirculation provision supplies a 20% minimum, but the currently held text does not establish the same 10 L/s/person rule. The English and Scottish documents must not be combined.

### 3.4 What the available Australia sources do and do not close

- **Australasian Health Facility Guidelines, Part E — Building Services and Environmental Design, Revision 5.0, 1 March 2016:** the official document is a general services overview and was retired in 2018 because service requirements vary by jurisdiction. It does not provide the requested ICU ventilation comparison row. [Official Part E page](https://healthfacilityguidelines.com.au/part/part-e-building-services-and-environmental-design)
- **AS 1668.2:2024, _The use of ventilation and airconditioning in buildings, Part 2: Mechanical ventilation in buildings_:** the official catalogue confirms the 2024 edition supersedes 2012, but the normative healthcare/ICU table is not present in the supplied evidence. Exact ICU values remain blocked. [Official catalogue](https://store.standards.org.au/product/as-1668-2-2024)
- **Victoria HTG-2020-004:** §4.172 provides the accepted 50% outside-air and remote-HEPA statements above. The accompanying **Reference Table 1 and 2**, dated 30 May 2020, is still required for the remaining ICU conditions referenced by §4.173. No air-change value has been inferred from it.

## 4. Directly verified pollutant measurements

These are study-specific observations. They are not regulatory limits, generic ICU regimes, source emission factors, or automatically transferable boundary conditions.

| Primary study, year, locator | Directly supported observation | Required scope label |
|---|---|---|
| **K.-Y. Kim, Y.-S. Kim and D. Kim, “Distribution Characteristics of Airborne Bacteria and Fungi in the General Hospitals of Korea,” _Industrial Health_ 48(2):236–243, 2010, Table 2, p. 238; Table 3, p. 239** | ICU bacteria: **202 CFU/m³ total**, **142 CFU/m³ respirable**. ICU fungi: **65 CFU/m³ total**, **47 CFU/m³ respirable**. | Five Seoul hospitals; ICU row; six-stage Andersen sampling. “Respirable” is stages 3–6. [Primary article](https://www.jstage.jst.go.jp/article/indhealth/48/2/48_2_236/_pdf/-char/en) |
| **Same study, “Materials and Methods,” p. 237** | Andersen aerodynamic stages: **>7, 4.7–7, 3.3–4.7, 2.1–3.3, 1.1–2.1, and 0.65–1.1 µm**; sampler flow **28.3 L/min**; 25 samples per site. | This is a viable aerodynamic size structure. It is not a PM₂.₅/PM₁₀ mass distribution. |
| **G. Lokeshwari, G. Balajee and T. Premalatha, “Aero-surveillance of Various Units in a Quaternary Care Hospital Based on Seasonal Perspective — An Observational Study,” _International Journal of Current Microbiology and Applied Sciences_ 9(9):2376–2389, 2020, Table 1, p. 2383** | Grouped ICU bacterial concentration: **93.85 ± 31.57 CFU/m³**. | Chennai quaternary-care hospital; ICU group comprises MICU/PICU/SICU/NICU/LMICU/CCU; active sampling during routine working hours. **151 ± 138.8 CFU/m³ belongs to a separate PICU isolation-room category and is not the upper end of an ICU range.** [Primary article](https://www.ijcmas.com/9-9-2020/G.%20Lokeshwari,%20et%20al.pdf) |
| **Same study, Table 2, p. 2384** | Grouped ICU fungal concentration: **2.62 CFU/m³**. | Same grouped ICU and sampling context. It must not be relabelled as a general “low-single-digits” ICU regime. |
| **C.-S. Tang, F.-F. Chung, M.-C. Lin and G.-H. Wan, “Impact of patient visiting activities on indoor climate in a medical intensive care unit: A 1-year longitudinal study,” _American Journal of Infection Control_ 37:183–188, 2009, Results, p. 184** | During the one-year study: room **21.2–25.8 °C**, **58–74% RH**, **828–1570 ppm CO₂**, and **4.2–43.7 µg/m³ PM₁₀**. | Four-bed medical ICU in northern Taiwan; weekly sampling before, during and after visiting periods. Fine particles were defined as **PM₂ (<2 µm), not PM₂.₅**. [Primary article](https://doi.org/10.1016/j.ajic.2008.06.018) |
| **Same study, Results and figures, pp. 184–187** | After visitation, RH, CO₂, PM₁₀, coarse/fine particles and fungi increased significantly; the bacterial change was not statistically significant. Reported high bacterial/fungal observations are month-specific measurements, not a universal “event-tail” range. | Exact before/after numerical values are plotted; they should not be converted into model inputs by unsourced visual digitization. |
| **R. Taushiba et al., “Assessment of indoor air quality and their inter-association in hospitals of northern India — a cross-sectional study,” _Air Quality, Atmosphere & Health_ 16:1023–1036, 2023** | The study reports particulate, metal and microbial measurements. It does **not** report CO₂. | Lucknow hospitals, February–April 2022. It cannot support the master’s “1822–2258 ppm (Aligarh)” CO₂ entry. Hospital-level maxima also cannot be relabelled as ICU values without a named ICU row. [Publisher record](https://link.springer.com/article/10.1007/s11869-023-01321-4) |

### 4.1 Pollutant entries to withdraw

The following current values are not admissible as written:

| Current master entry | Audit disposition |
|---|---|
| “Clean,” “Moderate,” “India high,” and “Event tail” regimes | **Withdraw.** These are analyst-created categories, not classifications or rows stated by the cited primary studies. Retain source-specific measurements only. |
| CO₂ **1822–2258 ppm (Aligarh)** attributed to Taushiba et al. | **Withdraw.** That study did not measure CO₂ and was conducted in Lucknow, not Aligarh. A different primary source with a precise room/ward and locator is required. |
| PM₂.₅ **20–35 µg/m³** and PM₁₀ **10–60 µg/m³** attributed generally to Tang | **Withdraw.** Tang reports PM₁₀ 4.2–43.7 µg/m³ and uses a PM₂ definition for fine particles. |
| Bacteria **94–151 CFU/m³** as an Indian ICU range | **Withdraw.** The accepted grouped-ICU result is 93.85 ± 31.57 CFU/m³; the 151 value belongs to a separate PICU isolation-room category. |
| Tang bacterial/fungal **>1000 to ~7236/~11654 CFU/m³** as “event tails” | **Withdraw as a generic range.** The high values are source-, month-, and study-specific observations, not a validated event-tail distribution. |
| TVOC concentration | **Blocked.** No direct ICU TVOC concentration source has been verified. |
| Any ICU-specific “allowable” pollutant limit | **Blocked.** No such limit is present in the inspected evidence. This is limited to the inspected evidence and is not a claim that no limit exists anywhere. |

## 5. CO₂ generation evidence and limits

| Primary source, year, locator | Directly reported value | Admissible interpretation |
|---|---|---|
| **A. Kagan et al., “Validation of carbon dioxide production (VCO₂) as a tool to calculate resting energy expenditure in mechanically ventilated critically ill patients: a retrospective observational study,” _Critical Care_ 22:186, 2018, Results** | Six-hour-block mean VCO₂ **244.5 ± 85.9 mL/min**; arithmetic unit conversion **4.075 × 10⁻⁶ ± 1.432 × 10⁻⁶ m³/s** at the instrument’s reporting state. | Cohort measurement in mechanically ventilated critically ill patients, not a universal patient emission factor. [Primary article](https://link.springer.com/article/10.1186/s13054-018-2108-8) |
| **M. L. Rousing et al., “Energy expenditure in critically ill patients estimated by population-based equations, indirect calorimetry and CO₂-based indirect calorimetry,” _Annals of Intensive Care_ 6:16, 2016, Results** | Mean VCO₂ **273 ± 63 mL/min**; arithmetic unit conversion **4.550 × 10⁻⁶ ± 1.050 × 10⁻⁶ m³/s** at the instrument’s reporting state. | Cohort mean, not a universal patient factor. A numerical pressure basis was not established from the held source, so it must not be pressure-harmonised by assumption. [Primary full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC4759444/) |
| **A. Persily and L. de Jonge, “Carbon dioxide generation rates for building occupants,” _Indoor Air_ 27(5):868–879, 2017, Equation 9 and Table 4, printed p. 875** | Male age 21–<30 row at 1.0/1.2/1.4/1.6 met: **0.0039/0.0048/0.0056/0.0064 L/s** at **273 K and 101 kPa**. | Direct table transcription for that sex/age/activity case only. The paper warns that mean-body-mass values are group approximations and generally inaccurate for a single individual. It is not a generic nurse/doctor/visitor/cleaner rate. [Primary paper](https://onlinelibrary.wiley.com/doi/pdf/10.1111/ina.12383) |

Before any patient VCO₂ value is entered into a room balance, site documentation must establish whether ventilator expiratory gas is released into the room or removed by an exhaust/scavenging connection. Before any non-patient value is entered, the staff/visitor sex, age and activity composition must be observed or explicitly defined as a researcher scenario. A single Persily row cannot be used for all people.

The master’s conversion to **297.15 K and 101325 Pa** is a researcher-selected evaluation state, not a measured ICU condition. The resulting “+8.5–8.8%” adjustment and all CO₂ results using it must not be presented as source data. A reference-state-independent molar balance is preferable until actual room temperature and pressure are known.

### 5.1 CO₂ inversion

The exact discrete inversion in the master is a mathematical rearrangement of a constant-coefficient, well-mixed mass balance. A noiseless synthetic round trip tests the implementation; it does not validate occupancy reconstruction in an ICU.

Use on measured data remains **blocked** until all of the following are supplied for the same intervals:

- measured ICU CO₂ trace and sensor metadata;
- outdoor CO₂ trace or measured boundary value;
- actual outdoor-air flow or a time-resolved verified ventilation state;
- patient expiratory discharge path;
- a defensible mapping from non-patient CO₂ source strength to individual people, if headcount rather than source strength is required.

An ICU SOP can provide event timing for a schedule route but cannot be replaced by a generic office or hospital schedule. The CO₂-derived temporal shape must not be transferred to PM, bacteria, fungi or TVOC without direct pollutant-specific ICU evidence.

## 6. Filtration, deposition and energy — admissible status

### 6.1 Filters

The verified documents provide descriptors—MERV-14 remains unverified here; EPA10, SUP1, F7, “99% down to 5 µm,” “fine filters,” and remote HEPA are source-specific descriptors. None supplies the product fractional-efficiency curve `η(dp)`, clean pressure drop at the project duty point, or loading curve required by the size-resolved model.

Therefore:

- no filter class may be converted into a fractional-efficiency curve by assumption;
- MERV E1/E2/E3 bands are not particle-state bins;
- a lower project face velocity does not, by itself, establish a numerical efficiency or pressure drop; product/manufacturer data at the operating point are required;
- SUP1 is a supply-air designation in the HTM appendix, not a product efficiency curve;
- the topology and affected airstream for the claimed ASHRAE 170-2025 MERV-14 requirement remain blocked pending §6.4 and the complete 2025 space table.

### 6.2 Deposition and PM size distribution

`k_dep` is **blocked** under the study’s no-proxy rule. Generic non-ICU aerosol literature cannot be inserted as an ICU-room deposition input merely because deposition is a general physical process. A usable input requires a directly applicable deposition formulation plus the actual room surface-to-volume ratio, relevant surface/material conditions, airflow/turbulence regime, and compatible particle-size distribution.

Kim’s Andersen bins provide an aerodynamic size structure for viable bacteria and fungi only. They do not close the PM₂.₅/PM₁₀ mass-distribution gap. ICU PM `dM/dlogDp` or an equivalent directly measured size distribution remains blocked.

### 6.3 Energy

**Bureau of Energy Efficiency, _Energy Conservation Building Code 2017_, §9.4.2.8, Table 9-5** states minimum efficiencies for standard-design chillers, including air-cooled chiller COP/IPLV entries. These are code minima, not the actual efficiency of the ICU plant. [Official BEE PDF](https://beeindia.gov.in/WriteReadData/L45218/1734417634.pdf)

The current ECSBC 2024 row “65% (IE3) / 70% (IE4) / 75% (IE4)” must not be used as written: fan mechanical efficiency and motor IE efficiency class are different quantities. The exact official ECSBC tables must be checked from the official edition, and actual fan/motor/chiller performance must come from selected equipment or measured plant data.

The following remain blocked for absolute energy:

- system pressure drop at each duty point and filter loading state;
- fan, motor and drive efficiency maps;
- chiller/heat-pump performance as a function of load and outdoor state;
- cooling-coil, dehumidification and reheat configuration;
- ICU sensible and latent loads;
- hourly outdoor dry-bulb, humidity and pollutant boundary files for each named city/zone.

The current **4.63× fan-power** result is conditional on the cube law for the same system curve and efficiency. The current **5× outdoor-air-conditioning** result also used an invalid UK outdoor-air treatment. Both must be withdrawn as evidence-backed findings. “Zero load” and a “plausible high load” may be mathematical test cases, but they are not sourced ICU inputs and cannot replace measured or design-load data under the stated rule.

## 7. Standards and clauses still blocked

No numerical requirement is entered for these items because the exact requested edition and normative row were not available in the supplied evidence.

| Country/topic | Exact document required | What is missing and therefore blocked |
|---|---|---|
| United States — ventilation | **ANSI/ASHRAE/ASHE Standard 170-2025, _Ventilation of Health Care Facilities_, Table 7-1 critical-care patient care station row, plus §6.4 and current errata/addenda** | Complete row: pressure relationship, minimum outdoor ACH, minimum total ACH, all-air-exhausted-outdoors, room-unit recirculation, RH and temperature; filtration requirement and airstream topology. The supplied file is only **Addendum h to Standard 170-2021**, approved 30 September 2022, and contains outpatient revisions rather than the inpatient critical-care row. [Official ASHRAE read-only page](https://www.ashrae.org/technical-resources/standards-and-guidelines/read-only-versions-of-ashrae-standards) |
| United States — area | **FGI, _Guidelines for Design and Construction of Hospitals_, 2022 edition, §2.2-2.6.2.2 adult critical-care patient room** | Exact 2022 area clause. The supplied “Major Additions and Revisions” summary is not the complete 2022 guideline and does not contain the adult ICU area clause. A 2018 value must not be carried forward to 2022 without the 2022 text. |
| Australia | **AS 1668.2:2024** or **AS 1668.2:2012**, exact healthcare/ICU entry | ICU ventilation row and all associated notes. AusHFG Part E does not close this item. |
| Victoria | **HTG-2020-004, Reference Table 1 and 2, 30 May 2020** | Exact ICU air-change, temperature, RH and any other conditions referenced by §4.173. |
| India — national building code | **SP 7:2016, National Building Code of India 2016, Volume 2, Part 8 Building Services, Section 3 Air Conditioning, Heating and Mechanical Ventilation** | Exact normative ICU row(s) and notes. The official BIS page confirms the edition/part structure but the required text was not supplied. [Official BIS page](https://www.bis.gov.in/standards/national-building-code/?lang=en) |
| India — accreditation | **NABH, _Accreditation Standards for Hospitals_, Sixth Edition, January 2025**, complete relevant clauses | The full edition was not available for audit. The absence of HVAC values from one cited COP.9 excerpt cannot prove absence throughout the edition. |
| Germany | **DIN 1946-4:2018-09, _Ventilation and air conditioning — Part 4: Ventilation in buildings and rooms of health care_, Table 1 and the intensive-care classification text; plus DIN 1946-4/A1:2025-11 where applicable** | Exact room class assigned to intensive care and all associated table requirements. The official catalogue confirms the edition, not the paywalled normative row. [Official DIN catalogue](https://www.dinmedia.de/en/standard/din-1946-4/294438653) |
| Canada | **CSA Z317.2**, edition named, ICU row; **CSA Z8000**, edition named, adult critical-care room-area clause | Exact ventilation row and exact room area. No older edition is substituted. |
| France | **NF S 90-351**, edition named, normative critical-care filtration/air-treatment clauses | Primary AFNOR text. Secondary explanatory material is inadmissible. |
| Activity classification | **ISO 8996**, edition named, exact activity table | Lying/resting, light standing work and walking values. Persily’s activity examples must not be relabelled as ISO 8996 values. |

The ASHRAE official title-and-scope register identifies Standard 170-2025 as the current published edition superseding 170-2021, but the title record is not a substitute for the normative row. [ASHRAE title and scope register](https://www.ashrae.org/technical-resources/standards-and-guidelines/titles-purposes-and-scopes)

## 8. Required revisions to the uploaded master

| Master section | Required action |
|---|---|
| §0.1 gap 7 | Mark **closed** by HTM 03-01:2021 §8.6 and §9.120. |
| §0.2 “Other Indian documents” | Add the Government of India March 2022 HDU/ICU guideline as its own scenario; do not merge it with ISCCM 2020. |
| §§2, 3, 4, 4.1 | Remove ASHRAE 170-2025 values until the complete 2025 Table 7-1 row and §6.4 are obtained. Replace “UK outdoor air undefined/free” with the source-specific HTM and SHTM minimum provisions. |
| §4 G7 | Replace “none” with “not selected in this room data sheet”; do not infer AusHFG-wide absence of requirements. |
| §§5–6 | Recalculate any common temperature/RH statement without the blocked ASHRAE row. Keep space conditions distinct from supply-air conditions. Describe the two HTM rows as an unreconciled difference, not proven internal inconsistency. |
| §§7 and 7.1 | Keep Kagan, Rousing and Persily source-specific. Remove generic staff/visitor use and the unsourced room-state conversion from confirmed inputs. |
| §8 | Change deposition from “not blocked” to **blocked** under the no-proxy rule. |
| §§9–10 | Separate code-minimum compliance values from actual plant performance. Remove zero/plausible-high loads from evidence inputs. |
| §§11.3–11.4 | Delete the invented regime table; replace it with the source-specific measurements in §4 of this audit. Keep TVOC and allowable limits blocked. |
| §12 A5–A6 | Label balanced exhaust/no infiltration and perfect mixing as model hypotheses requiring site validation, not confirmed data. |
| §§13 and 13.1 | Remove “Tier 1 — nothing blocked.” CO₂ and energy prerequisites remain open. |
| §14 | Retain the inversion only as unvalidated mathematics. Do not report headcount without heterogeneous source-rate information. |
| §§15–16 | Withdraw current CO₂, UK outdoor-air, response-time, fan-energy and outdoor-air-energy results until corrected inputs are available. Do not claim “four of eight guidelines” are complete/incomplete until every named edition has been checked. |

## 9. Fail-closed model status

The evidence currently permits a **source register and constrained scenario definitions**, but not the claimed complete Stage A simulation.

Directly usable now, with source labels retained:

- AusHFG room-sheet geometry and occupancy composition;
- HBN 04-02:2013 UK bed-space and ceiling-height data;
- HTM 03-01:2021 critical-care rows and general minimum-fresh-air rules;
- SHTM 03-01:2014 archived critical-care row and recirculation minimum;
- ISCCM 2020 ICU HVAC requirements;
- Government of India March 2022 HDU/ICU HVAC requirements;
- Victoria HTG-2020-004 §4.172 values only;
- source-specific Kim, Lokeshwari and Tang measurements;
- source-specific Kagan, Rousing and Persily CO₂-generation data, subject to their stated applicability limits.

Blocked quantities remain absent. They are not replaced with assumed, proxy, analogous or placeholder values.
