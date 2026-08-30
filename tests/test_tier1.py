import math
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from icu import inputs as I
from icu import room, energy
from icu.scenarios import BY_KEY


def test_room_volume():
    assert I.ROOM_VOLUME_M3 == 75.0


def test_duct_is_one_square_foot():
    assert abs(I.DUCT_AREA_M2 - 0.092903) < 1e-6


def test_streams_balance():
    s = room.streams_from_ach(6.0, 1 / 3, I.ROOM_VOLUME_M3)
    assert abs(s.supply * 3600 - 450.0) < 1e-9
    assert abs(s.outdoor * 3600 - 150.0) < 1e-9
    assert abs(s.recirculated * 3600 - 300.0) < 1e-9
    # A5: exhaust balances outdoor air
    assert s.exhaust == s.outdoor


def test_full_outdoor_air_has_no_recirculation():
    s = room.streams_from_ach(10.0, 1.0, I.ROOM_VOLUME_M3)
    assert abs(s.recirculated) < 1e-12


def test_co2_excess_scales_inversely_with_outdoor_air():
    s1 = room.streams_from_ach(6.0, 1 / 3, I.ROOM_VOLUME_M3)
    s2 = room.streams_from_ach(6.0, 2 / 3, I.ROOM_VOLUME_M3)
    src = I.source_at_eval_state(I.VCO2_PATIENT_KAGAN)
    e1 = room.co2_excess_steady_state(src, s1.outdoor)
    e2 = room.co2_excess_steady_state(src, s2.outdoor)
    assert abs(e1 / e2 - 2.0) < 1e-9


def test_recurrence_converges_to_steady_state():
    s = room.streams_from_ach(6.0, 1 / 3, I.ROOM_VOLUME_M3)
    src = 3 * I.source_at_eval_state(I.VCO2_PATIENT_KAGAN)
    ss = room.co2_excess_steady_state(src, s.outdoor)
    c = 0.0
    for _ in range(400):  # 400 x 15 min
        c = room.co2_excess_step(c, src, s.outdoor, I.ROOM_VOLUME_M3, 900)
    assert abs(c - ss) < 1e-6


def test_recurrence_is_exact_not_euler():
    """One step of dt must equal two steps of dt/2 to machine precision."""
    s = room.streams_from_ach(6.0, 1 / 3, I.ROOM_VOLUME_M3)
    src = 5 * I.source_at_eval_state(I.VCO2_PATIENT_KAGAN)
    one = room.co2_excess_step(0.0, src, s.outdoor, I.ROOM_VOLUME_M3, 900)
    half = room.co2_excess_step(0.0, src, s.outdoor, I.ROOM_VOLUME_M3, 450)
    two = room.co2_excess_step(half, src, s.outdoor, I.ROOM_VOLUME_M3, 450)
    assert abs(one - two) < 1e-12


def test_duct_velocity_and_transit():
    s = room.streams_from_ach(6.0, 1 / 3, I.ROOM_VOLUME_M3)
    v = room.duct_velocity(s.supply, I.DUCT_AREA_M2)
    assert abs(v - 1.345) < 1e-3
    t = room.duct_transit_time(s.supply, I.DUCT_AREA_M2, I.DUCT_LENGTH_M)
    assert abs(t - 4.46) < 1e-2


def test_fan_cube_law():
    a = room.streams_from_ach(10.0, 0.5, I.ROOM_VOLUME_M3).supply
    b = room.streams_from_ach(6.0, 0.5, I.ROOM_VOLUME_M3).supply
    assert abs(energy.fan_power_ratio(a, b) - (10 / 6) ** 3) < 1e-12


def test_blocked_inputs_fail_closed():
    for blocked in (I.OUTDOOR_CO2_PPM, I.SYSTEM_PRESSURE_DROP_PA,
                    I.ICU_PM_SIZE_DISTRIBUTION, I.OCCUPANCY_SCHEDULE,
                    I.STAFF_VISITOR_OBSERVED, I.PATIENT_EXHAUST_PATH,
                    I.VCO2_PATIENT_ROUSING_PRESSURE_BASIS,
                    I.K_DEPOSITION, I.FAN_EFFICIENCY, I.ROOM_ACTUAL_T_P):
        try:
            float(blocked)
        except I.BlockedInput:
            continue
        raise AssertionError("blocked input did not raise")


def test_no_scenario_claims_ashrae_170_2025():
    """170-2025 is not in evidence; only the 2021 row is attested."""
    for g in BY_KEY.values():
        assert "170-2025" not in g.document, g.key


def test_htm_fresh_air_minimum_is_person_dependent():
    """max(20% of supply, 10 L/s/person), per HTM 03-01:2021 s8.6."""
    g = BY_KEY["G2"]
    q = g.ach_total * I.ROOM_VOLUME_M3  # m3/h
    assert abs(g.fresh_air_rule.controlling_m3_h(q, 3) - 150.0) < 1e-9
    assert abs(g.fresh_air_rule.controlling_m3_h(q, 5) - 180.0) < 1e-9
    assert abs(g.fresh_air_rule.controlling_m3_h(q, 11) - 396.0) < 1e-9


def test_uk_outdoor_air_is_not_unbounded():
    """Withdraws the earlier finding that f_OA could approach zero."""
    g = BY_KEY["G2"]
    q = g.ach_total * I.ROOM_VOLUME_M3
    for n in (3, 5, 11):
        assert g.fresh_air_rule.controlling_m3_h(q, n) / q >= 0.20


def test_scottish_rule_has_no_person_term():
    """SHTM 2014 supplies only the 20% fraction; the documents must not merge."""
    assert BY_KEY["G4"].fresh_air_rule.min_l_s_per_person is None
    assert BY_KEY["G2"].fresh_air_rule.min_l_s_per_person == 10.0


def test_india_moh_2022_scenario_present():
    g = BY_KEY["G9"]
    assert (g.ach_total, g.ach_total_max) == (10.0, 12.0)
    assert (g.ach_outdoor, g.ach_outdoor_max) == (4.0, 5.0)
    assert g.rh_pct == (45, 65)


def test_nabh_absence_is_not_proven():
    assert BY_KEY["G8"].blocked and "does not prove absence" in BY_KEY["G8"].blocked


# --- diurnal machinery -------------------------------------------------------
from icu import occupancy as occ
from icu.inputs import BlockedInput


def _forward_co2(n_series, q_oa, V, dt, c_out, patient, per_person):
    """Generate a CO2 trace from a known occupancy, for round-trip testing."""
    trace = [c_out]
    for n_other in n_series:
        s = patient + n_other * per_person
        excess = room.co2_excess_step(trace[-1] - c_out, s, q_oa, V, dt)
        trace.append(c_out + excess)
    return trace


def test_co2_inversion_round_trips_to_machine_precision():
    """Generate CO2 from a known occupancy, invert, recover the occupancy."""
    V, dt, c_out = I.ROOM_VOLUME_M3, 900.0, 420.0
    q_oa = room.streams_from_ach(6.0, 1 / 3, V).outdoor
    patient = I.source_at_eval_state(I.VCO2_PATIENT_KAGAN)
    per_person = I.source_at_eval_state(I.VCO2_MALE_21_30_BY_MET[1.2])

    known = [2, 2, 4, 7, 10, 10, 4, 2, 2, 3]  # non-patient occupancy
    trace = _forward_co2(known, q_oa, V, dt, c_out, patient, per_person)

    src = occ.co2_inversion(trace, q_oa, V, dt, c_out)
    recovered = occ.equivalent_occupants(
        occ.non_patient_source(src, patient), per_person)

    assert len(recovered) == len(known)
    for got, want in zip(recovered, known):
        assert abs(got - want) < 1e-9, (got, want)


def test_inversion_is_exact_not_finite_difference():
    """A finite-difference inversion would carry O(dt) error; this must not."""
    V, dt, c_out = I.ROOM_VOLUME_M3, 3600.0, 400.0  # deliberately coarse step
    q_oa = room.streams_from_ach(10.0, 0.5, V).outdoor
    patient = I.source_at_eval_state(I.VCO2_PATIENT_KAGAN)
    pp = I.source_at_eval_state(I.VCO2_MALE_21_30_BY_MET[1.4])
    known = [1, 6, 6, 1]
    trace = _forward_co2(known, q_oa, V, dt, c_out, patient, pp)
    rec = occ.equivalent_occupants(
        occ.non_patient_source(occ.co2_inversion(trace, q_oa, V, dt, c_out), patient), pp)
    for got, want in zip(rec, known):
        assert abs(got - want) < 1e-9


def test_event_profile_fails_closed_without_schedule():
    try:
        occ.profile_from_events(3, [], range(24))
    except BlockedInput:
        return
    raise AssertionError("empty schedule did not fail closed")


def test_event_requires_a_source_document():
    e = occ.Event("ward round", 8.0, 1.0, 5, source="")
    try:
        occ.profile_from_events(3, [e], range(24))
    except BlockedInput:
        return
    raise AssertionError("unsourced event was accepted")


def test_event_wraps_past_midnight():
    e = occ.Event("night shift", 22.0, 4.0, 1, source="SOP x, s.3, rev 2")
    assert e.active_at(23.0) and e.active_at(1.0)
    assert not e.active_at(4.0) and not e.active_at(12.0)


def test_concentration_tiers_are_separated():
    from icu import concentrations as C
    assert C.VERIFIED["bacteria_icu_total"][0] == 202
    assert C.VERIFIED["fungi_icu_respirable"][0] == 47
    tvoc = [r for r in C.REPORTED if r.pollutant == "TVOC"][0]
    assert tvoc.clean is None and "BLOCKED" in tvoc.provenance


def test_gases_have_no_filter_or_uv_pathway():
    from icu.concentrations import CHARACTER
    for gas in ("CO2", "TVOC"):
        mech = CHARACTER[gas][2]
        assert "filtration" not in mech and "UVGI" not in mech
    for viable in ("bacteria", "fungi"):
        assert "UVGI" in CHARACTER[viable][2]


def test_altunalan_is_excluded():
    """The article's prose and Table 2 conflict; no value may enter the model."""
    assert not any("ALTUNALAN" in n.upper() for n in dir(I))


def test_gas_state_conversion_matches_audit():
    """Persily -> Draeger STPD must reproduce the audit's derived values."""
    expected = {1.0: 3.890587e-6, 1.2: 4.788414e-6,
                1.4: 5.586483e-6, 1.6: 6.384552e-6}
    for met, want in expected.items():
        got = I.VCO2_MALE_21_30_BY_MET[met].at_state(I.STPD_DRAEGER_T, I.STPD_DRAEGER_P)
        assert abs(got - want) < 1e-12, (met, got, want)


def test_molar_is_reference_state_independent():
    """The same physical rate expressed at two states gives the same mol/s."""
    g = I.VCO2_MALE_21_30_BY_MET[1.2]
    other = I.GasState(g.at_state(300.0, 95000.0), 300.0, 95000.0, "arbitrary")
    assert abs(g.to_molar() - other.to_molar()) < 1e-18


# --- capability gating -------------------------------------------------------
from icu import capabilities as CAP


def test_all_six_capabilities_are_disabled():
    for name in ("co2_patient_inclusive", "headcount_inversion",
                 "filtration_size_resolved", "deposition",
                 "stage_c_control", "absolute_energy"):
        assert not CAP.enabled(name), f"{name} unexpectedly enabled"


def test_disabled_capability_names_its_prerequisites():
    try:
        CAP.require("co2_patient_inclusive")
    except CAP.CapabilityDisabled as e:
        msg = str(e)
        assert "DISABLED" in msg and "Unmet prerequisites" in msg
        assert "ventilator" in msg.lower()
        return
    raise AssertionError("capability did not raise")


def test_headcount_is_gated_but_equivalent_occupants_is_not():
    from icu import occupancy as o
    try:
        o.headcount([1e-6])
    except CAP.CapabilityDisabled:
        pass
    else:
        raise AssertionError("headcount was not gated")
    # equivalent occupants remains available, correctly labelled
    assert o.equivalent_occupants([4.8e-6], 4.8e-6) == [1.0]


def test_patient_inclusive_co2_prediction_is_gated():
    try:
        room.co2_prediction_patient_inclusive()
    except CAP.CapabilityDisabled:
        return
    raise AssertionError("patient-inclusive CO2 was not gated")


def test_generic_ventilator_statement_is_not_acceptable():
    try:
        float(I.PATIENT_EXHAUST_PATH)
    except I.BlockedInput as e:
        assert "generic statement" in str(e).lower()
        return
    raise AssertionError("exhaust path not blocked")


def test_declared_scenario_is_not_observed_data():
    """A declaration enables sensitivity runs only; prediction needs site data."""
    assert I.STAFF_VISITOR_SCENARIO_DECLARED is None
    try:
        float(I.STAFF_VISITOR_OBSERVED)
    except I.BlockedInput as e:
        assert "roster" in str(e).lower()
        return
    raise AssertionError("observed composition not blocked")


def test_ashrae_170_2021_row_is_reinstated():
    g = BY_KEY["G1"]
    assert not g.blocked and g.simulatable
    assert "170-2021" in g.document
    assert (g.ach_total, g.ach_outdoor) == (6.0, 2.0)
    assert g.temp_c == (21, 24) and g.rh_pct == (30, 60)
    # airstream now defined as mixed air (researcher-defined topology)
    assert "MIXED AIR" in g.filter_descriptor


# --- general multi-species balance -------------------------------------------
def test_general_form_reduces_to_the_co2_case():
    """CO2 has P=1, Z=1, k_dep=0, so B must collapse to Q_OA/V exactly."""
    V = I.ROOM_VOLUME_M3
    for ach, f in ((6.0, 1 / 3), (10.0, 0.2), (12.0, 0.5), (6.0, 1.0)):
        st = room.streams_from_ach(ach, f, V)
        a, b = room.coefficients(1e-6, st.supply, f, V)
        assert abs(b - st.outdoor / V) < 1e-15, (ach, f, b, st.outdoor / V)
        # and the steady state matches the CO2-specific helper
        assert abs(room.steady_state(a, b)
                   - room.co2_excess_steady_state(1e-6, st.outdoor) / 1e6) < 1e-15


def test_perfect_filter_makes_all_supply_clean():
    """P=0: every pass is scrubbed, so B = Q_s/V + k_dep regardless of f_OA."""
    V = I.ROOM_VOLUME_M3
    st = room.streams_from_ach(6.0, 0.2, V)
    a, b = room.coefficients(1e-6, st.supply, 0.2, V, penetration=0.0,
                             k_dep_per_s=1e-4)
    assert abs(b - (st.supply / V + 1e-4)) < 1e-15


def test_uv_enters_exactly_like_filter_penetration():
    """In-duct UV is mathematically a filter on the viable bins."""
    V = I.ROOM_VOLUME_M3
    st = room.streams_from_ach(10.0, 0.3, V)
    a1, b1 = room.coefficients(0.0, st.supply, 0.3, V, penetration=0.5,
                               uv_survival=0.4, c_outdoor=1.0)
    a2, b2 = room.coefficients(0.0, st.supply, 0.3, V, penetration=0.2,
                               uv_survival=1.0, c_outdoor=1.0)
    assert abs(a1 - a2) < 1e-18 and abs(b1 - b2) < 1e-18


def test_more_removal_never_raises_steady_state():
    V = I.ROOM_VOLUME_M3
    st = room.streams_from_ach(6.0, 0.25, V)
    prev = None
    for p in (1.0, 0.8, 0.5, 0.2, 0.0):
        a, b = room.coefficients(5e-6, st.supply, 0.25, V, penetration=p)
        ss = room.steady_state(a, b)
        if prev is not None:
            assert ss <= prev + 1e-15
        prev = ss


def test_recirculation_cannot_help_a_dilution_only_species():
    """With P=Z=1, changing f_OA is the only lever on CO2 and TVOC."""
    V = I.ROOM_VOLUME_M3
    lo = room.coefficients(5e-6, room.streams_from_ach(6.0, 0.2, V).supply, 0.2, V)
    hi = room.coefficients(5e-6, room.streams_from_ach(12.0, 0.1, V).supply, 0.1, V)
    # doubling supply while halving f_OA leaves outdoor air unchanged
    assert abs(lo[1] - hi[1]) < 1e-15


def test_pm_metrics_are_integrals_not_states():
    from icu.species import reported_metric, VIABLE_BINS_UM
    vals = [1.0] * 6
    # bins wholly at or below 2.5 um: 0.65-1.1 and 1.1-2.1
    assert reported_metric(vals, VIABLE_BINS_UM, 2.5) == 2.0
    # below 10 um: all closed bins, the open >7.0 bin is excluded
    assert reported_metric(vals, VIABLE_BINS_UM, 10.0) == 5.0


def test_gases_declare_no_particulate_pathway():
    from icu.species import SPECIES
    for g in ("CO2", "TVOC"):
        assert SPECIES[g].dilution_only
    for v in ("bacteria", "fungi"):
        assert SPECIES[v].uv_susceptible and SPECIES[v].binned
    assert not SPECIES["PM"].uv_susceptible
