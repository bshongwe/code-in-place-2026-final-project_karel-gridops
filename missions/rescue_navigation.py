# from stanfordkarel import *
from stanfordkarel import run_karel_program
from engine.navigation import turn_right
from engine.beeper_logic import place_multiple_beepers
from engine.logging_utils import log_start
from engine.logging_utils import log_complete
from analytics.mission_stats import complete_mission
from analytics.mission_stats import print_stats


"""
Disaster Rescue Mission
-----------------------
Karel delivers emergency supplies
across damaged city sectors.
"""



def main():
    log_start('Rescue Navigation')

    navigate_city()

    log_complete('Rescue Navigation')
    complete_mission()
    print_stats()



def navigate_city():
    while front_is_clear():
        move()

        if no_beepers_present():
            put_beeper()

    deliver_final_supplies()



def deliver_final_supplies():
    turn_right()

    if front_is_clear():
        move()
        place_multiple_beepers(3)


if __name__ == '__main__':
    run_karel_program('worlds/rescue.w')