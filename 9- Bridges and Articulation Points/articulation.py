#Variables
graph =[
    [1, 2],
    [0, 2],
    [0, 1, 3],
    [2, 4, 6],
    [3, 5],
    [4, 6],
    [3, 5, 7, 8],
    [6, 8],
    [6, 7]
]
#Global variables needed for the Articulation Points Search Algorithm
id = 0
out = 0

# DFS Algorithm
def dfs(graph, r, i, p, visited, low_links, ids, art):
    global id, out
    visited[i] = True
    low_links[i] = ids[i] = id
    id += 1
    for arg in graph[i]:
        if arg == p: continue
        if not visited[arg]:
            dfs(graph, r, arg, i, visited, low_links, ids, art)
            low_links[i] = min(low_links[i], low_links[arg])
            if ids[i] <= low_links[arg]:
                art[i] = True
        else:
            low_links[i] = min(low_links[i], low_links[arg])

# Articulation Points Search Algorithm
def art_search(graph):
    global out
    n = len(graph)
    visited = [False] * n
    low_links = [0] * n
    ids = [0] * n
    art = [False] * n
    for i in range(n):
        if not visited[i]:
            out = 0
            dfs(graph, i, i, -1, visited, low_links, ids, art)
            art[i] = out > 1
    return art

print(art_search(graph))