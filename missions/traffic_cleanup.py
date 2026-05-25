# from stanfordkarel import *
from stanfordkarel import run_karel_program
from engine.beeper_logic import collect_all_beepers
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
    for i in range(5):
        clear_street()

        if left_is_clear():
            move_to_next_street()



def clear_street():
    while front_is_clear():
        collect_all_beepers()
        move()

    collect_all_beepers()



def move_to_next_street():
    turn_left()
    move()
    turn_left()


if __name__ == '__main__':
    run_karel_program('worlds/city_grid.w')