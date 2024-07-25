import heapq
import readFile as r

# manhattan distance
def heuristics(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def A_star_level2(matrix, start, goal, time):
    n = len(matrix)
    m = len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    explored_node = []
    heapq.heappush(explored_node, (0, start, 0))
    came_from = {}
    came_from[start] = None
    
    while explored_node:
        _, current, current_time = heapq.heappop(explored_node)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path, current_time
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and matrix[neighbor[0]][neighbor[1]] != '-1':
                additional_time = 1
                if matrix[neighbor[0]][neighbor[1]].isdigit():
                    additional_time += int(matrix[neighbor[0]][neighbor[1]])
                new_time = additional_time + current_time
                if neighbor not in came_from and new_time <= time:
                    priority = heuristics(neighbor, goal)
                    heapq.heappush(explored_node, (priority, neighbor, new_time))
                    came_from[neighbor] = current

    return [], -1

def compare_paths(matrix, start, goal, committed_time):
    shortest_path = None
    shortest_length = float('inf')
    shortest_time = float('inf')

    new_path, new_time = GBFS_level2(matrix, start, goal, committed_time)
    if new_path and len(new_path) < shortest_length:
        shortest_path = new_path
        shortest_length = len(new_path)
        shortest_time = new_time
    print(shortest_time, shortest_length)
    return shortest_path, shortest_length, shortest_time

def print_path_level2(path, time_spent):
    if not path:
        print("No path found")
    else:
        print("Path:")
        for node in path:
            print(node, end=" -> ")
        print("Goal")
        print(f"Time spent: {time_spent} minutes")

# def level2(filename):
    # filename = 'input1_level1.txt'
    # n, m, t, f, matrix = r.read_input(filename)
    # print (n,m,t,f)

    # for i in range (0, n):
    #     for j in range (0, m):
    #         print (matrix[i][j], " ", end = "")
    #     print("")
    # start, goal = r.find_positions(matrix, n, m)

    # # path_BFS = r.G.BFS(matrix, start, goal)
    # # path_DFS = r.G.DFS(matrix, start, goal)
    # # path_UCS = r.G.UCS(matrix, start, goal)
    # path_GBFS, time_spent = GBFS_level2(matrix, start, goal, t)
    # # path_A_star_search = r.G.A_star_search(matrix, start, goal)
    # # r.print_path(path_BFS)
    # # r.print_path(path_DFS)
    # # r.print_path(path_UCS)
    # print_path_level2(path_GBFS, time_spent)
    # # r.print_path(path_A_star_search)

filename = 'input1_level1.txt'
n, m, t, f, matrix = r.read_input(filename)
start, goal = r.find_positions(matrix, n, m)

shortest_path, shortest_length, shortest_time = compare_paths(matrix, start, goal, t)
print_path_level2(shortest_path, shortest_length)