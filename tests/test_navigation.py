import builtins

import engine.navigation as navigation


def test_turn_right_turns_left_three_times(monkeypatch):
	events = []

	monkeypatch.setattr(navigation, 'turn_left', lambda: events.append('turn_left'))

	navigation.turn_right()

	assert events == ['turn_left', 'turn_left', 'turn_left']


def test_turn_around_turns_left_twice(monkeypatch):
	events = []

	monkeypatch.setattr(navigation, 'turn_left', lambda: events.append('turn_left'))

	navigation.turn_around()

	assert events == ['turn_left', 'turn_left']


def test_move_until_wall_moves_and_records_each_step(monkeypatch):
	front_states = iter([True, True, False])
	events = []

	monkeypatch.setattr(navigation, 'front_is_clear', lambda: next(front_states))
	monkeypatch.setattr(navigation, 'move', lambda: events.append('move'))
	monkeypatch.setattr(navigation, 'record_move', lambda: events.append('record_move'))

	navigation.move_until_wall()

	assert events == ['move', 'record_move', 'move', 'record_move']


def test_face_north_turns_until_aligned(monkeypatch):
	states = iter([True, True, False])
	events = []

	monkeypatch.setattr(navigation, 'not_facing_north', lambda: next(states))
	monkeypatch.setattr(navigation, 'turn_left', lambda: events.append('turn_left'))

	navigation.face_north()

	assert events == ['turn_left', 'turn_left']


def test_face_south_turns_until_aligned(monkeypatch):
	states = iter([True, False])
	events = []

	monkeypatch.setattr(navigation, 'not_facing_south', lambda: next(states))
	monkeypatch.setattr(navigation, 'turn_left', lambda: events.append('turn_left'))

	navigation.face_south()

	assert events == ['turn_left']


def test_face_east_turns_until_aligned(monkeypatch):
	states = iter([True, True, False])
	events = []

	monkeypatch.setattr(navigation, 'not_facing_east', lambda: next(states))
	monkeypatch.setattr(navigation, 'turn_left', lambda: events.append('turn_left'))

	navigation.face_east()

	assert events == ['turn_left', 'turn_left']


def test_face_west_turns_until_aligned(monkeypatch):
	states = iter([True, False])
	events = []

	monkeypatch.setattr(navigation, 'not_facing_west', lambda: next(states))
	monkeypatch.setattr(navigation, 'turn_left', lambda: events.append('turn_left'))

	navigation.face_west()

	assert events == ['turn_left']


def test_return_home_calls_waypoints_in_order(monkeypatch):
	events = []

	monkeypatch.setattr(navigation, 'face_west', lambda: events.append('face_west'))
	monkeypatch.setattr(navigation, 'move_until_wall', lambda: events.append('move_until_wall'))
	monkeypatch.setattr(navigation, 'face_south', lambda: events.append('face_south'))
	monkeypatch.setattr(navigation, 'face_east', lambda: events.append('face_east'))

	navigation.return_home()

	assert events == ['face_west', 'move_until_wall', 'face_south', 'move_until_wall', 'face_east']
