import GBFS as G
import BFS as B
from readFile import read_input, find_positions, print_path

def main():
    filename = 'input1_level1.txt'
    n, m, t, f, matrix = read_input(filename)
    print(n, m, t, f)

    for i in range(n):
        for j in range(m):
            print(matrix[i][j], " ", end="")
        print("")
    print("")

    positions = find_positions(matrix, n, m)

    # for start_label, goal_label in [('S', 'G'), ('S1', 'G1'), ('S2', 'G2')]:
    for start_label, goal_label in [('S', 'G')]:
        if positions[start_label] and positions[goal_label]:
            start = positions[start_label]
            goal = positions[goal_label]

            path_GBFS = G.GBFS(matrix, start, goal)
            print_path("GBFS", start_label, path_GBFS)

            path_BFS = B.BFS(matrix, start, goal)
            print_path("BFS", start_label, path_BFS)
        else:
            print(f"Missing positions for {start_label} to {goal_label}")

if __name__ == "__main__":
    main()
