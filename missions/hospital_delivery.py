# from stanfordkarel import *
from stanfordkarel import run_karel_program
from engine.navigation import turn_around
from engine.navigation import turn_right
from engine.navigation import face_east
from engine.beeper_logic import place_multiple_beepers
from engine.logging_utils import log_start
from engine.logging_utils import log_complete
from analytics.mission_stats import complete_mission
from analytics.mission_stats import print_stats


"""
Hospital Delivery Mission
-------------------------
Karel delivers medicine
through hospital corridors.
"""



def main():
    log_start('Hospital Delivery')

    deliver_medicine()

    log_complete('Hospital Delivery')
    complete_mission()
    print_stats()



def deliver_medicine():
    move_to_room_entrance()
    enter_room_and_deliver()
    move_to_room_entrance()
    enter_room_and_deliver()
    move_to_room_entrance()
    enter_room_and_deliver()



def move_to_room_entrance():
    face_east()
    move()
    while left_is_blocked():
        move()



def enter_room_and_deliver():
    turn_left()
    move()
    place_multiple_beepers(2)
    turn_around()
    move()
    turn_right()



def move_to_corridor():
    turn_left()
    move()
    move()
    turn_right()



def deliver_to_room():
    while right_is_blocked():
        move()
    turn_right()
    move()
    place_multiple_beepers(2)
    turn_around()
    move()
    turn_right()


if __name__ == '__main__':
    run_karel_program('worlds/hospital.w')