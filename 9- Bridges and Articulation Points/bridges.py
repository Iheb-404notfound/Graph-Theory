#Variables
graph =[
    [1, 2],
    [0, 2],
    [0, 1, 3],
    [2, 4, 6],
    [3, 5],
    [4, 6],
    [3, 5, 7],
    [6, 8],
    [7]
]
#Global variables needed for the Bridges Search Algorithm
id = 0

# DFS Algorithm
def dfs(graph, i, p, visited, low_links, ids, bridges):
    global id
    id+=1
    visited[i] = True
    low_links[i] = ids[i] = id
    for arg in graph[i]:
        if arg == p: continue
        if not visited[arg]:
            dfs(graph, arg, i, visited, low_links, ids, bridges)
            low_links[i] = min(low_links[i], low_links[arg])
            if ids[i] < low_links[arg]:
                bridges.append((i, arg))
        else:
            low_links[i] = min(low_links[i], low_links[arg])


# Bridges Search Algorithm
def bridges_search(graph):
    n = len(graph)
    visited = [False] * n
    low_links = [0] * n
    ids = [0] * n
    bridges = []
    for i in range(n):
        if not visited[i]: dfs(graph, i, -1, visited, low_links, ids, bridges)
    return bridges

print(bridges_search(graph))