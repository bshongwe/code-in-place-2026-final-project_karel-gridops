import builtins

import engine.movement_patterns as movement_patterns


def test_sweep_row_moves_until_wall(monkeypatch):
	front_states = iter([True, True, False])
	events = []

	monkeypatch.setattr(movement_patterns, 'front_is_clear', lambda: next(front_states))
	monkeypatch.setattr(movement_patterns, 'move', lambda: events.append('move'))

	movement_patterns.sweep_row()

	assert events == ['move', 'move']


def test_move_to_next_row_uses_left_path_when_available(monkeypatch):
	events = []

	monkeypatch.setattr(movement_patterns, 'left_is_clear', lambda: True)
	monkeypatch.setattr(movement_patterns, 'right_is_clear', lambda: False)
	monkeypatch.setattr(movement_patterns, 'turn_left', lambda: events.append('turn_left'))
	monkeypatch.setattr(movement_patterns, 'move', lambda: events.append('move'))

	movement_patterns.move_to_next_row()

	assert events == ['turn_left', 'move', 'turn_left']


def test_move_to_next_row_uses_right_path_when_left_blocked(monkeypatch):
	events = []

	monkeypatch.setattr(movement_patterns, 'left_is_clear', lambda: False)
	monkeypatch.setattr(movement_patterns, 'right_is_clear', lambda: True)
	monkeypatch.setattr(movement_patterns, 'turn_right', lambda: events.append('turn_right'))
	monkeypatch.setattr(movement_patterns, 'move', lambda: events.append('move'))

	movement_patterns.move_to_next_row()

	assert events == ['turn_right', 'move', 'turn_right']


def test_snake_pattern_sweeps_each_row(monkeypatch):
	events = []

	monkeypatch.setattr(movement_patterns, 'sweep_row', lambda: events.append('sweep'))
	monkeypatch.setattr(movement_patterns, 'move_to_next_row', lambda: events.append('next'))
	monkeypatch.setattr(movement_patterns, 'left_is_clear', lambda: True)
	monkeypatch.setattr(movement_patterns, 'right_is_clear', lambda: False)

	movement_patterns.snake_pattern(3)

	assert events == ['sweep', 'next', 'sweep', 'next', 'sweep', 'next']
