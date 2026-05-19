from karel.stanfordkarel import *
from engine.navigation import turn_right



def sweep_row():
    while front_is_clear():
        move()



def snake_pattern(rows):
    for i in range(rows):
        sweep_row()

        if left_is_clear() or right_is_clear():
            move_to_next_row()



def move_to_next_row():
    if left_is_clear():
        turn_left()
        move()
        turn_left()

    elif right_is_clear():
        turn_right()
        move()
        turn_right()