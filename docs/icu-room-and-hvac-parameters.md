# ICU Room and HVAC Parameters — Verified Source Register

Status: **geometry closed; ventilation parameters open, awaiting pasted sources.**

Rule for this file: an entry is written only after the figure has been read
first-hand from a primary document. Nothing is inferred, interpolated, or
recalled. Unsourced parameters stay marked `pending` rather than being filled
with a plausible value.

---

## 0. Agreed scope

| Decision | Setting |
|---|---|
| Geometry | Area x ceiling height only. No length/width; room treated as a single well-mixed zone. |
| Jurisdictions | All — the work is a cross-country comparison, so every standard gets its own row and is reported separately, not merged into a single "typical" value. |
| Operating mode | Normal ICU operation only. Airborne-infection-isolation / negative-pressure cases are out of scope. |
| Source route | Tables pasted as text by the researcher; each entry recorded with document, edition and table/row. |

---

## 1. Verified: room geometry and occupancy

Source, read in full in this session:

> Australasian Health Infrastructure Alliance (AHIA), *Australasian Health
> Facility Guidelines — Room Data Sheet, "1 Bed Room - Intensive Care",
> Room Code 1BR-ICU*. Issue date 12.11.2025, Revision 2, 7 pages.
> Copyright (c) 2025 AHIA.

| Quantity | Value | Location in source |
|---|---|---|
| Briefed area, `A` | `25.00 m²` | page 1, "Briefed Area" |
| Ceiling height, `H` | `3.0 m` | page 1, "Ceiling Height" |
| Occupancy | `1 patient; 1-2 visitors; 1-2 staff (with 4-6 additional staff as required)` | page 1, "Occupancy" |
| Hours of operation | `24 hours` | page 1 |
| Beds | 1 | page 5, `MMBE-116 BED: patient, electric, with mattress, intensive care`, QTY 1 |

Room volume, by arithmetic on the two verified figures above:

    V = A x H = 25.00 m² x 3.0 m = 75.0 m³

Volumetric flow for any air change rate, by definition of ACH:

    Q [m³/h] = ACH [1/h] x 75.0 m³
    Q [L/s]  = ACH [1/h] x 75.0 / 3.6

No ACH value is asserted here; see section 3.

### 1.1 What the 25.00 m² covers

Established from the source, not assumed:

- The area **excludes** the staff write-up workstation. Page 2: "A write-up
  workstation with observation windows is currently indicated directly outside
  the bed room *(area not included calculation for the area of this Standard
  Component)*."
- The area **contains no ensuite**. The hydraulic schedule for this room code
  lists exactly one sanitary fixture — `HYBA-101 BASIN: type A, handwashing`
  with `HYTP-067` tapware (page 4). There is no WC, shower or bedpan fixture.
  The remaining hydraulic items are dialysis-related (`HYGE-082` wall box,
  `HYDR-104` tundish, `HYDR-157` cooling pit) plus drainage connections. The
  patient-lifter note on page 2 offers "full transfer to ensuite" as an optional
  track extent, indicating an ensuite adjacent to the Standard Component rather
  than inside it.

So `25.00 m²` is the patient bed room alone, and `V = 75.0 m³` is the volume of
the single zone to be modelled.

### 1.2 Occupant count for source-term modelling

The occupancy line supports two counts, both read directly from it:

- steady state: 1 patient + 1-2 visitors + 1-2 staff → 3 to 5 persons
- with surge staff: + 4-6 additional staff → up to 11 persons

### 1.3 Room envelope (pages 3-4, verbatim codes)

| Element | Source entry | Figure |
|---|---|---|
| Main door | `DOST-074.01 DOOR: stacking, 2 leaves + 1 fixed panel, fully glazed` | **1800 mm clear opening** |
| Second door (optional) | `DOSL-073.02 DOOR: sliding, 1 leaf, fully glazed, with integral blinds` | **900 mm clear opening** |
| External window | `WIOP-256.02 WINDOW: operable, jockey sash, external, double glazed, with integral blind` | **operable**, sill at 750 mm |
| Internal windows | `WIFX-058.04 WINDOW: fixed, internal, double glazed, with integral blind` x3 — two to staff write-up (if provided), one to adjacent room | fixed, sill at 1050 mm |
| Ceiling | `CLFS-011 CEILING: flush set, suspended`; `CLCN-031 CORNICE: square set` | at 3.0 m |
| Floor | `FLVY-101 FLOOR FINISH: vinyl, seamless`; `FLSK-021 SKIRTING: vinyl, integral, coved` | — |
| Walls | `WLFI-002` paint, clinical areas; `WLFI-011.03` vinyl to 1200 AFFL | — |

Bearing on the model: the door clear openings give the aperture for any
door-opening exchange term; the operable external window confirms that the
`VENTILATION: natural` service listed on page 1 is physically realisable in this
room; the flush-set suspended ceiling at 3.0 m is the mounting plane for supply
terminals and for any upper-room fixture.

### 1.4 HVAC service types named in the sheet (page 1, verbatim)

The sheet lists which services the room may have. It gives no quantities.

```
HVAC   AIRCONDITIONING: general
       AIRCONDITIONING: HEPA filtered
       AIRCONDITIONING: positive pressure
       AIRCONDITIONING: negative pressure
       VENTILATION: exhaust
       VENTILATION: supply
       VENTILATION: natural
```

Page 1 also notes the room "may be utilised as a standard pressure (S-Class)
isolation room", with P-Class and N-Class engineering referred out to *AusHFG
Part D: Infection Prevention and Control* and *AusHFG Isolation Room –
Engineering and Design Requirements* (page 2). Isolation modes are out of scope
per section 0.

### 1.5 Equipment relevant to an emission source term (pages 5-7)

`MMHA-051 DEVICE: ventilator, adult` (1); `MMPM-021 MONITOR: patient, high
acuity` (1); `MMGE-381 MACHINE: dialysis` (1, optional); `MMSP-212 MEDICAL
SERVICES PENDANT: double arm` (1); oxygen, medical air and suction outlets,
2 each per pendant arm.

---

## 2. Confirmed absent from the AusHFG sheet

Checked, not assumed. All 7 pages were text-extracted and all 22 embedded
images were extracted and inspected — the images are section icons repeated on
every page, and the file contains no floor plan.

Not stated anywhere in the document:

- overall length or width — door and window openings are dimensioned, the room
  outline is not
- air changes per hour
- outdoor air rate or outdoor air fraction
- filter class — HEPA is named as a service, with no H-class, no MERV, no
  ISO 16890 grade, and no pre-filter stage
- pressure differential in Pa
- design temperature and design relative humidity
- supply or return terminal type, size or position

---

## 3. Provenance tiers

Values in this file carry one of three tags. The distinction matters because
section 0 committed to primary text only, and not every entry below meets that
bar in the same way.

- **[READ]** — read first-hand from the primary document in this session.
- **[ATTESTED]** — recorded from *ICU guideline archive verification*,
  2026-08-29, which reports having inspected the primary document and gives a
  full locator. The underlying PDF has not been opened here. This is a report
  *about* a document, not the document.
- **[ATTESTED-EXT]** — as above, but the verification report itself states the
  evidence was supplied separately as images rather than from the archive.

---

## 4. Comparison table

| Jurisdiction | Document, edition | Locator | Total ACH | Outdoor air | Pressure | Filtration | T | RH | Room area | Ceiling | Tier |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AU/NZ (room) | AusHFG RDS 1BR-ICU, Rev 2, 12.11.2025 | page 1 | — | — | S/P/N-class selectable, no Pa | "HEPA filtered" named, no class | — | — | **25.00 m²** | **3.0 m** | [READ] |
| AU/NZ (vent) | AusHFG Part E; AS 1668.2 | pending | pending | pending | pending | pending | pending | pending | — | — | — |
| AU – Victoria | *Engineering guidelines for healthcare facilities, Vol 4 – HVAC*, HTG-2020-004, VHHSBA, May 2020 | §4.172 "ICU and CCU", p34 | not in this clause | **50 % outside air to patient areas** | positive, beds → circulation | remote HEPA outside the ICU | — | — | — | — | [ATTESTED] |
| US | ANSI/ASHRAE/ASHE 170-**2025** | Table 7-1, "Critical care patient care station (FGI 2.2-2.6.2)" | **6 min** | **2 ACH min** | **N/R** | **MERV-14 min** | 70–75 °F / 21–24 °C | 30–60 % | see FGI | — | [ATTESTED-EXT] |
| US (area) | FGI *Hospitals*, 2022 | ICU room-area clause | — | — | — | — | — | — | pending | pending | — |
| UK | HTM 03-01 Part A, **2021** | Table 3, "Level 2 or 3 critical care individual room", p64 print / p80 PDF | **≥10 ac/h** | supply only; cascade out | **+5 Pa** to general area | **BS EN 1822 EPA10** final | 20–25 °C, BMS | floating, max 60 % | — | — | [ATTESTED] |
| UK | HTM 03-01 Part A, **2021** | Appendix 2, "Critical care areas (Level 2 and 3 care)", p147 print / p163 PDF | **10 ac/h** | supply | **+10 Pa** | **BS EN 16798 SUP1** supply | not in this row | — | — | — | [ATTESTED] |
| UK (area) | HBN 04-02, **2013** | §4.14 and §4.17, p9 print / p18 PDF | — | — | — | — | — | — | **25.5 m² min bed space** | **3 m recommended** | [ATTESTED] |
| UK (historical) | SHTM 03-01 Part A, v2 Feb 2014, **archived** | Appendix 1, Table A1, "Critical Care Areas", p139 | 10 ac/h | supply | +10 Pa | **F7** supply | 18–25 °C | — | — | — | [ATTESTED] |
| India | ISCCM Consensus Statement on ICU Planning and Designing, **2020** | "Environmental Requirements" → HVAC system of ICU | **6** | **2 ACH** | no numerical differential given for general ICU | **99 % efficiency down to 5 µm** | 16–25 °C (enclosed patient modules) | not stated | — | — | [ATTESTED] |
| India | NABH *Accreditation Standards for Hospitals*, 6th ed., Jan 2025 | COP.9 | **ABSENT** | ABSENT | ABSENT | ABSENT | ABSENT | ABSENT | — | — | [ATTESTED] |
| India | NBC 2016 Part 8 §3 | Tables 4, 6, 7 | pending | pending | pending | pending | pending | pending | — | — | — |
| Germany | DIN 1946-4:2018-09 + /A1:2025-11 | Table 1, room classification | pending | pending | pending | pending | pending | pending | — | — | — |
| Canada | CSA Z317.2; CSA Z8000 | edition to be named | pending | pending | pending | pending | pending | pending | pending | — | — |

NABH is marked **ABSENT** rather than pending: full-document screening found no
numerical ICU HVAC values. For a comparison study that is a finding, not a gap.

---

## 5. Flow rates implied for this room

Arithmetic on the verified volume `V = 75.0 m³`. No rate is asserted; each is
the consequence of a sourced ACH.

| Basis | ACH | Q (m³/h) | Q (L/s) |
|---|---|---|---|
| ASHRAE 170-2025 / ISCCM 2020, total | 6 | 450 | 125.0 |
| ASHRAE 170-2025 / ISCCM 2020, outdoor | 2 | 150 | 41.7 |
| HTM 03-01 2021 / SHTM 2014, total | 10 | 750 | 208.3 |
| Victoria HTG-2020-004, outdoor at 6 ACH total | 3.0 | 225 | 62.5 |
| Victoria HTG-2020-004, outdoor at 10 ac/h total | 5.0 | 375 | 104.2 |

**The UK total is 1.67x the US/India total.** At this volume that is 300 m³/h of
additional supply, and it propagates directly into the HVAC removal term.

Outdoor air per person at the ASHRAE/ISCCM minimum of 2 ACH (150 m³/h), against
the occupancy verified in §1.2:

| Occupancy | Persons | m³/h per person | L/s per person |
|---|---|---|---|
| Minimum steady | 3 | 50.0 | 13.9 |
| Maximum steady | 5 | 30.0 | 8.3 |
| With surge staff | 11 | 13.6 | 3.8 |

The 2 ACH floor is volume-based, not occupancy-based, so per-person outdoor air
falls to roughly a quarter of its steady-state value during a surge.

---

## 6. Observations bearing on the model

**6.1 Two jurisdictions converge on room size.** AusHFG 25.00 m² [READ] and
HBN 04-02 25.5 m² [ATTESTED] agree within 2 %, from independent guideline
families. `V = 75.0 m³` is well supported. FGI remains the outlier candidate and
is still pending.

**6.2 Filtration is specified in four incommensurable systems.** MERV-14
(ASHRAE 52.2), EPA10 (BS EN 1822), SUP1 (BS EN 16798), and "99 % down to 5 µm"
(ISCCM), plus historical F7 (EN 779). These cannot be placed in a single column
without stating a conversion basis, and at least one pair is not convertible at
all: EN 1822 EPA10 is a *filter efficiency* class, while EN 16798 SUP1 is a
*supply air quality* category — different quantities, not different units for
the same quantity. Any cross-country filtration comparison has to address this
explicitly rather than tabulating them side by side.

**6.3 HTM 03-01 2021 is internally inconsistent in two places, not one.** The
verification report flags the pressure disagreement (+5 Pa in Table 3 vs +10 Pa
in Appendix 2) and is right that these must not be collapsed. The same two
locations also disagree on filtration — EN 1822 EPA10 in Table 3, EN 16798 SUP1
in Appendix 2 — which is the more awkward of the two, per §6.2.

**6.4 The ISCCM filtration spec is coarse relative to the aerosols of
interest.** "99 % efficiency down to 5 µm" sets no requirement below 5 µm.
Respirable infectious aerosol is largely sub-5 µm, so this clause constrains the
recirculation removal term far less than MERV-14 or EPA10 do. Worth stating
plainly if the comparison reports a single "filtration" row.

**6.5 ASHRAE 170-2025 permits unoccupied turndown.** Table 7-1 records
"Unoccupied turndown: Yes" for this space. The code-permitted ventilation rate
is therefore not constant in time, which matters for any transient simulation
and for how a UV term is credited against it.

**6.6 UK filtration tightened between editions.** SHTM 03-01 v2 (2014) specifies
F7; HTM 03-01 (2021) specifies EPA10. A directional change over time that a
comparative paper can report.

---

## 7. Still required

| Document | Edition | Locator needed |
|---|---|---|
| AusHFG Part E – Building Services and Environmental Design | edition to be identified | intensive-care ventilation entry |
| AS 1668.2 | 2012 or 2024 | intensive-care ventilation entry |
| FGI *Guidelines for Design and Construction of Hospitals* | 2022 | adult ICU patient-room area clause |
| ANSI/ASHRAE/ASHE 170-2025 | 2025 + 2026 errata | §6.4 filter-bank topology |
| NBC India 2016 Part 8, Section 3 | 2016 | ICU rows in Tables 4, 6, 7 |
| DIN 1946-4 | 2018-09 + /A1:2025-11 | Table 1, intensive-care classification |
| CSA Z317.2; CSA Z8000 | to be named | ICU row; critical-care room area |

---

## 8. Session limitation

Primary-document retrieval is not possible from this environment. Every
outbound host tested returned an HTTP 403 policy denial at the egress gateway,
across two rounds covering standards bodies, health departments, publishers and
preprint servers. Only GitHub hosts are reachable. Sources must therefore be
supplied directly to the session.
