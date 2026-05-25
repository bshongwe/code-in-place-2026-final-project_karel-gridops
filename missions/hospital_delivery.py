# from stanfordkarel import *
from stanfordkarel import run_karel_program
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
    for i in range(3):
        move_to_room()
        place_multiple_beepers(2)
        return_to_corridor()



def move_to_room():
    move()
    turn_left()
    move()



def return_to_corridor():
    turn_left()
    turn_left()
    move()
    turn_left()


if __name__ == '__main__':
    run_karel_program('worlds/hospital.w')