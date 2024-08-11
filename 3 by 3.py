# Print puzzle state
def print_puzzle(state):
    for row in state:
        print(' '.join(map(str, row)))
    print()  # Print a new line for better readability

# Manhattan distance heuristic
def manhattan_distance(state, goal):
    flat_goal = [val for row in goal for val in row]
    return sum(
        abs(i - goal_index // 3) + abs(j - goal_index % 3)
        for i, row in enumerate(state) for j, val in enumerate(row)
        if val != 0 and (goal_index := flat_goal.index(val)) is not None
    )

# Get neighbors of the current state
def get_neighbors(state):
    x, y = next((ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0)
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# A* search algorithm
def a_star(start, goal):
    open_set = [(manhattan_distance(start, goal), start)]
    came_from, g_score, f_score = {}, {str(start): 0}, {str(start): manhattan_distance(start, goal)}
    nodes_expanded = 0

    while open_set:
        open_set.sort()  # Sort by priority (f_score)
        _, current = open_set.pop(0)  # Get the state with the lowest f_score

        if current == goal:
            return reconstruct_path(came_from, current), nodes_expanded

        nodes_expanded += 1
        for neighbor in get_neighbors(current):
            key = str(neighbor)
            tentative_g = g_score[str(current)] + 1
            if key not in g_score or tentative_g < g_score[key]:
                came_from[key] = current
                g_score[key] = tentative_g
                f = tentative_g + manhattan_distance(neighbor, goal)
                if not any(neighbor == item[1] for item in open_set):
                    open_set.append((f, neighbor))

    return None, nodes_expanded

# Reconstruct path for A* search
def reconstruct_path(came_from, current):
    path = [current]
    while str(current) in came_from:
        current = came_from[str(current)]
        path.append(current)
    return path[::-1]

# Brute force search algorithm
def brute_force(start, goal):
    queue, visited = [start], {str(start)}
    came_from, nodes_expanded = {}, 0

    while queue:
        current = queue.pop(0)
        if current == goal:
            return reconstruct_path(came_from, current), nodes_expanded

        nodes_expanded += 1
        for neighbor in get_neighbors(current):
            key = str(neighbor)
            if key not in visited:
                visited.add(key)
                queue.append(neighbor)
                came_from[key] = current

    return None, nodes_expanded

# Main function to solve the 3x3 puzzle
def solve_puzzle_3x3():
    start = [[8 , 7 ,6], [5, 4, 3], [2, 1, 0]]  # Example start state
    goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # Goal state

    print("Solving 3x3 puzzle using A* search:")
    path, nodes_expanded = a_star(start, goal)
    if path:
        for step in path:
            print_puzzle(step)
    else:
        print("No path found")
    print("Nodes expanded:", nodes_expanded)

    print("Solving 3x3 puzzle using brute force:")
    path, nodes_expanded = brute_force(start, goal)
    if path:
        for step in path:
            print_puzzle(step)
    else:
        print("No path found")
    print("Nodes expanded:", nodes_expanded)

solve_puzzle_3x3()
