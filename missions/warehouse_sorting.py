# from stanfordkarel import *
from stanfordkarel import run_karel_program
from engine.navigation import return_home
from engine.navigation import turn_right
from engine.navigation import face_north
from engine.navigation import face_south
from engine.navigation import face_east
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

    collect_aisle_going_north()
    cross_to_next_aisle()
    collect_aisle_going_south()
    cross_to_next_aisle()
    collect_aisle_going_south()
    cross_to_next_aisle()
    collect_aisle_going_south()
    return_home()

    log_complete('Warehouse Sorting')
    complete_mission()
    print_stats()


if __name__ == '__main__':
    run_karel_program('worlds/warehouse.w')



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



def process_warehouse():
    for i in range(4):
        process_aisle()
        move_to_next_aisle()



def process_aisle():
    while front_is_clear():
        collect_all_beepers()
        move()

    collect_all_beepers()



def move_to_next_aisle():
    if facing_north():
        turn_right()
        move()
        turn_right()
    else:
        turn_left()
        move()
        turn_left()