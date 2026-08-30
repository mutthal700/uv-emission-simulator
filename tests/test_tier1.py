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
    src = I.source_at_room_state(I.VCO2_PATIENT_KAGAN)
    e1 = room.co2_excess_steady_state(src, s1.outdoor)
    e2 = room.co2_excess_steady_state(src, s2.outdoor)
    assert abs(e1 / e2 - 2.0) < 1e-9


def test_recurrence_converges_to_steady_state():
    s = room.streams_from_ach(6.0, 1 / 3, I.ROOM_VOLUME_M3)
    src = 3 * I.source_at_room_state(I.VCO2_PATIENT_KAGAN)
    ss = room.co2_excess_steady_state(src, s.outdoor)
    c = 0.0
    for _ in range(400):  # 400 x 15 min
        c = room.co2_excess_step(c, src, s.outdoor, I.ROOM_VOLUME_M3, 900)
    assert abs(c - ss) < 1e-6


def test_recurrence_is_exact_not_euler():
    """One step of dt must equal two steps of dt/2 to machine precision."""
    s = room.streams_from_ach(6.0, 1 / 3, I.ROOM_VOLUME_M3)
    src = 5 * I.source_at_room_state(I.VCO2_PATIENT_KAGAN)
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
                    I.STAFF_VISITOR_DEMOGRAPHICS, I.PATIENT_EXHAUST_PATH,
                    I.VCO2_PATIENT_ROUSING_PRESSURE_BASIS):
        try:
            float(blocked)
        except I.BlockedInput:
            continue
        raise AssertionError("blocked input did not raise")


def test_guideline_simulatability():
    assert BY_KEY["G1"].simulatable and BY_KEY["G1"].min_f_oa() == 2.0 / 6.0
    # UK rows state no outdoor-air value
    assert BY_KEY["G2"].min_f_oa() is None
    # Victoria fixes the fraction but states no rate
    assert not BY_KEY["G6"].simulatable and BY_KEY["G6"].min_f_oa() == 0.5


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
    patient = I.source_at_room_state(I.VCO2_PATIENT_KAGAN)
    per_person = I.source_at_room_state(I.VCO2_MALE_21_30_BY_MET[1.2])

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
    patient = I.source_at_room_state(I.VCO2_PATIENT_KAGAN)
    pp = I.source_at_room_state(I.VCO2_MALE_21_30_BY_MET[1.4])
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
