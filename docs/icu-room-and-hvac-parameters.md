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

## 3. Comparison table — to be filled from pasted sources

One row per jurisdiction, reported separately. Every cell is `pending` until
the source text is supplied.

| Jurisdiction | Document + edition | Total ACH | Outdoor air | Pressure | Filtration | Design T | Design RH | Room area | Ceiling ht |
|---|---|---|---|---|---|---|---|---|---|
| Australia / NZ | pending | pending | pending | pending | pending | pending | pending | **25.00 m²** (verified) | **3.0 m** (verified) |
| United States | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| United Kingdom | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| India | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| Germany | pending | pending | pending | pending | pending | pending | pending | pending | pending |
| Canada | pending | pending | pending | pending | pending | pending | pending | pending | pending |

---

## 4. What to paste, per jurisdiction

For each paste, include the **document title, edition/year, and table or
section number**. Edition matters: the same standard has changed these values
between revisions, and a comparison study has to name which revision it used.

**Australia / NZ**
- AusHFG Part E – Engineering Services, or AS 1668.2 (state the year, 2012 or
  2024): the ventilation rate entry covering intensive care.

**United States**
- ANSI/ASHRAE/ASHE Standard 170 (state the edition — 2008, 2013, 2017 or 2021):
  the design-parameters table row for critical / intensive care, with all its
  columns: pressure relationship to adjacent areas, minimum outdoor ACH,
  minimum total ACH, whether all room air is exhausted directly outdoors,
  whether air is recirculated by room units, design RH, design temperature.
- The same standard's filtration requirement for that space — in the 2008-2017
  editions this is a separate filter-efficiency table (filter bank 1 and filter
  bank 2); in the 2021 edition filtration was moved into the space tables, so
  paste whichever your copy has.
- FGI *Guidelines for Design and Construction of Hospitals* (state the edition):
  the critical care patient room area requirement.

**United Kingdom**
- HBN 04-02 *Critical care units*: the bed space area and ceiling height text.
- HTM 03-01 Part A, or SHTM 03-01: the appendix table row for critical care —
  air change rate and pressure regime.

**India**
- ISCCM ICU planning and design guidelines: the HVAC section.
- NABH standard, and NBC 2016 Part 8 if you have it: the ICU ventilation clause.

**Germany**
- DIN 1946-4:2018-09: the room-class table, and which class intensive care
  falls into, with its air volume and filter stages.

**Canada** (optional, if you have access)
- CSA Z317.2 *HVAC systems in health care facilities*: the ICU row.
- CSA Z8000 *Canadian health care facilities*: the critical care room area.

Paste in any order and in any size chunks — each one gets recorded against its
row in section 3 as it arrives.

---

## 5. Session limitation

Primary-document retrieval is not possible from this environment. Every
outbound host tested returned an HTTP 403 policy denial at the egress gateway
(`connect_rejected`, "gateway answered 403 to CONNECT"): `www.ashrae.org`,
`www.england.nhs.uk`, `www.cdc.gov`, `fgiguidelines.org`,
`ccforum.biomedcentral.com`, `doi.org`, `www.who.int`,
`store.standards.org.au`, `healthfacilityguidelines.com.au`,
`www.nss.nhs.scot`, `en.wikipedia.org`.

Web search still returns titles and machine-written summaries, but a summary of
a page is not the page, and nothing obtained that way is recorded in this file.
