from analytics.performance_tracker import update_best_run


mission_stats = {
    'moves': 0,
    'beepers_collected': 0,
    'missions_completed': 0
}



def record_move():
    mission_stats['moves'] += 1



def record_beeper_collection():
    mission_stats['beepers_collected'] += 1



def complete_mission():
    mission_stats['missions_completed'] += 1
    update_best_run(mission_stats['moves'], mission_stats['beepers_collected'])



def print_stats():
    print('Mission Statistics')
    print(mission_stats)