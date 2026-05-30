# from stanfordkarel import *
from stanfordkarel import run_karel_program
from engine.logging_utils import log_start
from engine.logging_utils import log_complete
from analytics.mission_stats import complete_mission
from analytics.mission_stats import print_stats


"""
Traffic Cleanup Mission
-----------------------
Karel clears traffic hazards
across city intersections.
"""



def main():
    log_start('Traffic Cleanup')

    clear_city_grid()

    log_complete('Traffic Cleanup')
    complete_mission()
    print_stats()



def clear_city_grid():
    total_rows = 10
    going_east = True

    for row_index in range(total_rows):
        if going_east:
            clear_street_eastward()
        else:
            clear_street_westward()

        if row_index == total_rows - 1:
            break

        if not move_to_next_street(going_east):
            break

        going_east = not going_east



def clear_street_eastward():
    face_east()
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()
    if beepers_present():
        pick_beeper()



def clear_street_westward():
    face_west()
    while front_is_clear():
        if beepers_present():
            pick_beeper()
        move()
    if beepers_present():
        pick_beeper()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def face_east():
    while not_facing_east():
        turn_left()


def face_west():
    while not_facing_west():
        turn_left()



def move_to_next_street(going_east):
    if going_east:
        turn_left()
    else:
        turn_right()

    if not front_is_clear():
        return False

    move()

    if going_east:
        turn_left()
    else:
        turn_right()

    return True


if __name__ == '__main__':
    import sys

    world_path = sys.argv[1] if len(sys.argv) > 1 else 'worlds/traffic_cleanup.w'
    del sys
    run_karel_program(world_path)