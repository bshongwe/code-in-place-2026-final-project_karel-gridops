from stanfordkarel import *



def collect_all_beepers():
    while beepers_present():
        pick_beeper()



def place_multiple_beepers(count):
    for i in range(count):
        put_beeper()



def safe_pick_beeper():
    if beepers_present():
        pick_beeper()