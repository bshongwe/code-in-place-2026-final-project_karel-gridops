performance_tracker = {
    'best_run_moves': None,
    'best_run_beepers': None
}



def update_best_run(moves, beepers):
    if performance_tracker['best_run_moves'] is None or moves < performance_tracker['best_run_moves']:
        performance_tracker['best_run_moves'] = moves

    if performance_tracker['best_run_beepers'] is None or beepers > performance_tracker['best_run_beepers']:
        performance_tracker['best_run_beepers'] = beepers