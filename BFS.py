from collections import deque

def BFS(matrix, start, goal):
    n = len(matrix)
    m = len(matrix[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = deque([start])
    came_from = {}
    came_from[start] = None
    
    while queue:
        current = queue.popleft()
        
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
                if neighbor not in came_from:
                    queue.append(neighbor)
                    came_from[neighbor] = current

    return []
