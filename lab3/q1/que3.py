def create_cube(f_name):
    with open(f_name, "r") as f:
        lines = f.readlines()
        array_2d = [list(line.split()) for line in lines]
    return array_2d

def heuristic(node, goal):
    a1, b1 = node
    a2, b2 = goal
    return abs(a1 - a2) + abs(b1 - b2)

def astar(cube, start, goal):
    open_nodes = [(0, start)]
    closed_nodes = set()
    g_scores = {start: 0}

    while open_nodes:
        current_priority, current_state = min(open_nodes)
        open_nodes.remove((current_priority, current_state))

        if current_state == goal:
            return reconstruct(start, goal, g_scores)

        closed_nodes.add(current_state)
        neighbors = get_neighbors(cube, current_state)

        for neighbor in neighbors:
            neighbor_g_score = g_scores[current_state] + 1

            if neighbor not in g_scores or neighbor_g_score < g_scores[neighbor]:
                g_scores[neighbor] = neighbor_g_score
                priority = neighbor_g_score + heuristic(neighbor, goal)
                open_nodes.append((priority, neighbor))

    return None

def reconstruct(start, end, cost_map):
    path = [end]
    current_point = end

    while current_point != start:
        min_next_point = min(get_neighbors(cube, current_point), key=lambda neighbor: cost_map.get(neighbor, float('inf')) + 1)
        path.append(min_next_point)
        current_point = min_next_point

    path.reverse()
    return path

def get_neighbors(cube, point):
    deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    neighbors = [(point[0] + dx, point[1] + dy) for dx, dy in deltas]

    valid_neighbors = []
    for neighbor in neighbors:
        if is_valid(cube, neighbor):
            valid_neighbors.append(neighbor)

    return valid_neighbors

def is_valid(cube, point):
    rows, cols = len(cube), len(cube[0])
    return 0 <= point[0] < rows and 0 <= point[1] < cols and cube[point[0]][point[1]] != '1'

f_name = "file1.txt"
cube = create_cube(f_name)

start_node = (0, 2)
goal_node = (6, 0)

shortest_path = astar(cube, start_node, goal_node)
print("\nPath:", shortest_path)
