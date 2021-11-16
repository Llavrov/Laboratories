
class Graph(object):
    def __init__(self, V, adj = []):
        self.V = V
        self.adj = []

    def addEdge(self, v, w):
        self.v = v
        self.w = w

    def bridgeUtil(self, u, visited = [], disc = [], low = [],
                    parent = []):
        time = 0
        self.u = u
        self.visited = []
        visited[u] = True
        self.disc = []
        self.low = []
        disc[u] = low[u] = time + 1;
        self.parent = []

