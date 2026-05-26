from stanfordkarel import run_karel_program
from engine.navigation import face_north, face_east, return_home, move_until_wall
from engine.beeper_logic import collect_all_beepers
from analytics.mission_stats import record_move, complete_mission, print_stats

"""
Assembly Line Mission (minimal deterministic)
- Move north one cell to assembly row
- Sweep east across the row, collect any beepers
- Return home and finish
"""


def run_mission():
    # Move to assembly row (north one cell) if possible
    face_north()
    if front_is_clear():
        move()
        record_move()

    # Sweep east across this row, collecting beepers
    face_east()
    # collect at starting cell
    collect_all_beepers()
    while front_is_clear():
        move()
        record_move()
        collect_all_beepers()

    # Return to home corner (west then south)
    return_home()


def main():
    run_mission()
    complete_mission()
    print_stats()


if __name__ == '__main__':
    run_karel_program('worlds/assembly_line.w')
