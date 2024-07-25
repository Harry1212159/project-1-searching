import readFile as r
def level1(filename):
    filename = 'input1_level1.txt'
    n, m, t, f, matrix = r.read_input(filename)
    # print (n,m,t,f)

    # for i in range (0, n):
    #     for j in range (0, m):
    #         print (matrix[i][j], " ", end = "")
    #     print("")
    start, goal = r.find_positions(matrix, n, m)

    # path_BFS = r.G.BFS(matrix, start, goal)
    # path_DFS = r.G.DFS(matrix, start, goal)
    # path_UCS = r.G.UCS(matrix, start, goal)
    path_GBFS = r.G.GBFS(matrix, start, goal)
    # path_A_star_search = r.G.A_star_search(matrix, start, goal)
    # r.print_path(path_BFS)
    # r.print_path(path_DFS)
    # r.print_path(path_UCS)
    r.print_path(path_GBFS)
    # r.print_path(path_A_star_search)

