import builtins

import missions.hospital_delivery as hospital_delivery
import missions.rescue_navigation as rescue_navigation
import missions.traffic_cleanup as traffic_cleanup
import missions.warehouse_sorting as warehouse_sorting


def test_warehouse_collect_aisle_going_north_picks_expected_cells(monkeypatch):
    front_states = iter([True, True, False])
    beeper_states = iter([True, False, True])
    moves = []
    picks = []
    faced_north = []

    monkeypatch.setattr(warehouse_sorting, 'face_north', lambda: faced_north.append(True))
    monkeypatch.setattr(builtins, 'front_is_clear', lambda: next(front_states), raising=False)
    monkeypatch.setattr(builtins, 'beepers_present', lambda: next(beeper_states), raising=False)
    monkeypatch.setattr(builtins, 'move', lambda: moves.append('move'), raising=False)
    monkeypatch.setattr(builtins, 'pick_beeper', lambda: picks.append('pick'), raising=False)

    warehouse_sorting.collect_aisle_going_north()

    assert len(faced_north) == 1
    assert len(moves) == 2
    assert len(picks) == 2


def test_warehouse_collect_aisle_going_south_picks_expected_cells(monkeypatch):
    front_states = iter([True, True, False])
    beeper_states = iter([False, True, True])
    moves = []
    picks = []
    faced_south = []

    monkeypatch.setattr(warehouse_sorting, 'face_south', lambda: faced_south.append(True))
    monkeypatch.setattr(builtins, 'front_is_clear', lambda: next(front_states), raising=False)
    monkeypatch.setattr(builtins, 'beepers_present', lambda: next(beeper_states), raising=False)
    monkeypatch.setattr(builtins, 'move', lambda: moves.append('move'), raising=False)
    monkeypatch.setattr(builtins, 'pick_beeper', lambda: picks.append('pick'), raising=False)

    warehouse_sorting.collect_aisle_going_south()

    assert len(faced_south) == 1
    assert len(moves) == 2
    assert len(picks) == 2


def test_traffic_clear_street_eastward_picks_on_path(monkeypatch):
    front_states = iter([True, True, False])
    beeper_states = iter([True, True, False])
    moves = []
    picks = []
    faced_east = []

    monkeypatch.setattr(traffic_cleanup, 'face_east', lambda: faced_east.append(True))
    monkeypatch.setattr(builtins, 'front_is_clear', lambda: next(front_states), raising=False)
    monkeypatch.setattr(builtins, 'beepers_present', lambda: next(beeper_states), raising=False)
    monkeypatch.setattr(builtins, 'move', lambda: moves.append('move'), raising=False)
    monkeypatch.setattr(builtins, 'pick_beeper', lambda: picks.append('pick'), raising=False)

    traffic_cleanup.clear_street_eastward()

    assert len(faced_east) == 1
    assert len(moves) == 2
    assert len(picks) == 2


def test_traffic_clear_street_westward_picks_on_path(monkeypatch):
    front_states = iter([True, False])
    beeper_states = iter([False, True])
    moves = []
    picks = []
    faced_west = []

    monkeypatch.setattr(traffic_cleanup, 'face_west', lambda: faced_west.append(True))
    monkeypatch.setattr(builtins, 'front_is_clear', lambda: next(front_states), raising=False)
    monkeypatch.setattr(builtins, 'beepers_present', lambda: next(beeper_states), raising=False)
    monkeypatch.setattr(builtins, 'move', lambda: moves.append('move'), raising=False)
    monkeypatch.setattr(builtins, 'pick_beeper', lambda: picks.append('pick'), raising=False)

    traffic_cleanup.clear_street_westward()

    assert len(faced_west) == 1
    assert len(moves) == 1
    assert len(picks) == 1


def test_traffic_move_to_next_street_from_east_when_open(monkeypatch):
    events = []

    monkeypatch.setattr(builtins, 'turn_left', lambda: events.append('turn_left'), raising=False)
    monkeypatch.setattr(builtins, 'front_is_clear', lambda: True, raising=False)
    monkeypatch.setattr(builtins, 'move', lambda: events.append('move'), raising=False)

    moved = traffic_cleanup.move_to_next_street(True)

    assert moved is True
    assert events == ['turn_left', 'move', 'turn_left']


def test_traffic_move_to_next_street_from_west_when_blocked(monkeypatch):
    events = []

    monkeypatch.setattr(traffic_cleanup, 'turn_right', lambda: events.append('turn_right'))
    monkeypatch.setattr(builtins, 'front_is_clear', lambda: False, raising=False)
    monkeypatch.setattr(builtins, 'move', lambda: events.append('move'), raising=False)

    moved = traffic_cleanup.move_to_next_street(False)

    assert moved is False
    assert events == ['turn_right']


def test_traffic_clear_city_grid_processes_ten_rows(monkeypatch):
    calls = []

    monkeypatch.setattr(
        traffic_cleanup,
        'clear_street_eastward',
        lambda: calls.append('east'),
    )
    monkeypatch.setattr(
        traffic_cleanup,
        'clear_street_westward',
        lambda: calls.append('west'),
    )
    monkeypatch.setattr(
        traffic_cleanup,
        'move_to_next_street',
        lambda going_east: True,
    )

    traffic_cleanup.clear_city_grid()

    assert len(calls) == 10
    assert calls == [
        'east',
        'west',
        'east',
        'west',
        'east',
        'west',
        'east',
        'west',
        'east',
        'west',
    ]


def test_hospital_enter_room_and_deliver_places_two_beepers(monkeypatch):
    events = []

    monkeypatch.setattr(builtins, 'turn_left', lambda: events.append('turn_left'), raising=False)
    monkeypatch.setattr(builtins, 'move', lambda: events.append('move'), raising=False)
    monkeypatch.setattr(
        hospital_delivery,
        'place_multiple_beepers',
        lambda count: events.append(f'place_{count}'),
    )
    monkeypatch.setattr(hospital_delivery, 'turn_around', lambda: events.append('turn_around'))
    monkeypatch.setattr(hospital_delivery, 'turn_right', lambda: events.append('turn_right'))

    hospital_delivery.enter_room_and_deliver()

    assert events == [
        'turn_left',
        'move',
        'place_2',
        'turn_around',
        'move',
        'turn_right',
    ]


def test_hospital_move_to_room_entrance_faces_east(monkeypatch):
    events = []
    front_states = iter([True, True, False])

    monkeypatch.setattr(hospital_delivery, 'face_east', lambda: events.append('face_east'))
    monkeypatch.setattr(builtins, 'move', lambda: events.append('move'), raising=False)
    monkeypatch.setattr(builtins, 'left_is_blocked', lambda: next(front_states), raising=False)

    hospital_delivery.move_to_room_entrance()

    assert events == ['face_east', 'move', 'move', 'move']


def test_rescue_navigate_city_pickup_and_final_drop(monkeypatch):
    moves = []
    picks = []
    placed = []

    monkeypatch.setattr(builtins, 'turn_left', lambda: None, raising=False)
    monkeypatch.setattr(rescue_navigation, 'turn_right', lambda: None)
    monkeypatch.setattr(builtins, 'move', lambda: moves.append('move'), raising=False)
    monkeypatch.setattr(builtins, 'beepers_present', lambda: True, raising=False)
    monkeypatch.setattr(builtins, 'pick_beeper', lambda: picks.append('pick'), raising=False)
    monkeypatch.setattr(
        rescue_navigation,
        'place_multiple_beepers',
        lambda count: placed.append(count),
    )

    rescue_navigation.navigate_city()

    assert len(moves) == 11
    assert len(picks) == 1
    assert placed == [3]


def test_rescue_navigate_city_no_pick_when_absent(monkeypatch):
    picks = []

    monkeypatch.setattr(builtins, 'turn_left', lambda: None, raising=False)
    monkeypatch.setattr(rescue_navigation, 'turn_right', lambda: None)
    monkeypatch.setattr(builtins, 'move', lambda: None, raising=False)
    monkeypatch.setattr(builtins, 'beepers_present', lambda: False, raising=False)
    monkeypatch.setattr(builtins, 'pick_beeper', lambda: picks.append('pick'), raising=False)
    monkeypatch.setattr(rescue_navigation, 'place_multiple_beepers', lambda count: None)

    rescue_navigation.navigate_city()

    assert picks == []
