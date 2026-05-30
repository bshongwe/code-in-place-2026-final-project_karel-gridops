import os
import subprocess
from pathlib import Path
import sys


MISSIONS = {
    '1': ('Warehouse Sorting', 'missions/warehouse_sorting.py', None),
    '2': ('Hospital Delivery', 'missions/hospital_delivery.py', {
        '1': ('Hospital', 'worlds/hospital.w'),
        '2': ('Hospital Delivery', 'worlds/hospital_delivery.w'),
    }),
    '3': ('Rescue Navigation', 'missions/rescue_navigation.py', {
        '1': ('Rescue', 'worlds/rescue.w'),
        '2': ('Rescue Navigation', 'worlds/rescue_navigation.w'),
    }),
    '4': ('Traffic Cleanup',   'missions/traffic_cleanup.py', {
        '1': ('City Grid', 'worlds/city_grid.w'),
        '2': ('Traffic Cleanup', 'worlds/traffic_cleanup.w'),
    }),
    '5': ('Supply Relay',      'missions/supply_relay.py', None),
}


def select_mission():
    print('\n=== KarelGridOps Mission Selector ===')
    for key, (name, _, _) in MISSIONS.items():
        print(f'  {key}. {name}')
    choice = input('\nSelect mission (1-5): ').strip()
    return MISSIONS.get(choice)


def select_world(mission_name, worlds):
    print(f'\nSelect world for {mission_name}:')
    for key, (name, _) in worlds.items():
        print(f'  {key}. {name}')
    choice = input('\nSelect world: ').strip()
    return worlds.get(choice)


if __name__ == '__main__':
    mission = select_mission()
    if mission:
        name, path, worlds = mission
        world_path = None
        if worlds:
            world_choice = select_world(name, worlds)
            if world_choice:
                world_name, world_path = world_choice
                print(f'\nLaunching: {name} ({world_name})\n')
            else:
                print('Invalid world selection.')
                sys.exit(1)
        else:
            print(f'\nLaunching: {name}\n')

        project_root = Path(__file__).parent
        env = os.environ.copy()
        env['PYTHONPATH'] = str(project_root)
        command = [sys.executable, str(project_root / path)]
        if world_path:
            command.append(world_path)
        subprocess.run(command, cwd=str(project_root), env=env)
    else:
        print('Invalid selection.')