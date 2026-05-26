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
    # The warehouse has four aisles in columns 1, 3, 5, and 7.
    for aisle_index in range(4):
        sweep_current_aisle()

        if aisle_index < 3:
            cross_to_next_aisle()



def sweep_current_aisle():
    # Sweep from the bottom of the aisle to the top, collecting beepers as we go.
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


def cross_to_next_aisle():
    # We are at the top of an aisle facing north.
    face_east()
    move()
    record_move()
    move()
    record_move()

    face_south()
    while front_is_clear():
        move()
        record_move()

    face_east()


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
    run_karel_program('worlds/warehouse.w')
