grid = [
    ["CLEAN", "DIRTY",    "OBSTACLE"],
    ["DIRTY", "OBSTACLE", "DIRTY"],
    ["CLEAN", "DIRTY",    "CLEAN"]
]

pos = (0, 0)
direction = "EAST"
memory = {pos: "CLEAN"}  
moves = {
    "NORTH": (-1, 0),
    "EAST":  (0, 1),
    "SOUTH": (1, 0),
    "WEST":  (0, -1)
}

turn_left = {
    "NORTH": "WEST",
    "WEST":  "SOUTH",
    "SOUTH": "EAST",
    "EAST":  "NORTH"
}

for step in range(1, 9):
    r, c = pos
    dr, dc = moves[direction]
    nr, nc = r + dr, c + dc

    is_dirty = grid[r][c] == "DIRTY"
    is_obstacle = nr < 0 or nr >= 3 or nc < 0 or nc >= 3 or grid[nr][nc] == "OBSTACLE"

    if is_dirty:
        action = "SUCK"
        grid[r][c] = "CLEAN" 
        memory[pos] = "CLEAN" 
    elif is_obstacle:
        action = "TURN_LEFT"
        memory[(nr, nc)] = "OBSTACLE" # Record obstacle in memory
        direction = turn_left[direction]
    else:
        action = "MOVE_FORWARD"
        pos = (nr, nc)
        memory[pos] = "CLEAN"

    print(f"Step {step}: Action={action:12} | Position={pos} | Facing={direction}")
