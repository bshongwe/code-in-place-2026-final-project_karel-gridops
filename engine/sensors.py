from karel.stanfordkarel import *



def front_blocked():
    return not front_is_clear()



def left_blocked():
    return not left_is_clear()



def right_blocked():
    return not right_is_clear()



def beeper_detected():
    return beepers_present()