# Variables
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D', 'F'],
    'D': ['F'],
    'F': ['C']
}

def bfs(graph, start):
    visited = set()
    queue = [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            print(node, end=' | ')
            visited.add(node)
            if node in graph.keys():
                queue.extend(graph[node])

# Starting the BFS from node 'A'
bfs(graph, 'A')