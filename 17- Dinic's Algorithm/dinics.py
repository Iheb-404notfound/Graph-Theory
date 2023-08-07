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
        self.level = [0] * n
    
    def add_edge(self, back, front, capacity):
        edge = Edge(back, front, capacity)
        residual = Edge(front, back, 0)
        edge.residual = residual
        residual.residual = edge
        self.graph[back].append(edge)
        self.graph[front].append(residual)
    # Dinic' Algorithm
    def bfs(self):
        self.level = [-1] * self.n
        queue = Queue()
        queue.put(self.source)
        self.level[self.source] = 0
        while not queue.empty():
            node = queue.get()
            for edge in self.graph[node]:
                if edge.remaining_capacity()>0 and self.level[edge.front] == -1:
                    self.level[edge.front] = self.level[node] + 1
                    queue.put(edge.front)
        return self.level[self.sink]!=-1

    def dfs(self, i, next, flow):
        if i == self.sink: return flow
        while next[i] < len(self.graph[i]):
            edge = self.graph[i][next[i]]
            if edge.remaining_capacity()>0 and self.level[edge.front] == self.level[i]+1:
                bottleneck = self.dfs(edge.front, next, min(flow, edge.remaining_capacity()))
                if bottleneck > 0:
                    edge.augment(bottleneck)
                    return bottleneck
            next[i] += 1
        return 0

    def find_max_flow(self):
        while self.bfs():
            next = [0] * self.n
            f = self.dfs(self.source, next, INF)
            while f!=0:
                self.max_flow += f
                f = self.dfs(self.source, next, INF)
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