import heapq

# manhattan distance
def heuristics(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def A_star(matrix, start, goal):
    n = len(matrix)
    m = len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    explored_node = []
    heapq.heappush(explored_node, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while explored_node:
        _, current = heapq.heappop(explored_node)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path
        
        for direction in directions:
            neighbor = (current[0] + direction[0], current[1] + direction[1])
            if 0 <= neighbor[0] < n and 0 <= neighbor[1] < m and matrix[neighbor[0]][neighbor[1]] != '-1':
                new_cost = cost_so_far[current] + 1
                if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                    cost_so_far[neighbor] = new_cost
                    priority = new_cost + heuristics(neighbor, goal)
                    heapq.heappush(explored_node, (priority, neighbor))
                    came_from[neighbor] = current

    return []