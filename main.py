import os
import subprocess
from pathlib import Path
import sys


MISSIONS = {
    '1': ('Warehouse Sorting', 'missions/warehouse_sorting.py'),
    '2': ('Hospital Delivery', 'missions/hospital_delivery.py'),
    '3': ('Rescue Navigation', 'missions/rescue_navigation.py'),
    '4': ('Traffic Cleanup',   'missions/traffic_cleanup.py'),
}


def select_mission():
    print('\n=== KarelGridOps Mission Selector ===')
    for key, (name, _) in MISSIONS.items():
        print(f'  {key}. {name}')
    choice = input('\nSelect mission (1-4): ').strip()
    return MISSIONS.get(choice)


if __name__ == '__main__':
    mission = select_mission()
    if mission:
        name, path = mission
        print(f'\nLaunching: {name}\n')
        project_root = Path(__file__).parent
        env = os.environ.copy()
        env['PYTHONPATH'] = str(project_root)
        subprocess.run([sys.executable, str(project_root / path)], cwd=str(project_root), env=env)
    else:
        print('Invalid selection.')