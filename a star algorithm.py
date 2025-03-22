import heapq

def a_star(graph, start, goal, h):
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = h[start]
    
    while open_set:
        _, current = heapq.heappop(open_set)
        
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1], g_score[goal]
        
        for neighbor, cost in graph[current].items():
            tentative_g_score = g_score[current] + cost
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h[neighbor]
                heapq.heappush(open_set, (f_score[neighbor], neighbor))
    
    return None, float('inf')

graph = {
    'A': {'B': 10, 'C': 15},
    'B': {'A': 10, 'D': 12},
    'C': {'A': 15, 'D': 10},
    'D': {'B': 12, 'C': 10}
}

heuristic = {'A': 7, 'B': 6, 'C': 2, 'D': 0}  # Estimated costs to goal 'D'

start_node = 'A'
goal_node = 'D'
path, cost = a_star(graph, start_node, goal_node, heuristic)
print(f"Optimal path: {path} with cost {cost}")
