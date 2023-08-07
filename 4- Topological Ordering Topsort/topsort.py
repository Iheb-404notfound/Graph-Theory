# Variables
graph = [
    [3],
    [3],
    [0, 1],
    [6, 7],
    [0, 3, 5, 7],
    [9, 10],
    [],
    [6, 10],
    [],
    [10],
    []
]

# The Depth-First Search Algorithm
def dfs(arg, visited, graph):
    if arg in visited:
        return []
    else:
        visited.add(arg)
        l = []
        for i in graph[arg]:
            l = dfs(i, visited, graph) + l
        return [arg] + l

# The Actual Topological Ordering Algorithm
def topsort(graph):
    n = len(graph)
    visited = set()
    l = []
    for i in range(n):
        if not i in visited:
            l = dfs(i, visited, graph) + l
    return l

print(topsort(graph))