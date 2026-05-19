from stanfordkarel import *
from engine.navigation import turn_right
from engine.beeper_logic import place_multiple_beepers
from engine.logging_utils import log_start
from engine.logging_utils import log_complete


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
    main()