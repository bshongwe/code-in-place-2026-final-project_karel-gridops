performance_tracker = {
    'best_run_moves': 0,
    'best_run_beepers': 0
}



def update_best_run(moves, beepers):
    if performance_tracker['best_run_moves'] == 0:
        performance_tracker['best_run_moves'] = moves

    if performance_tracker['best_run_beepers'] == 0:
        performance_tracker['best_run_beepers'] = beepers