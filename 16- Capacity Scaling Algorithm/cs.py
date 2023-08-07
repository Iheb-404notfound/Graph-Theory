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
        self.delta = 0
    
    def add_edge(self, back, front, capacity):
        edge = Edge(back, front, capacity)
        residual = Edge(front, back, 0)
        edge.residual = residual
        residual.residual = edge
        self.graph[back].append(edge)
        self.graph[front].append(residual)
        self.delta = max(self.delta, capacity)
    # Capacity Scaling Algorithm
    def dfs(self, node, flow):
        if node==self.sink: return flow
        self.visited[node] = self.visitedToken
        for edge in self.graph[node]:
            if (edge.remaining_capacity()>=self.delta and 
                self.visited[edge.front] != self.visitedToken):
                bottleneck = self.dfs(edge.front, min(flow, edge.remaining_capacity()))
                if bottleneck > 0:
                    edge.augment(bottleneck)
                    return bottleneck
        return 0

    def find_max_flow(self):
        self.delta = 1<<(self.delta.bit_length()-1)
        while self.delta > 0:
            f = 1
            while f!=0:
                # Mark all nodes as visited
                self.visitedToken += 1
                f = self.dfs(self.source, INF)
                self.max_flow += f
            self.delta//=2
        return self.max_flow

#Application
cs = FlowNetwork(11, 0, 10)
cs.add_edge(0, 2, 10)
cs.add_edge(0, 3, 20)
cs.add_edge(0, 1, 10)
cs.add_edge(1, 4, 15)
cs.add_edge(2, 6, 20)
cs.add_edge(2, 3, 5)
cs.add_edge(3, 5, 10)
cs.add_edge(3, 4, 10)
cs.add_edge(3, 1, 10)
cs.add_edge(4, 7, 30)
cs.add_edge(5, 6, 15)
cs.add_edge(5, 8, 20)
cs.add_edge(6, 9, 10)
cs.add_edge(6, 8, 20)
cs.add_edge(7, 5, 25)
cs.add_edge(7, 8, 5)
cs.add_edge(7, 10, 30)
cs.add_edge(8, 10, 15)
cs.add_edge(9, 10, 20)

print(cs.find_max_flow())
