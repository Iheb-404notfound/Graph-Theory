
#Variables
graph =[
    [1, 4],
    [2, 6],
    [4, 5],
    [4],
    [5, 3],
    [3, 6],
    [2]
]
#Global Variables and constants
UNVISITED = -1

class Tarjan:
    def findSccs(self, graph):
        self.n = len(graph)
        self.sccs =0
        self.id = 0
        self.ids = [UNVISITED] * self.n
        self.low_links = [0] * self.n
        self.stacked = [False] * self.n
        self.stack = []

        for i in range(self.n):
            if self.ids[i] == UNVISITED:
                self.dfs(i, graph)
        return self.low_links

    def dfs(self, i, graph):
        self.stack.append(i)
        self.stacked[i] = True
        self.ids[i] = self.low_links[i] = self.id
        self.id += 1
        for arg in graph[i]:
            if self.ids[i] == UNVISITED: self.dfs(arg)
            if self.stacked[arg]: self.low_links[i] = min(self.low_links[arg],
                                                           self.low_links[i])
        if self.ids[i] == self.low_links[i]:
            node = self.stack.pop()
            while not node == i:
                self.stacked[node] = False
                self.low_links[node] = self.ids[i]
                node = self.stack.pop()
            self.sccs += 1

print(Tarjan().findSccs(graph))
