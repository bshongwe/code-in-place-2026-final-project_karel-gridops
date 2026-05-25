from stanfordkarel import *
from analytics.mission_stats import record_beeper_collection



def collect_all_beepers():
    while beepers_present():
        pick_beeper()
        record_beeper_collection()



def place_multiple_beepers(count):
    for i in range(count):
        put_beeper()



def safe_pick_beeper():
    if beepers_present():
        pick_beeper()
        record_beeper_collection()