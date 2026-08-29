# ICU Room and HVAC Parameters — Verified Source Register

Status: **incomplete — awaiting primary sources.**

This file records only what has been read first-hand from a primary document.
Nothing here is inferred, interpolated, or recalled. Items that cannot yet be
sourced are listed in section 3 as open, not filled with a placeholder.

---

## 1. Verified: AusHFG Room Data Sheet 1BR-ICU

Source, read in full in this session:

> Australasian Health Infrastructure Alliance (AHIA), *Australasian Health
> Facility Guidelines — Room Data Sheet, "1 Bed Room - Intensive Care",
> Room Code 1BR-ICU*. Issue date 12.11.2025, Revision 2, 7 pages.
> Copyright (c) 2025 AHIA.

### 1.1 Geometry and occupancy (page 1, verbatim)

| Field | Value as printed |
|---|---|
| Briefed Area | `25.00 m²` |
| Ceiling Height | `3.0 m` |
| Occupancy | `1 patient; 1-2 visitors; 1-2 staff (with 4-6 additional staff as required)` |
| Hours of Operation | `24 hours` |

Bed count is 1, established from the FF&E schedule (page 5):
`MMBE-116  BED: patient, electric, with mattress, intensive care  QTY 1`.

The sheet describes the room as "an acuity adaptable, enclosed room for a
patient requiring intensive medical treatment, nursing care and monitoring for
potentially life threatening conditions" (page 1).

### 1.2 HVAC services listed (page 1, verbatim)

The sheet lists service *types* available to the room. It gives no quantities.

```
HVAC   AIRCONDITIONING: general
       AIRCONDITIONING: HEPA filtered
       AIRCONDITIONING: positive pressure
       AIRCONDITIONING: negative pressure
       VENTILATION: exhaust
       VENTILATION: supply
       VENTILATION: natural
```

### 1.3 Pressure regime (pages 1-2, verbatim)

> "This room may be utilised as a standard pressure (S-Class) isolation room."
> (page 1)

> "For additional information on standard pressure (S-Class) isolation rooms, as
> well considerations and requirements for positive pressure (P-Class) and
> negative pressure (N-Class) rooms refer to 'AusHFG Part D: Infection
> Prevention and Control' and 'AusHFG Isolation Room- Engineering and Design
> Requirements'." (page 2)

So the ICU room's pressure class and its engineering values are **defined in two
other AusHFG documents**, not in this sheet.

### 1.4 The one dimensional constraint stated in the sheet (page 2)

> "The handwashing basin is to be located at least 1.2m from the patient bed."

### 1.5 Equipment relevant to a source/emission model (pages 5-7)

`MMHA-051 DEVICE: ventilator, adult` (1), `MMPM-021 MONITOR: patient, high
acuity` (1), `MMGE-381 MACHINE: dialysis` (1, optional), `MMSP-212 MEDICAL
SERVICES PENDANT: double arm` (1), oxygen / medical air / suction outlets x2 per
pendant arm.

---

## 2. Not present in this document

Checked and confirmed absent — do not assume these from the sheet:

- **Length and width.** The sheet gives area and ceiling height only. All 7
  pages were text-extracted and all 22 embedded images were extracted and
  inspected; the images are section icons repeated on every page. There is no
  floor plan and no L x B dimension anywhere in the file. The header line
  "View related documents on the AusHFG website" indicates the dimensioned
  Standard Component drawing is a separate document.
- **Air changes per hour.** Not stated.
- **Outdoor / fresh air rate or fraction.** Not stated.
- **Filter grade.** "HEPA filtered" is named as an available service; no class
  (H13/H14), no MERV, no ISO 16890 grade, and no pre-filter is specified.
- **Pressure differential in Pa.** Not stated.
- **Design temperature or relative humidity.** Not stated.
- **Supply/return terminal type or position.** Not stated.

---

## 3. Open items and the exact source needed for each

| # | Parameter | Document required | Where in it |
|---|---|---|---|
| 1 | Room length x width | AusHFG Standard Component drawing for 1BR-ICU | dimensioned floor plan |
| 2 | ACH, outdoor air, filter grade, pressure (AU) | AS 1668.2 and/or AusHFG Part E — Engineering Services | healthcare ventilation rate table |
| 3 | Isolation-mode engineering values (AU) | AusHFG *Isolation Room – Engineering and Design Requirements*; AusHFG Part D | S/P/N-class tables |
| 4 | ACH, outdoor ACH, pressure, T, RH (US) | ANSI/ASHRAE/ASHE 170 — state the edition | Table 7.1, row "Critical and intensive care" |
| 5 | Filter bank efficiencies (US) | ANSI/ASHRAE/ASHE 170 — same edition | Table 6-4 (2008-2017) or the space table (2021+) |
| 6 | Clear floor area, headwall, clearances (US) | FGI *Guidelines for Design and Construction of Hospitals* — state the edition | critical care unit section |
| 7 | Bed space area, ceiling height (UK) | HBN 04-02 *Critical care units* | bed space / space requirements |
| 8 | ACH and pressure regime (UK) | HTM 03-01 Part A, or SHTM 03-01 | Appendix 1 air change rate table |
| 9 | ACH, fresh air, filtration (India) | ISCCM ICU planning guidelines; NABH standard | HVAC section |
| 10 | Room class and air volumes (DE) | DIN 1946-4:2018-09 | room class table |

---

## 4. Session limitation affecting verification

Primary-document retrieval is not possible from this environment. Every outbound
host tested returned an HTTP 403 policy denial at the egress gateway
(`connect_rejected`, "gateway answered 403 to CONNECT"), including
`www.ashrae.org`, `www.england.nhs.uk`, `www.cdc.gov`, `fgiguidelines.org`,
`ccforum.biomedcentral.com`, `doi.org`, `www.who.int`,
`store.standards.org.au`, `healthfacilityguidelines.com.au`,
`www.nss.nhs.scot` and `en.wikipedia.org`.

Web *search* still returns result titles and machine-written summaries, but a
summary of a page is not the page. Nothing sourced that way has been entered in
section 1, and nothing should be.

To close section 3, the source documents need to be supplied directly — uploaded
as files to the session, or the relevant table pasted as text.
