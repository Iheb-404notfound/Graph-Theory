# Variables
graph = [   
    [(1, 2), (2, 4)],
    [(3, 3)],
    [(3, 7), (4, -3)],
    [(6, 2)],
    [(5, -2)],
    [(6, 5), (10, 1)],
    [(7, 1)],
    [(9, 3)],
    [(7, -10)],
    [(8, 4)],
    [(4, 1)]
]

#Bellman-Ford Algorithm
def bf(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    distances[start] = 0

    for i in range(n - 1):
        for arg in range(n):
            for to, weight in graph[arg]:
                distances[ to ] = min(distances[ to ] , distances[arg] + weight)
    
    for i in range(n - 1):
        for arg in range(n):
            for to, weight in graph[arg]:
                if distances[ to ] > distances[arg] + weight:
                    distances[ to ] = -float('inf')
        
    return distances
                
print( bf(graph, 0) )