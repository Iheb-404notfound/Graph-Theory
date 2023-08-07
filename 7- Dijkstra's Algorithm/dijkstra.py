from queue import PriorityQueue

# Variables
graph = [
    [(1, 2), (2, 4)],
    [(3, 3)],
    [(3, 7), (4, 1)],
    [(6, 2)],
    [(5, 3), (10, 1)],
    [(6, 5)],
    [(7, 1)],
    [(9, 3)],
    [(7, 2)],
    [(8, 4)],
    [(5, 1)]
]


def dijkstra(graph, start):
    n = len(graph)
    distances = [float('inf')] * n
    pq = PriorityQueue()
    visited = set()

    distances[start] = 0
    pq.put((start, 0))

    while not pq.empty():
        i, d = pq.get()
        visited.add(i)

        for el in graph[i]:
            if el[0] in visited:
                continue
            dist = d + el[1]
            if dist < distances[ el[0] ]:
                distances[ el[0] ] = dist
                pq.put( (el[0], dist) )
    return distances

print(dijkstra(graph, 0))