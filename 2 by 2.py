def print_puzzle(state):
    for row in state:
        print(' '.join(map(str, row)))
    print()

def get_neighbors(state):
    x, y = next((ix, iy) for ix, row in enumerate(state) for iy, i in enumerate(row) if i == 0)
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 2 and 0 <= new_y < 2:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def is_goal(state, goal):
    return state == goal

def sliding_puzzle(start, goal):
    from collections import deque

    queue = deque([(start, [start])])  # (current state, path taken)
    visited = set()
    
    while queue:
        current, path = queue.popleft()
        
        if is_goal(current, goal):
            return path
        
        visited.add(tuple(map(tuple, current)))  # Add current state to visited
        
        for neighbor in get_neighbors(current):
            if tuple(map(tuple, neighbor)) not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return None

def main():
    start_state = [[1, 2], [0, 3]]  # Valid start state
    goal_state = [[1, 2], [3, 0]]    # Goal state

    print("Solving 2x2 puzzle:")
    path = sliding_puzzle(start_state, goal_state)

    if path:
        for state in path:
            print_puzzle(state)
    else:
        print("No path found")

if __name__ == "__main__":
    main()
