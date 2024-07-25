def dfs(city_map, start, goal):
    movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    stack = [start]
    visited = set()
    parent = {}
    
    while stack:
        current = stack.pop()
        if current == goal:
            break
        
        for move in movements:
            next_cell = (current[0] + move[0], current[1] + move[1])
            
            if (0 <= next_cell[0] < len(city_map) and 
                0 <= next_cell[1] < len(city_map[0]) and 
                city_map[next_cell[0]][next_cell[1]] != -1 and
                next_cell not in visited):
                
                stack.append(next_cell)
                visited.add(next_cell)
                parent[next_cell] = current

    path = []
    if goal in parent:
        path.append(goal)
        while path[-1] != start:
            path.append(parent[path[-1]])
        path.reverse()
    
    return path