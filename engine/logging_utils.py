"""
Mission logging utilities.
"""



def log_start(mission_name):
    print('=================================')
    print('MISSION START:', mission_name)
    print('=================================')



def log_complete(mission_name):
    print('=================================')
    print('MISSION COMPLETE:', mission_name)
    print('=================================')



def log_event(event_name):
    print('[EVENT]', event_name)