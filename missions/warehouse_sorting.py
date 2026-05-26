# from stanfordkarel import *
from stanfordkarel import run_karel_program
from engine.navigation import return_home
from engine.navigation import turn_right
from engine.navigation import face_north
from engine.navigation import face_south
from engine.navigation import face_east
from engine.navigation import turn_around
from engine.beeper_logic import collect_all_beepers
from engine.logging_utils import log_start
from engine.logging_utils import log_complete
from analytics.mission_stats import complete_mission
from analytics.mission_stats import print_stats


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


if __name__ == '__main__':
    run_karel_program('worlds/warehouse.w')



def process_warehouse():
    # World-aware traversal: process each aisle (odd-numbered avenues)
    # starting at avenue 1, street 1, facing East.
    while True:
        collect_current_aisle()

        # attempt to step two avenues east to next aisle
        face_east()
        if not front_is_clear():
            break
        move()
        if not front_is_clear():
            break
        move()



def process_aisle():
    while front_is_clear():
        collect_all_beepers()
        move()

    collect_all_beepers()



def move_to_next_aisle():
    face_east()
    if front_is_clear():
        move()
    else:
        return

    if front_is_clear():
        move()
    else:
        return



def collect_aisle_going_north():
    face_north()
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()
    if beepers_present():
        pick_beeper()



def collect_aisle_going_south():
    face_south()
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()
    if beepers_present():
        pick_beeper()



def cross_to_next_aisle():
    face_north()
    while front_is_clear():
        move()
    face_east()
    move()
    move()


def collect_current_aisle():
    # Assumes Karel is at bottom of an aisle facing East.
    # Move into the aisle, sweep from bottom to top picking beepers,
    # and return to the bottom facing East.
    # Face north and ascend
    turn_left()
    while True:
        if beepers_present():
            pick_beeper()
        if not front_is_clear():
            break
        move()

    # at top of aisle; pick beeper if present
    if beepers_present():
        pick_beeper()

    # return to bottom
    turn_left()
    turn_left()
    while front_is_clear():
        move()

    # now facing south at bottom; orient east for next step
    turn_left()
