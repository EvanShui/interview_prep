import heapq

class Vertex:
    def __init__(self, letter):
        self.letter = letter
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight):
        self.neighbors[neighbor] = weight

    def __str__(self):
        return "node id: {} neighbors: {}".format(self.letter, self.neighbors)

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def add_edge(self, node_from, node_to, weight):
        if node_from not in self.vert_dict:
            self.add_vertex(node_from)
        if node_to not in self.vert_dict:
            self.add_vertex(node_to)
        self.vert_dict[node_from].add_neighbor(self.vert_dict[node_to], weight)
        self.vert_dict[node_to].add_neighbor(self.vert_dict[node_from], weight)

    def __str__(self):
        return "number of vertices: {} vertices: {}".format(self.num_vertices,
                self.vert_dict.keys())

def prim(graph, start_v):

    q = []

    if start_v not in graph.vert_dict:
        return -1
    start_v = graph.vert_dict[start_v] 
    all_v = graph.vert_dict.values()
    seen_vertices = set(start_v.letter)

    for neighbor, weight in start_v.neighbors.items():
        heapq.heappush(q, (weight, id(neighbor), start_v.letter, neighbor))

    while len(seen_vertices) != graph.num_vertices:
        v = heapq.heappop(q)
        while v[3].letter in seen_vertices:
            v = heapq.heappop(q)
        print("add edge from: {} to: {} weight: {}".format(v[2], v[3].letter, v[0]))
        seen_vertices.add(v[3].letter)
        for neighbor, weight in v[3].neighbors.items():
            heapq.heappush(q, (weight, id(neighbor), v[3].letter, neighbor))
    return seen_vertices

def main():
    g = Graph()
    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')
    g.add_vertex('g')

    g.add_edge('a', 'b', 7)
    g.add_edge('a', 'd', 5)

    g.add_edge('b', 'a', 7)
    g.add_edge('b', 'c', 8)
    g.add_edge('b', 'd', 9)
    g.add_edge('b', 'e', 7)

    g.add_edge('c', 'b', 8)
    g.add_edge('c', 'e', 5)

    g.add_edge('d', 'a', 5)
    g.add_edge('d', 'b', 9)
    g.add_edge('d', 'e', 15)
    g.add_edge('d', 'f', 8)

    g.add_edge('e', 'b', 7)
    g.add_edge('e', 'c', 8)
    g.add_edge('e', 'd', 15)
    g.add_edge('e', 'f', 8)
    g.add_edge('e', 'g', 9)
    
    g.add_edge('f', 'd', 6)
    g.add_edge('f', 'e', 8)
    g.add_edge('f', 'g', 11)

    g.add_edge('g', 'e', 9)
    g.add_edge('g', 'f', 11)

    print(prim(g, 'd'))
if __name__ == '__main__':
    main()
