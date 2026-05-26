import engine.beeper_logic as beeper_logic


def test_collect_all_beepers_picks_until_empty(monkeypatch):
    states = iter([True, True, False])
    picked = []
    recorded = []

    monkeypatch.setattr(beeper_logic, 'beepers_present', lambda: next(states))
    monkeypatch.setattr(beeper_logic, 'pick_beeper', lambda: picked.append('pick'))
    monkeypatch.setattr(beeper_logic, 'record_beeper_collection', lambda: recorded.append('record'))

    beeper_logic.collect_all_beepers()

    assert len(picked) == 2
    assert len(recorded) == 2


def test_place_multiple_beepers_places_exact_count(monkeypatch):
    placed = []

    monkeypatch.setattr(beeper_logic, 'put_beeper', lambda: placed.append('put'))

    beeper_logic.place_multiple_beepers(4)

    assert len(placed) == 4


def test_place_multiple_beepers_with_zero_is_noop(monkeypatch):
    placed = []

    monkeypatch.setattr(beeper_logic, 'put_beeper', lambda: placed.append('put'))

    beeper_logic.place_multiple_beepers(0)

    assert placed == []


def test_safe_pick_beeper_when_present(monkeypatch):
    picked = []
    recorded = []

    monkeypatch.setattr(beeper_logic, 'beepers_present', lambda: True)
    monkeypatch.setattr(beeper_logic, 'pick_beeper', lambda: picked.append('pick'))
    monkeypatch.setattr(beeper_logic, 'record_beeper_collection', lambda: recorded.append('record'))

    beeper_logic.safe_pick_beeper()

    assert len(picked) == 1
    assert len(recorded) == 1


def test_safe_pick_beeper_when_absent(monkeypatch):
    picked = []
    recorded = []

    monkeypatch.setattr(beeper_logic, 'beepers_present', lambda: False)
    monkeypatch.setattr(beeper_logic, 'pick_beeper', lambda: picked.append('pick'))
    monkeypatch.setattr(beeper_logic, 'record_beeper_collection', lambda: recorded.append('record'))

    beeper_logic.safe_pick_beeper()

    assert picked == []
    assert recorded == []
