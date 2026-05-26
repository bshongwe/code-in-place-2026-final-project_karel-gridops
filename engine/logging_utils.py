"""
Mission logging utilities.
"""
from pathlib import Path
from stanfordkarel.karel_application import KarelApplication


_original_load_world = getattr(KarelApplication, '_original_load_world', KarelApplication.load_world)


def _patched_load_world(self):
    world_before = self.world.world_file
    _original_load_world(self)
    world_after = self.world.world_file
    if world_after != world_before:
        print('[WORLD] Loaded:', Path(world_after).name)


KarelApplication._original_load_world = _original_load_world
KarelApplication.load_world = _patched_load_world



def log_start(mission_name):
    print('=================================')
    print('MISSION START:', mission_name)
    print('=================================')



def log_complete(mission_name):
    print('=================================')
    print('MISSION COMPLETE:', mission_name)
    print('=================================')



def log_world_loaded(world_file):
    print('[WORLD] Loaded:', Path(world_file).name)



def log_event(event_name):
    print('[EVENT]', event_name)