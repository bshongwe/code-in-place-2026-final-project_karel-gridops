from stanfordkarel import *
from engine.navigation import return_home
from engine.beeper_logic import collect_all_beepers
from engine.logging_utils import log_start
from engine.logging_utils import log_complete


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



def process_warehouse():
    for i in range(4):
        process_aisle()

        if left_is_clear():
            move_to_next_aisle()



def process_aisle():
    while front_is_clear():
        collect_all_beepers()
        move()

    collect_all_beepers()



def move_to_next_aisle():
    turn_left()
    move()
    turn_left()