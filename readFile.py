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
            if matrix[i][j] == 'S1':
                start = (i, j)
            elif matrix[i][j] == 'G1':
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

filename = 'input1_level1.txt'
n, m, t, f, matrix = read_input(filename)
print (n,m,t,f)

for i in range (0, n):
    for j in range (0, m):
        print (matrix[i][j], " ", end = "")
    print("")
start, goal = find_positions(matrix, n, m)

path_GBFS = G.GBFS(matrix, start, goal)
print_path(path_GBFS)

