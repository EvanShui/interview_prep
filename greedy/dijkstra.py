import graph
import heapq

def dijkstra(graph, start_v):
    q = []
    dist = {}
    dist[start_v] = 0
    start_node = graph.vert_dict[start_v]
    seen_vertices = set()
    heapq.heappush(q, (dist[start_v], id(start_node), start_node))
    for let, node in graph.vert_dict.items():
        if let != start_v:
            dist[let] = float('inf')
            heapq.heappush(q, (dist[let], id(node), node))

    while len(q) != 0:
        u = heapq.heappop(q)[2]
        seen_vertices.add(u.letter)
        for v, weight in u.neighbors.items():
            if dist[v.letter] > dist[u.letter] + weight:
                dist[v.letter] = dist[u.letter] + weight
    return dist

    
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

    print(dijkstra(g, 'd'))
if __name__ == '__main__':
    main()
