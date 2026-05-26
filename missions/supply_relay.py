from stanfordkarel import *
from engine.logging_utils import log_start, log_complete
from analytics.mission_stats import record_move, complete_mission, print_stats


"""
Supply Relay Mission
--------------------
Karel follows a simple corridor route, collects relay beepers,
and returns to the start.
"""


def main():
    log_start('Supply Relay')

    run_relay_route()

    log_complete('Supply Relay')
    complete_mission()
    print_stats()


def run_relay_route():
    # Move to the relay row and sweep east across it.
    face_north()
    if front_is_clear():
        step()
        collect_here()

    face_east()
    collect_here()

    while front_is_clear():
        step()
        collect_here()

    # Finish by returning home from the far end of the row.
    return_home()


def step():
    move()
    record_move()


def collect_here():
    while beepers_present():
        pick_beeper()


def turn_around():
    turn_left()
    turn_left()


def face_north():
    while not_facing_north():
        turn_left()


def face_east():
    while not_facing_east():
        turn_left()


def face_west():
    while not_facing_west():
        turn_left()


def face_south():
    while not_facing_south():
        turn_left()


def return_home():
    face_west()
    while front_is_clear():
        step()

    turn_around()
    face_south()
    while front_is_clear():
        step()

    face_east()


if __name__ == '__main__':
    from stanfordkarel import run_karel_program

    run_karel_program('worlds/supply_relay.w')