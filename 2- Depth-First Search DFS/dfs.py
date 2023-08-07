graph = [ [4], [0, 2], [], [4], [1, 6], [], [2, 3] ]

n = len(graph)
visited = [False]*n

def dfs(i):
    print(i, end=' | ')
    if visited[i]:
        return
    visited[i] = True

    for n in graph[i]:
        dfs(n)

dfs(0)