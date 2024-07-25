import GBFS as G
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
    start = None
    goal = None

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'S':
                start = (i, j)
            elif matrix[i][j] == 'G':
                goal = (i, j)
    
    return start, goal

def print_path(path):
    if not path:
        print("No path found")
    else:
        print("Path: ", end = "")

        for node in path:
            print(node, end=" -> ")
        print("Goal")


