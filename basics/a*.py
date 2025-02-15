import heapq

heuristics = {
    'Arad': 366,
    'Bucharest': 0,
    'Cralova': 160,
    'Dobreta': 242,
    'Eforie': 161,
    'Fagaras': 176,
    'Giurgiu': 77,
    'Hirsova': 151,
    'Iasi': 226,
    'Lugoj': 244,
    'Mehadia': 241,
    'Neamt': 234,
    'Oradea': 380,
    'Pitesti': 100,
    'Rimnicu Vilcea': 193,
    'Sibiu': 253,
    'Timisoara': 329,
    'Urziceni': 80,
    'Vaslui': 199,
    'Zerind': 374
}

graph = {
    'Arad': [('Zerind', 75), ('Sibiu', 140), ('Timisoara', 118)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Cralova', 120)],
    'Cralova': [('Dobreta', 120), ('Rimnicu Vilcea', 146), ('Pitesti', 138)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Cralova', 146), ('Pitesti', 97)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Cralova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

def a_star_search(graph, heuristics, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristics[start], 0, start))  # (f = g + h, g, node)
    
    came_from = {}
    came_from[start] = None
    
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    while open_list:
        current_f, current_g, current = heapq.heappop(open_list)
        
        if current == goal:
            break
        
        if current_g > g_score[current]:
            continue
        
        for neighbor, cost in graph[current]:
            tentative_g = current_g + cost
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f = tentative_g + heuristics[neighbor]
                heapq.heappush(open_list, (f, tentative_g, neighbor))
    
    path = []
    if current == goal:
        while current:
            path.append(current)
            current = came_from[current]
        path.reverse()
    
    return path

start = 'Arad'
goal = 'Bucharest'  
path = a_star_search(graph, heuristics, start, goal)
print("Path found by A*:", path)