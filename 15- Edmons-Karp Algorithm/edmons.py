from queue import Queue
# Variables
INF = float('inf')
# Edge Class
class Edge:
    def __init__(self, back, front, capacity):
        self.back = back
        self.front = front
        self.capacity = capacity
        self.residual = None
        self.flow = 0
    def isResidual(self):
        return self.capacity == 0
    def remaining_capacity(self):
        return self.capacity - self.flow
    def augment(self, bottleNeck):
        self.flow += bottleNeck
        self.residual.flow -= bottleNeck

class FlowNetwork:
    def __init__(self, n, source, sink):
        self.n = n
        self.source = source
        self.sink = sink
        self.graph = [[] for _ in range(n)]
        self.visited = [0] * n
        self.visitedToken = 1
        self.max_flow = 0
    
    def add_edge(self, back, front, capacity):
        edge = Edge(back, front, capacity)
        residual = Edge(front, back, 0)
        edge.residual = residual
        residual.residual = edge
        self.graph[back].append(edge)
        self.graph[front].append(residual)
    # Edmonds-Karp Algorithm
    def bfs(self):
        queue = Queue()
        self.visited[self.source] = self.visitedToken
        queue.put(self.source)
        prev = [None] * self.n
        while not queue.empty():
            node = queue.get()
            if node == self.sink: break
            for edge in self.graph[node]:
                if edge.remaining_capacity()>0 and self.visited[edge.front] != self.visitedToken:
                    self.visited[edge.front] = self.visitedToken
                    prev[edge.front] = edge
                    queue.put(edge.front)
        if prev[self.sink] == None: return 0
        bottleneck = INF
        edge = prev[self.sink]
        while edge!=None:
            bottleneck = min(bottleneck, edge.remaining_capacity())
            edge = prev[edge.back]
        edge = prev[self.sink]
        while edge!=None:
            edge.augment(bottleneck)
            edge = prev[edge.back]
        return bottleneck

    def find_max_flow(self):
        f = self.bfs()
        while f!=0:
            # Mark all nodes as visited
            self.visitedToken += 1
            self.max_flow += f
            f = self.bfs()
        return self.max_flow

#Application
edmonds = FlowNetwork(11, 0, 10)
edmonds.add_edge(0, 2, 10)
edmonds.add_edge(0, 3, 20)
edmonds.add_edge(0, 1, 10)
edmonds.add_edge(1, 4, 15)
edmonds.add_edge(2, 6, 20)
edmonds.add_edge(2, 3, 5)
edmonds.add_edge(3, 5, 10)
edmonds.add_edge(3, 4, 10)
edmonds.add_edge(3, 1, 10)
edmonds.add_edge(4, 7, 30)
edmonds.add_edge(5, 6, 15)
edmonds.add_edge(5, 8, 20)
edmonds.add_edge(6, 9, 10)
edmonds.add_edge(6, 8, 20)
edmonds.add_edge(7, 5, 25)
edmonds.add_edge(7, 8, 5)
edmonds.add_edge(7, 10, 30)
edmonds.add_edge(8, 10, 15)
edmonds.add_edge(9, 10, 20)

print(edmonds.find_max_flow())