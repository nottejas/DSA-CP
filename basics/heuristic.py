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
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Mehadia': ['Lugoj', 'Dobreta'],
    'Dobreta': ['Mehadia', 'Cralova'],
    'Cralova': ['Dobreta', 'Rimnicu Vilcea', 'Pitesti'],
    'Rimnicu Vilcea': ['Sibiu', 'Cralova', 'Pitesti'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Pitesti': ['Rimnicu Vilcea', 'Cralova', 'Bucharest'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

def greedy_best_first_search(graph, heuristics, start, goal):
    open_list = [(heuristics[start], start)]  
    came_from = {} 
    came_from[start] = None

    while open_list:
        _, current = heapq.heappop(open_list)  

        if current == goal:
            break  

        for neighbor in graph[current]:
            if neighbor not in came_from:
                heapq.heappush(open_list, (heuristics[neighbor], neighbor))
                came_from[neighbor] = current

    path = []
    if current == goal:
        while current:
            path.append(current)
            current = came_from[current]
        path.reverse()

    return path

start = 'Sibiu'
goal = 'Iasi'
path = greedy_best_first_search(graph, heuristics, start, goal)
print("Path found by GBFS:", path)