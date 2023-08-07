#Variables and constants
graph = [
    [1, 3],
    [2],
    [0, 4],
    [2, 4],
    [0, 5],
    [6],
    [3]
]

def degrees(graph, n):
    indegrees = [0] * n
    outdegrees = [0] * n
    for i in range(n):
        outdegrees[i] = len(graph[i])
        for el in graph[i]:
            indegrees[el] += 1
    return indegrees, outdegrees

def circuitexists(indegrees, outdegrees):
    for i,o in zip(indegrees, outdegrees):
        if not i==o: return False
    return True

def pathexists(indegrees, outdegrees):
    count1 = count2 = 0
    for i,o in zip(indegrees, outdegrees):
        if count1>1 or count2>1 or abs(i-o)>1: return False
        count1 += i-o == 1
        count2 += o-i == 1
    return True

def findstart(indegrees, outdegrees, n):
    start = 0
    for i in range(n):
        if outdegrees[i] - indegrees[i] == 1: return i
        if outdegrees[i]>0: start = i
    return start

def dfs(graph, i, path, outdegrees):
    while not outdegrees[i] == 0:
        outdegrees[i] -= 1
        dfs(graph, graph[i][outdegrees[i]] , path, outdegrees)
    path.insert(0, i)

def findpath(graph):
    path = []
    n = len(graph)
    indegrees, outdegrees = degrees(graph, n)
    if pathexists(indegrees, outdegrees):
        dfs(graph, findstart(indegrees, outdegrees, n), path, outdegrees)
    return path

print(findpath(graph))