import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

def reconstruct(came_from, start, goal):
    path = [goal]
    while goal != start:
        path.append(came_from[goal])
        goal = came_from[goal]
    return list(reversed(path))

def ucs(graph, start, goal):
    frontier = [(0, start)]  # Priority queue
    came_from = {start: None}
    total_cost = {start: 0}

    while frontier:
        cost, current_node = heapq.heappop(frontier)

        if current_node == goal:
            return reconstruct(came_from, start, goal), total_cost[goal]

        for neighbor, weight in graph[current_node].items():
            new_cost = total_cost[current_node] + weight

            if neighbor not in total_cost or new_cost < total_cost[neighbor]:
                heapq.heappush(frontier, (new_cost, neighbor))
                came_from[neighbor] = current_node
                total_cost[neighbor] = new_cost

    return None

# Example usage:
graph = Graph()
graph.add_edge('A', 'B', 5)
graph.add_edge('A', 'C', 2)
graph.add_edge('B', 'D', 4)
graph.add_edge('B', 'E', 2)
graph.add_edge('C', 'B', 8)
graph.add_edge('C', 'D', 7)
graph.add_edge('D', 'E', 6)
graph.add_edge('E', 'F', 3)

start_node = 'A'
goal_node = 'F'

path, cost = ucs(graph.graph, start_node, goal_node)

if path is not None:
    print("Shortest path:", path)
    print("Total cost:", cost)
else:
    print("No path found.")
