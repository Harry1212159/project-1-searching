import GBFS as G
import BFS as B

def read_input(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    
    first_line = lines[0].strip().split()
    n = int(first_line[0])
    m = int(first_line[1])
    t = int(first_line[2])
    f = int(first_line[3])

    matrix = []
    for i in range(1, n + 1):
        row = lines[i].strip().split()
        matrix.append(row)
    
    return n, m, t, f, matrix

def find_positions(matrix, n, m):
    positions = {'S': None, 'G': None, 'S1': None, 'G1': None, 'S2': None, 'G2': None}

    for i in range(n):
        for j in range(m):
            if matrix[i][j] in positions:
                positions[matrix[i][j]] = (i, j)
    
    return positions

def print_path(algorithm_name, start_label, path):
    if not path:
        print(f"No path found from {start_label} using {algorithm_name}")
    else:
        print(f"{start_label}")
        print(f"{algorithm_name} path: ", end="")
        for node in path:
            print(node, end=" -> ")
        print("Goal")

filename = 'input1_level1.txt'
n, m, t, f, matrix = read_input(filename)
print(n, m, t, f)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], " ", end="")
    print("")
print("")

positions = find_positions(matrix, n, m)

for start_label, goal_label in [('S', 'G'), ('S1', 'G1'), ('S2', 'G2')]:
    if positions[start_label] and positions[goal_label]:
        start = positions[start_label]
        goal = positions[goal_label]

        path_GBFS = G.GBFS(matrix, start, goal)
        print_path("GBFS", start_label, path_GBFS)

        path_BFS = B.BFS(matrix, start, goal)
        print_path("BFS", start_label, path_BFS)
    else:
        print(f"Missing positions for {start_label} to {goal_label}")
