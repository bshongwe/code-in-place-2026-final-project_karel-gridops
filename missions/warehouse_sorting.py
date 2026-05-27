# from stanfordkarel import *
from stanfordkarel import run_karel_program
from engine.navigation import return_home
from analytics.mission_stats import record_beeper_collection
from analytics.mission_stats import record_move
from engine.logging_utils import log_start
from engine.logging_utils import log_complete
from analytics.mission_stats import complete_mission
from analytics.mission_stats import print_stats


DEBUG = False


"""
Warehouse Sorting Mission
-------------------------
Karel traverses warehouse aisles,
collects inventory,
and returns to the dock.
"""



def main():
    log_start('Warehouse Sorting')

    process_warehouse()
    return_home()

    log_complete('Warehouse Sorting')
    complete_mission()
    print_stats()


def process_warehouse():
    # World-aware scan: traverse every reachable column.
    # Start at bottom-left, sweep up first column, then for each next
    # column (moved at top boundary) sweep down and back up.
    sweep_column_north_collect()

    while move_to_next_column_at_top():
        sweep_column_south_collect()
        sweep_column_north_collect()



def sweep_column_north_collect():
    # Sweep from bottom to top in the current column.
    face_north()

    while True:
        if beepers_present():
            pick_beeper()
            record_beeper_collection()
            if DEBUG:
                print('picked beeper')

        if not front_is_clear():
            break

        move()
        record_move()

    if beepers_present():
        pick_beeper()
        record_beeper_collection()
        if DEBUG:
            print('picked beeper')


def sweep_column_south_collect():
    # Sweep from top to bottom in the current column.
    face_south()

    while True:
        if beepers_present():
            pick_beeper()
            record_beeper_collection()
            if DEBUG:
                print('picked beeper')

        if not front_is_clear():
            break

        move()
        record_move()

    if beepers_present():
        pick_beeper()
        record_beeper_collection()
        if DEBUG:
            print('picked beeper')


def move_to_next_column_at_top():
    # Move one column east along the top boundary.
    face_east()
    if not front_is_clear():
        return False

    move()
    record_move()
    return True


def sweep_current_aisle():
    # Backward-compatible alias for older tests/helpers.
    sweep_column_north_collect()


def cross_to_next_aisle():
    # Backward-compatible alias for older tests/helpers.
    moved_once = move_to_next_column_at_top()
    if not moved_once:
        return

    # Try one more step to preserve old two-column hop behavior when needed.
    if front_is_clear():
        move()
        record_move()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def face_north():
    while not_facing_north():
        turn_left()


def face_south():
    while not_facing_south():
        turn_left()


def face_east():
    while not_facing_east():
        turn_left()


if __name__ == '__main__':
    run_karel_program('worlds/warehouse_sorting.w')
