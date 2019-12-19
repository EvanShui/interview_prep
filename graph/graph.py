from collections import defaultdict

class Graph(object):
    def __init__(self):
        """
        G = Graph which contains:
        V = set of vertices
        E = set of edges
        """
        self.graph = defaultdict(list)
        self.pre = {}
        self.post = {}
        self.time = 1

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def previsit(self, v):
        self.pre[v] = self.time
        self.time += 1

    def postvisit(self, v):
        self.post[v] = self.time
        self.time += 1

    def dfs_helper(self, vertex, visited):
        visited[vertex] = True 
        print('visiting vertex: ', vertex)
        self.previsit(vertex)
        for neighbor in self.graph[vertex]:
            if not visited[neighbor]:
                self.dfs_helper(neighbor, visited)
        self.postvisit(vertex)
    
    def dfs(self):
        v = self.graph.keys()
        visited = [False] * (len(v) + 1)
        for vertex in v:
            if not visited[vertex]:
                self.dfs_helper(vertex, visited)

    def bfs(self, vertex):
        dist = {}
        for x in self.graph:
            dist[x] = None
        dist[vertex] = 0
        Q = [vertex]
        while Q:
            x = Q.pop(0)
            print('popped out: ',x)
            for neighbor in self.graph[x]:
                if dist[neighbor] is None:
                    Q.append(neighbor)
                    dist[neighbor] = dist[x] + 1
        print(dist)

    def print_pre_post(self):
        for i in range(1, len(self.graph)+1):
            print("Node: {} Pre: {} Post: {}".format(i, self.pre[i], self.post[i]))

