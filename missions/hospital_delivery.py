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
    deliver_to_current_room()
    move_to_next_room()
    deliver_to_current_room()
    move_to_next_room()
    deliver_to_current_room()
    move()



def deliver_to_current_room():
    move()
    turn_left()
    climb_room_column()
    place_multiple_beepers(2)
    return_to_corridor()



def climb_room_column():
    while front_is_clear():
        move()



def move_to_next_room():
    move()



def return_to_corridor():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()


if __name__ == '__main__':
    import sys

    world_path = sys.argv[1] if len(sys.argv) > 1 else 'worlds/hospital_delivery.w'
    del sys
    run_karel_program(world_path)