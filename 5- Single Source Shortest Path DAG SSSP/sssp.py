# Variables
graph = [
    [(1, 2), (2, -1)],
    [(3, 3), (4, 1)],
    [(3, 4), (5, 2)],
    [(6, 2)],
    [(6, 1)],
    [(7, 3)],
    [(7, 1), (8, 2)],
    [(9, -2)],
    [(9, 1)],
    [(10, 3)],
    []
]

# The Depth-First Search Algorithm
def dfs(arg, visited, graph):
    if arg in visited:
        return []
    else:
        visited.add(arg)
        l = []
        for el in graph[arg]:
            l = dfs(el[0], visited, graph) + l
        return [arg] + l

# The Topological Ordering Algorithm
def topsort(graph):
    n = len(graph)
    visited = set()
    l = []
    for i in range(n):
        if not i in visited:
            l = dfs(i, visited, graph) + l
    return l

# SSSP DAG Algorithm
def SSSP(graph):
    n = len(graph)
    order = topsort(graph)
    distances = [float('inf')] * n
    distances[ order[0] ] = 0
    
    for arg in order:
        for el in graph[arg]:
            distances[el[0]] = min(distances[arg] + el[1], distances[el[0]])
    
    return order, distances

order, distances = SSSP(graph)
print(order, distances, sep="\n")