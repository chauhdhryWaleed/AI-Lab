def read_file(filename):
    f = open(filename, "r")
    data = f.read()
    d = []
    p = []
    for char in data:
        if char == " ":
            continue
        if char == "\n":
            d.append(p)
            p = []
        else:
            p.append(char)
    if p:
        d.append(p)
    return d


def get_neighbors(matrix, x, y):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    neighbors = []

    if x > 0:
        neighbors.append((x - 1, y))

    if x < rows - 1:
        neighbors.append((x + 1, y))

    if y > 0:
        neighbors.append((x, y - 1))

    if y < cols - 1:
        neighbors.append((x, y + 1))

    return neighbors


def BFS(cube, x, y, visited, path):
    queue = []
    queue.append([(x, y)])
    while len(queue) > 0:
        current_path = queue[0]
        queue.pop(0)
        visited[current_path[-1][0]][current_path[-1][1]] = 1
        if cube[current_path[-1][0]][current_path[-1][1]] == "1":
            continue
        if cube[current_path[-1][0]][current_path[-1][1]] == "G":
            return current_path
        neighbors = get_neighbors(cube, current_path[-1][0], current_path[-1][1])
        for n in neighbors:
            if visited[n[0]][n[1]] == 0:
                temp = [i for i in current_path]
                temp.append((n[0], n[1]))
                queue.append(temp)
    return None


def DFS(cube, x, y, visited, path):
    visited[x][y] = 1
    if cube[x][y] == "1":
        return 0
    elif cube[x][y] == "G":
        path.append((x, y))
        return 1
    neighbors = get_neighbors(cube, x, y)
    for n in neighbors:
        if visited[n[0]][n[1]] == 0:
            if DFS(cube, n[0], n[1], visited, path) == 1:
                path.append((x, y))
                return 1
    return 0


data = read_file("file.txt")
visited_bfs = [[0 for j in i] for i in data]
visited_dfs = [[0 for j in i] for i in data]
path_bfs = []
path_dfs = []


print("BFS Path:")
path_bfs=BFS(data, 0, 0, visited_bfs, path_bfs)
for i in range(0,len(path_bfs)):
    print(path_bfs[i])

DFS(data, 0, 0, visited_dfs, path_dfs)
print("DFS Path:")
for i in range(len(path_dfs) - 1, -1, -1):
    print(path_dfs[i])
