# Verified CO2 generation source audit

## Verdict

The supplied table is **not valid unchanged**. Three corrections are required:

1. The Kagan value is a six-hour mean VCO2 reported by the **Evita 4 ventilator**, not the Deltatrac II indirect calorimeter.
2. The Persily values describe the **male, age 21 to <30** row of Table 4. They are not a generic staff/visitor class.
3. The Altunalan value cannot be used: the article's results prose and Table 2 contradict one another about VCO2 and VO2.

No proxy values, substitutions, or interpolations are included below. Values in m3/s are arithmetic unit conversions of source-reported values and are marked as such.

## Source-faithful values

| Class or scenario | Source-reported value | Unit-only conversion to m3/s | Reporting basis and status | Exact source locator |
|---|---:|---:|---|---|
| Patient - Kagan et al. cohort mean | 244.5 +/- 85.9 mL/min | **(4.075 +/- 1.432) x 10^-6** | Six-hour block mean from the Evita 4 ventilator. Drager specifies this displayed CO2-production value as STPD: 0 deg C, 1013 hPa, dry. | Kagan et al. (2018), *Validation of carbon dioxide production (VCO2) as a tool to calculate resting energy expenditure (REE) in mechanically ventilated critically ill patients*, *Critical Care* 22:186, **Methods** and **Results**. Drager, *Instructions for Use: Evita 4 / Evita 4 edition, Software 4.n*, **Edition 5, 2015-01**, document 9039485, **Technical data - Measured value displays**, printed p. 176. |
| Patient - Rousing et al. cohort mean | 273 +/- 63 mL/min | **(4.550 +/- 1.050) x 10^-6** | Thirty-minute indirect-calorimetry cohort mean measured with the E-CAiOVX Compact Airway Module. GE's clinical reference for this named module reports VCO2 in mL/min at standard temperature (0 deg C), dry gas (STPD). The reviewed GE text does **not** give a numeric standard pressure, so no exact pressure harmonization is asserted. | Rousing et al. (2016), *Energy expenditure in critically ill patients estimated by population-based equations, indirect calorimetry and CO2-based indirect calorimetry*, *Annals of Intensive Care* 6:16, **Methods - Patients** and **Results - Comparing estimates of energy expenditure**. GE Healthcare, *CARESCAPE Monitors Clinical Reference Manual*, **30 March 2009**, 2040384-003A, **Chapter 12 - Gas exchange, Carbon dioxide production**, pp. 12-4 to 12-5. |
| Patient - Altunalan et al. | **Excluded** | **Not available** | The source is internally inconsistent. Results prose reports VCO2 means of 188.362, 203.000, and 189.812 mL/min. Table 2 instead reports VCO2 as 275.32 +/- 118.44 mL/min at all three time points and places 188.36 +/- 77.28 under VO2. The source does not permit a defensible choice between them. | Altunalan et al. (2026), *Metabolic and hemodynamic responses to early passive range of motion in sedated critically ill adults*, *BMC Anesthesiology* 26:89, **Results - Metabolic response**, printed p. 4, versus **Table 2**, printed p. 5. Version of record dated 4 February 2026. |
| Occupant scenario - male, age 21 to <30, 1.0 / 1.2 / 1.4 / 1.6 met | 0.0039 / 0.0048 / 0.0056 / 0.0064 L/s | **3.90 / 4.80 / 5.60 / 6.40 x 10^-6** | Source basis is 273 K and 101 kPa. These values apply to the specified sex/age class and mean body mass used by Persily; they are not universal staff or visitor rates. The met levels remain declared scenario parameters unless separately supported. | Persily and de Jonge (2017), *Carbon dioxide generation rates for building occupants*, *Indoor Air* 27(5):868-879, **Table 4**, male 21 to <30 row, p. 875; basis stated in the text preceding Table 4. |

## Arithmetic audit

Only the following exact unit conversions were applied:

```text
m3/s = (mL/min) x 10^-6 / 60
m3/s = (L/s) x 10^-3
```

Therefore:

```text
244.5 mL/min  = 4.075000e-6 m3/s
85.9 mL/min   = 1.431667e-6 m3/s
273 mL/min    = 4.550000e-6 m3/s
63 mL/min     = 1.050000e-6 m3/s
```

## Gas-basis reconciliation

The earlier caveat "clinical calorimetry reports STPD or BTPS" is too broad. For these VCO2 data:

- Drager explicitly reports Evita 4 CO2 production at STPD, 0 deg C, 1013 hPa, dry.
- GE's gas-exchange reference reports VCO2 at standard temperature, 0 deg C, dry gas (STPD); it distinguishes this from alveolar ventilation at BTPS.
- Persily reports volumetric rates at 273 K and 101 kPa.

Persily can be converted exactly to the Drager STPD basis without introducing empirical data:

```text
V_Drager-STPD = V_Persily x (273.15 / 273) x (101 / 101.3)
               = V_Persily x 0.997586322858
```

This produces the following **derived harmonization**, not source-reported values:

| Persily male 21 to <30 scenario | At source basis, 273 K and 101 kPa (m3/s) | At Drager STPD, 273.15 K and 101.3 kPa (m3/s) |
|---|---:|---:|
| 1.0 met | 3.900000e-6 | **3.890587e-6** |
| 1.2 met | 4.800000e-6 | **4.788414e-6** |
| 1.4 met | 5.600000e-6 | **5.586483e-6** |
| 1.6 met | 6.400000e-6 | **6.384552e-6** |

The Rousing/GE value should not be pressure-normalized further until a GE document stating the numeric standard pressure for the relevant monitor revision is available. Calling both values "STPD" is not sufficient for an exact pressure conversion under a no-assumption rule.

For a model evaluated at another dry-gas state `(T_model, P_model)`, use the ideal-gas relation only after the source reference state has been established:

```text
V_model = V_reference x (T_model / T_reference) x (P_reference / P_model)
```

Using mol/s or kg/s internally avoids ambiguity from volumetric reference conditions.

## Modeling boundaries that remain open

- **Met level:** 1.0, 1.2, 1.4, and 1.6 met are scenario inputs here. No ISO 8996 value has been inserted.
- **Staff/visitor demographics:** Persily Table 4 varies by sex and age. The male 21 to <30 row cannot represent all staff and visitors without an explicitly declared demographic scenario.
- **Patient variability:** Kagan and Rousing are cohort means, not universal single-patient emission factors.
- **Altunalan:** no numeric VCO2 value from this paper should enter the model until the source discrepancy is corrected by the publisher or authors.
- **Room-source boundary:** physiological or ventilator-measured VCO2 becomes a room CO2 source only to the extent that the patient's exhaled gas is discharged into the room. The ventilator exhaust/scavenging/return path must be documented for the modeled ICU.
- **Archive check:** the supplied `Archive.zip` contains healthcare ventilation standards and guidelines, but none of the Kagan, Rousing, Altunalan, Persily, or cited device-reference documents. The CO2 audit therefore uses the primary publisher and manufacturer documents linked below.

## Primary and manufacturer sources

1. [Kagan et al. (2018), Critical Care 22:186](https://link.springer.com/article/10.1186/s13054-018-2108-8)
2. [Drager, Instructions for Use: Evita 4 / Evita 4 edition SW 4.n, Edition 5 (2015-01), document 9039485](https://www.draeger.com/Library/Content/IfU_Evita_4_SW_4.n_EN_9039485.pdf)
3. [Rousing et al. (2016), Annals of Intensive Care 6:16](https://link.springer.com/article/10.1186/s13613-016-0118-8)
4. [GE Healthcare, CARESCAPE Monitors Clinical Reference Manual, 2040384-003A (30 March 2009)](https://www.scribd.com/document/520410543/2040384-003A-Clinical-Ref-Manual)
5. [GE HealthCare, Gas exchange and indirect calorimetry, JB32913XX (3/2025)](https://clinicalview.gehealthcare.com/sites/default/files/Appliguide-Gas-exchange-and-indirect%20calorimetry-JB32913XX_Mar27.pdf)
6. [Altunalan et al. (2026), BMC Anesthesiology 26:89](https://link.springer.com/article/10.1186/s12871-025-03565-2)
7. [Persily and de Jonge (2017), NIST-hosted article PDF](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=920870)

## Final usable status

- **Usable with the stated source conditions:** Kagan, Rousing, and the explicitly labeled Persily male 21 to <30 scenarios.
- **Usable after exact conversion to Drager STPD:** Kagan and the derived Persily values shown above.
- **Not usable:** Altunalan, pending correction of the article's internal VCO2/VO2 conflict.
- **Not yet fully harmonized:** Rousing versus the numeric pressure basis, because the reviewed GE references state STPD and 0 deg C/dry but not the numeric standard pressure.
