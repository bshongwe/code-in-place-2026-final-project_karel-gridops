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
    move_to_first_room()
    deliver_to_room()
    move_to_next_room()
    deliver_to_room()
    move_to_next_room()
    deliver_to_room()



def move_to_first_room():
    move()
    turn_left()
    move()



def move_to_next_room():
    move()
    move()



def deliver_to_room():
    place_multiple_beepers(2)
    turn_left()
    turn_left()
    move()
    turn_right()


if __name__ == '__main__':
    run_karel_program('worlds/hospital.w')