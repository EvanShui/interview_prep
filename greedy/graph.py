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

