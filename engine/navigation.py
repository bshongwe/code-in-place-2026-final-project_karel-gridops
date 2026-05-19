from stanfordkarel import *



def turn_right():
    for i in range(3):
        turn_left()



def turn_around():
    turn_left()
    turn_left()



def move_until_wall():
    while front_is_clear():
        move()



def face_north():
    while not_facing_north():
        turn_left()



def face_south():
    while not_facing_south():
        turn_left()



def face_east():
    while not_facing_east():
        turn_left()



def face_west():
    while not_facing_west():
        turn_left()



def return_home():
    face_west()
    move_until_wall()

    face_south()
    move_until_wall()

    face_east()