import sys

GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

MOVES = {
    'UP': (-1, 0),
    'DOWN': (1, 0),
    'LEFT': (0, -1),
    'RIGHT': (0, 1)
}

def find_blank(state):
    """Locate the row and column of the empty tile (0)."""
    for r in range(3):
        for c in range(3):
            if state[r][c] == 0:
                return r, c

def get_neighbors(state):
    """Generate all valid next states from the current state."""
    r, c = find_blank(state)
    neighbors = []
    
    for move, (dr, dc) in MOVES.items():
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            grid_list = [list(row) for row in state]
            grid_list[r][c], grid_list[nr][nc] = grid_list[nr][nc], grid_list[r][c]
            next_state = tuple(tuple(row) for row in grid_list)
            neighbors.append((next_state, move))
            
    return neighbors

def dfs_recursive(state, path, visited, depth_limit):
    """Core Recursive DFS Function."""
    if state == GOAL_STATE:
        return path
    
    if len(path) >= depth_limit:
        return None
    
    visited.add(state)
    
    for next_state, move in get_neighbors(state):
        if next_state not in visited:
            result = dfs_recursive(next_state, path + [move], visited, depth_limit)
            if result is not None:
                return result 
                
    visited.remove(state)
    return None

def solve_dfs(start_state, max_depth=20):
    """Wrapper function to invoke depth-limited DFS."""
    visited = set()
    return dfs_recursive(start_state, [], visited, max_depth)

# -------------------------------------------------------------
# NEW: Iterative Deepening Search (IDS)
# -------------------------------------------------------------
def solve_ids(start_state, max_depth=20):
    """Loop depth from 0 to max_depth and run DFS at each level."""
    for depth in range(max_depth + 1):
        visited = set()
        result = dfs_recursive(start_state, [], visited, depth)
        if result is not None:
            return result, depth  # Return path and the depth where it was found
    return None, max_depth


if __name__ == "__main__":
    initial_state = (
        (1, 2, 3),
        (4, 0, 6),
        (7, 5, 8)
    )

    print("=== 1. DFS Search ===")
    dfs_path = solve_dfs(initial_state, max_depth=15)
    if dfs_path is not None:
        print(f"Solution Found in {len(dfs_path)} moves!")
        print("Move Sequence:", " -> ".join(dfs_path))
    else:
        print("No solution found within the specified depth limit.")

    print("\n=== 2. IDS Search ===")
    ids_path, depth_found = solve_ids(initial_state, max_depth=15)
    if ids_path is not None:
        print(f"Optimal Solution Found at Depth {depth_found} in {len(ids_path)} moves!")
        print("Move Sequence:", " -> ".join(ids_path))
    else:
        print("No solution found within the specified depth limit.")
