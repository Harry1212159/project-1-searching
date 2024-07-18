import heapq

class Graph:
    def __init__(self, nodes, matrix, heuristics, start, end):
        self.nodes = nodes
        self.matrix = matrix
        self.heuristics = heuristics
        self.start = start
        self.end = end

def GBFS(graph):
    pq = []
    parent = {}

    heapq.heappush(pq, (graph.heuristics[graph.start], graph.start))
    parent[graph.start] = None
    
    while pq:
        current_heuristic, current_node = heapq.heappop(pq)

        if(current_node == graph.end):
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            path.reverse()
            return path
        
        for i in range(graph.nodes):
            if graph.matrix[current_node][i] != 0 and i not in parent:
                heapq.heappush(pq, (graph.heuristics[i],i))
                parent[i] = current_node
    
    return [-1]


if __name__ == "__main__":
    nodes = 10
    matrix = [
        [0, 0, 0, 0, 0, 0, 5, 3, 3, 4],
        [0, 0, 3, 5, 0, 0, 0, 0, 3, 0],
        [0, 3, 0, 0, 3, 0, 0, 0, 0, 2],
        [0, 5, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 1, 5, 2, 0, 0],
        [0, 0, 0, 5, 1, 0, 5, 0, 4, 0],
        [5, 0, 0, 0, 5, 5, 0, 0, 0, 0],
        [3, 0, 0, 0, 2, 0, 0, 0, 0, 0],
        [3, 3, 0, 0, 0, 4, 0, 0, 0, 0],
        [4, 0, 2, 0, 0, 0, 0, 0, 0, 0]
    ]
    heuristics = [3, 15, 12, 0, 6, 9, 3, 6, 18, 24]
    start = 0
    end = 3

    graph = Graph(nodes, matrix, heuristics, start, end)
    path = GBFS(graph)
    
    print("Path:", " -> ".join(map(str, path)))