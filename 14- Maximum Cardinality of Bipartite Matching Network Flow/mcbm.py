# Variables
INF = float('inf')
# Edge Class
class Edge:
    def __init__(self, back, front, capactiy):
        self.back = back
        self.front = front
        self.capacity = capactiy
        self.residual = None
        self.flow = 0
    def isResidual(self):
        return self.capacity == 0
    def remaining_capactiy(self):
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
    # Ford Fulkerson Algorithm
    def dfs(self, node, flow):
        if node == self.sink: return flow

        self.visited[node] = self.visitedToken
        edges = self.graph[node]
        for edge in edges:
            if edge.remaining_capactiy()>0 and self.visited[edge.front] != self.visitedToken:
                bottlneck = self.dfs(edge.front, min(flow, edge.remaining_capactiy()))
                if bottlneck >0:
                    edge.augment(bottlneck)
                    return bottlneck
        return 0

    def find_max_flow(self):
        f = self.dfs(self.source, INF)
        while f!=0:
            self.visitedToken += 1
            self.max_flow += f
            f = self.dfs(self.source, INF)
        return self.max_flow

#Application
ford = FlowNetwork(10, 0, 9)
# add edges from the source node 0 to the input nodes
ford.add_edge(0, 1, 1)
ford.add_edge(0, 2, 1)
ford.add_edge(0, 3, 1)
ford.add_edge(0, 4, 1)
# add edges of the graph
ford.add_edge(1, 5, 1)
ford.add_edge(1, 6, 1)
ford.add_edge(1, 8, 1)
ford.add_edge(2, 5, 1)
ford.add_edge(2, 8, 1)
ford.add_edge(3, 6, 1)
ford.add_edge(3, 7, 1)
ford.add_edge(4, 6, 1)
ford.add_edge(4, 7, 1)
ford.add_edge(4, 8, 1)
# add edges from output nodes to the sink node
ford.add_edge(5, 9, 1)
ford.add_edge(6, 9, 1)
ford.add_edge(7, 9, 1)
ford.add_edge(8, 9, 1)

mcbm = ford.find_max_flow()
print(mcbm)