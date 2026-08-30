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
    src = I.VCO2_PATIENT_KAGAN
    e1 = room.co2_excess_steady_state(src, s1.outdoor)
    e2 = room.co2_excess_steady_state(src, s2.outdoor)
    assert abs(e1 / e2 - 2.0) < 1e-9


def test_recurrence_converges_to_steady_state():
    s = room.streams_from_ach(6.0, 1 / 3, I.ROOM_VOLUME_M3)
    src = 3 * I.VCO2_PATIENT_KAGAN
    ss = room.co2_excess_steady_state(src, s.outdoor)
    c = 0.0
    for _ in range(400):  # 400 x 15 min
        c = room.co2_excess_step(c, src, s.outdoor, I.ROOM_VOLUME_M3, 900)
    assert abs(c - ss) < 1e-6


def test_recurrence_is_exact_not_euler():
    """One step of dt must equal two steps of dt/2 to machine precision."""
    s = room.streams_from_ach(6.0, 1 / 3, I.ROOM_VOLUME_M3)
    src = 5 * I.VCO2_PATIENT_KAGAN
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
                    I.ICU_PM_SIZE_DISTRIBUTION, I.OCCUPANCY_SCHEDULE):
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
