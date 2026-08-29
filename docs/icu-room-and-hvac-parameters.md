# ICU Room Geometry and HVAC Parameters for Simulation

Reference parameter set for modelling a single-bed adult ICU room coupled to an
HVAC system. Compiled from national health facility guidelines and ventilation
standards. Every number below carries its source so the model can be defended.

> **Verification note.** The Australasian room data sheet (`1BR-ICU`, Rev 2,
> 12.11.2025) was read directly and is quoted exactly. The other standards
> (ASHRAE 170, FGI, HBN/HTM, ISCCM/NABH) could not be downloaded in full from
> this environment — those figures come from published secondary sources and
> should be checked against the purchased standard before being used in a
> submitted paper or a real design.

---

## 1. Recommended base-case room

| Quantity | Value | Basis |
|---|---|---|
| Length (L) | 5.0 m | chosen to give the AusHFG briefed area |
| Width (B) | 5.0 m | chosen to give the AusHFG briefed area |
| Height (H) | 3.0 m | AusHFG 1BR-ICU ceiling height; HBN 04-02 recommends 3 m in bed areas |
| Floor area | 25.0 m² | AusHFG 1BR-ICU "Briefed Area 25.00 m²" |
| Volume V | **75 m³** | 5.0 x 5.0 x 3.0 |
| Beds | 1 | single-bed rooms are the global norm for critical care |
| Occupancy (steady) | 3 persons: 1 patient + 1 nurse + 1 visitor | AusHFG occupancy line |
| Occupancy (surge) | up to 8-9 persons | AusHFG: "1 patient; 1-2 visitors; 1-2 staff (with 4-6 additional staff as required)" |

A **26 m² variant (5.2 x 5.0 x 3.0 = 78 m³)** also satisfies the UK minimum, if
you want one geometry that clears every guideline at once. The difference is
~4 % in volume and will not change conclusions.

Do not model a shared multi-bed bay unless that is the research question —
current guidance in Australia, the UK and the US is single-patient rooms.

### Room-size requirements by country

| Guideline | Country | Minimum single ICU bed space |
|---|---|---|
| AusHFG Room Data Sheet 1BR-ICU, Rev 2 (2025) | AU / NZ | 25.00 m² briefed area, 3.0 m ceiling |
| HBN 04-02 *Critical care units* | UK (NHS) | 26 m² minimum bed space; 3 m ceiling recommended for pendants and hoists |
| FGI *Guidelines for Design and Construction of Hospitals* (2018, 2022) | US | 200 ft² (18.6 m²) clear floor area per patient space, 13 ft (3.96 m) headwall width, new construction |
| SCCM ICU design guidelines | US | 8-12 beds per unit / pod is the recommended unit size |

The AusHFG 25 m² is a *briefed* area (the whole room). FGI's 200 ft² is *clear
floor area* — usable floor after fixed joinery — so the two are closer than they
look. 25-26 m² is the honest global consensus for a modern single ICU room.

---

## 2. Ventilation rates

At V = 75 m³:

| ACH | Total supply | | Notes |
|---|---|---|---|
| 6 | 450 m³/h | 125 L/s | ASHRAE 170 minimum, US baseline |
| 10 | 750 m³/h | 208 L/s | UK SHTM/HTM 03-01 critical care |
| 12 | 900 m³/h | 250 L/s | India (ISCCM/NABH); also the AII isolation rate |
| 2 (outdoor) | 150 m³/h | 41.7 L/s | ASHRAE 170 minimum outdoor air, ~14 L/s per person at 3 occupants |

**Recommended simulation matrix:** base case **6 ACH**, sensitivity runs at
**10** and **12 ACH**, plus a **12 ACH negative-pressure isolation mode**.

### By standard

| Standard | Total ACH | Outdoor ACH | Pressure | T | RH |
|---|---|---|---|---|---|
| ANSI/ASHRAE/ASHE 170, "Critical and intensive care" | 6 min | 2 min | NR (no requirement) | 21-24 °C (70-75 °F) | 30-60 % |
| ASHRAE 170, airborne infection isolation (AII) | 12 | 2 | negative | — | — |
| ASHRAE 170, protective environment (PE) | 12 | 2 | positive, HEPA supply | — | — |
| SHTM/HTM 03-01 Appendix 1, critical care | 10 | — | balanced / positive | — | — |
| ISCCM / NABH (India) | >= 12 | often 100 % OA specified | positive; negative for AII | — | — |
| AusHFG 1BR-ICU | per AS 1668.2 (not stated on the sheet) | — | S-class (equal), P-class (positive) or N-class (negative) selectable | — | — |

Note AS 1668.2:2024 raised the isolation-room rate from 6 to 12 ACH.

---

## 3. Outdoor-air fraction

ASHRAE 170 sets a **floor of 2 outdoor ACH**, not a fraction. The fraction falls
out of whatever total you pick:

| Total ACH | Minimum OA fraction (2 ACH OA) |
|---|---|
| 6 | 33 % |
| 10 | 20 % |
| 12 | 17 % |

Real ICU air handlers commonly run **15-25 % outdoor air**, recirculating the
balance through the central filter banks. 100 % outdoor air is *not* required by
ASHRAE 170 or FGI and is uncommon in temperate climates on energy grounds,
though Indian guidance leans towards it.

**Model as 20 % outdoor air / 80 % recirculated** for the base case, and check
33 % (the ASHRAE floor at 6 ACH) and 100 % as bounds.

Two constraints that matter for a UV model:

- Room-level recirculating units (fan coils, induction units) are **not
  permitted** in critical care spaces — recirculation happens centrally at the
  AHU, so recirculated air is filtered before it returns.
- In-room devices (portable HEPA, upper-room GUV) may add *equivalent* air
  changes but **cannot be counted against the 2 ACH minimum outdoor air**.

---

## 4. Filtration

| Location | Filter | Equivalents |
|---|---|---|
| AHU filter bank 1 (pre-filter) | MERV 7-8 | ISO 16890 ePM10 50-65 %, EN 779 G4/M5 |
| AHU filter bank 2 (final, downstream of cooling coil) | MERV 14 | ISO 16890 ePM1 75-85 %, EN 779 F8/F9 |
| Terminal HEPA | H13/H14 (>= 99.95 % @ MPPS) | required for protective environment; optional for ICU |

ASHRAE 170 historically specified MERV 7 + MERV 14 for inpatient care spaces
(Table 6-4 in the 2008/2013/2017 editions). The 2021 edition removed Table 6-4
and moved minimum filtration into the space tables (7.1 inpatient, 8.1
outpatient, 9.1 residential); some secondary sources report MERV 13 as the final
filter for general inpatient rooms and ICUs, with MERV 14 permitted as an
alternative where a tertiary terminal HEPA is fitted. **Check the edition you are
citing.** For a simulation, MERV 14 is the safe assumption.

The AusHFG sheet explicitly lists `AIRCONDITIONING: HEPA filtered` as an
available service for 1BR-ICU, so a terminal-HEPA variant is defensible for an
Australian model.

Removal efficiency to use in a well-mixed model, for the recirculated fraction:

- MERV 14: ~0.80-0.90 for ~1 µm particles
- HEPA H13: ~0.9995

---

## 5. Airflow arrangement

- **Type:** central all-air ducted system (AHU per unit or per zone), constant
  volume, with terminal reheat for room-by-room temperature control. This is the
  standard ICU arrangement in ASHRAE 170, FGI, HTM 03-01 and AusHFG.
- **Supply:** ceiling diffusers over/near the bed, low-velocity and
  non-aspirating, sized to avoid draught on the patient.
- **Return/exhaust:** low-level wall grilles, typically two, on the opposite side
  to the supply, to establish a clean-to-dirty downward sweep across the bed.
- **Pressure:** ICU rooms are usually held slightly positive to the corridor
  (+2.5 to +15 Pa). The AusHFG sheet makes the room switchable between
  S-class (equal pressure), P-class (positive) and N-class (negative) — the
  N-class mode exhausts directly outdoors and is what you want for an
  airborne-isolation scenario.
- **Setpoints:** 21-24 °C, 30-60 % RH.

---

## 6. Coupling a UV term to this model

For a well-mixed single-zone box, the total first-order removal rate is

    k_total = ACH_outdoor + ACH_recirc * eta_filter + k_UV + k_deposition + k_decay   [1/h]

where `k_UV` is the equivalent air changes per hour delivered by the germicidal
system. With the base case above:

    V           = 75 m³
    ACH_total   = 6 /h      (450 m³/h)
    ACH_outdoor = 1.2 /h    at 20 % OA  (90 m³/h)
    ACH_recirc  = 4.8 /h    (360 m³/h), through MERV 14, eta ~ 0.85
    -> HVAC-equivalent clean air delivery ~ 1.2 + 4.8*0.85 = 5.3 /h

Upper-room GUV in a room of this size is typically credited with an additional
10-20 equivalent ACH, so the UV term will dominate the HVAC term — worth
stating explicitly when you report results. Keep `ACH_outdoor` pinned at or
above 2 ACH in any "code-compliant" scenario, since UV cannot substitute for it.

---

## 7. Sources

Uploaded / read directly:

- Australasian Health Infrastructure Alliance, *Australasian Health Facility
  Guidelines — Room Data Sheet, 1 Bed Room - Intensive Care (Room Code 1BR-ICU)*,
  Revision 2, issued 12 November 2025. https://healthfacilityguidelines.com.au/

Consulted via published secondary sources:

- ANSI/ASHRAE/ASHE Standard 170, *Ventilation of Health Care Facilities*
  (2008/2013/2017/2021 editions and addenda). https://www.ashrae.org/
- Facility Guidelines Institute, *Guidelines for Design and Construction of
  Hospitals*, 2018 and 2022 editions. https://fgiguidelines.org/
- NHS England, *Health Building Note 04-02: Critical care units*.
  https://www.england.nhs.uk/publication/critical-care-units-planning-and-design-hbn-04-02/
- NHS England, *Health Technical Memorandum 03-01: Specialised ventilation for
  healthcare premises*, Parts A and B; and NHS Scotland SHTM 03-01, Appendix 1.
  https://www.england.nhs.uk/publication/specialised-ventilation-for-healthcare-buildings/
- Saran S., Gurjar M., Baronia A., et al. "Heating, ventilation and air
  conditioning (HVAC) in intensive care unit." *Critical Care* 24, 194 (2020).
  https://doi.org/10.1186/s13054-020-02907-5
- CDC/HICPAC, *Guidelines for Environmental Infection Control in Health-Care
  Facilities* (2003, updated 2019), Appendix B — Air.
  https://www.cdc.gov/infection-control/hcp/environmental-control/appendix-b-air.html
- Society of Critical Care Medicine, *2024 Guidelines on Adult ICU Design*,
  *Critical Care Medicine* 53(3):e690-e700 (2025).
  https://doi.org/10.1097/CCM.0000000000006572
- Standards Australia, AS 1668.2 *The use of ventilation and airconditioning in
  buildings — Mechanical ventilation in buildings*, 2012 and 2024 editions.
- Victorian Health Building Authority, *Engineering Guidelines for Healthcare
  Facilities, Volume 4 — Heating, ventilation and air conditioning* (2020).
  https://www.vhba.vic.gov.au/guideline/engineering-guidelines-healthcare-facilities
- DIN 1946-4:2018-09, *Ventilation and air conditioning — Part 4: Ventilation in
  buildings and rooms of health care*.
