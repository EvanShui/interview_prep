import graph
import heapq

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
    g = graph.Graph()
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
