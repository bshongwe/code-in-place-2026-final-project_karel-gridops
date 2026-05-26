from stanfordkarel import *
from engine.navigation import turn_right, move_until_wall, face_north, face_south, face_east, face_west
from engine.beeper_logic import collect_all_beepers, safe_pick_beeper
from analytics.mission_stats import record_move

MISSION_NAME = "Narrow Maze"
DIFFICULTY = "Intermediate"
DESCRIPTION = "Explore a narrow maze and collect beepers placed at dead-ends."

DEBUG = False

def left_is_clear():
    turn_left()
    clear = front_is_clear()
    turn_right()
    return clear


def right_is_clear():
    turn_right()
    clear = front_is_clear()
    turn_left()
    return clear


def step():
    if front_is_clear():
        move()
        record_move()
        if DEBUG:
            print("moved")
        if beepers_present():
            collect_all_beepers()


def explore_left_hand():
    # Simple left-hand wall follower to explore the maze
    for _ in range(1000):  # safety cap — extended to cover larger mazes
        if left_is_clear():
            turn_left()
            step()
        elif front_is_clear():
            step()
        else:
            turn_right()
        if DEBUG and beepers_present():
            print("found beeper at", get_karel_position() if 'get_karel_position' in globals() else "?")


def zigzag_grid_sweep(max_rows=6):
    # Perform a zig-zag sweep across rows attempting to cover reachable cells.
    # Start by ensuring we're facing east at the bottom row.
    face_east()
    for _ in range(max_rows):
        # Sweep current row to the east
        while front_is_clear():
            move()
            record_move()
            if beepers_present():
                collect_all_beepers()

        # Try to step up to the next row
        face_north()
        if front_is_clear():
            move()
            record_move()
        else:
            # No more rows upward from here
            break

        # Sweep back to the west
        face_west()
        while front_is_clear():
            move()
            record_move()
            if beepers_present():
                collect_all_beepers()

        # Try to step up again for the next iteration
        face_north()
        if front_is_clear():
            move()
            record_move()
        else:
            break


# --- Full DFS exploration with coordinate tracking ---
# We track Karel's (x,y) position starting from (1,1). This assumes
# worlds start Karel at (1,1) which is true for our puzzle set.
X = 1
Y = 1
WIDTH = None
HEIGHT = None


def get_facing():
    if not not_facing_north():
        return 'N'
    if not not_facing_south():
        return 'S'
    if not not_facing_east():
        return 'E'
    if not not_facing_west():
        return 'W'
    return None


def move_and_track():
    """Move forward, record analytics, and update X/Y."""
    global X, Y
    f = get_facing()
    move()
    record_move()
    if f == 'N':
        Y += 1
    elif f == 'S':
        Y -= 1
    elif f == 'E':
        X += 1
    elif f == 'W':
        X -= 1


def dfs_explore(visited=None):
    """Depth-first explore reachable cells, collecting beepers and backtracking."""
    global X, Y
    if visited is None:
        visited = set()

    visited.add((X, Y))
    if beepers_present():
        collect_all_beepers()

    # Try directions N, E, S, W
    for face, dx, dy, face_fn in (
        ('N', 0, 1, face_north),
        ('E', 1, 0, face_east),
        ('S', 0, -1, face_south),
        ('W', -1, 0, face_west),
    ):
        face_fn()
        if front_is_clear():
            nx = X + dx
            ny = Y + dy
            if (nx, ny) not in visited:
                move_and_track()
                dfs_explore(visited)
                # backtrack
                turn_left(); turn_left()
                move_and_track()
                turn_left(); turn_left()


def probe_face(face_fn):
    """Probe distance to the wall in the given facing, return steps, and restore position+facing."""
    start_face = get_facing()
    face_fn()
    cnt = 0
    while front_is_clear():
        move()
        cnt += 1

    # move back to start
    turn_left(); turn_left()
    for _ in range(cnt):
        move()

    # restore original facing
    if start_face == 'N':
        face_north()
    elif start_face == 'S':
        face_south()
    elif start_face == 'E':
        face_east()
    elif start_face == 'W':
        face_west()

    return cnt


def probe_world_dimensions():
    """Use sensors to compute full world width and height and set globals."""
    global WIDTH, HEIGHT, X, Y
    # measure from current starting cell how many steps to each wall
    east = probe_face(face_east)
    west = probe_face(face_west)
    north = probe_face(face_north)
    south = probe_face(face_south)

    WIDTH = west + east + 1
    HEIGHT = south + north + 1

    # Derive current coordinates (assuming 1-based grid with walls at edges)
    X = west + 1
    Y = south + 1

    if DEBUG:
        print(f'Probed WIDTH={WIDTH}, HEIGHT={HEIGHT}, start X={X}, Y={Y}')



def run_mission():
    # Probe the world to determine width/height using sensors
    probe_world_dimensions()

    # Start with a DFS exploration to cover all reachable cells
    dfs_explore()

    # As an extra pass, perform a zig-zag sweep across the probed height
    if HEIGHT:
        zigzag_grid_sweep(max_rows=HEIGHT)


def main():
    run_mission()


if __name__ == '__main__':
    # Keep the run_karel_program call at file end per project convention
    from stanfordkarel import run_karel_program

    run_karel_program('worlds/narrow_maze.w')
