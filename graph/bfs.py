from graph import Graph

def test_3():
    G = Graph()
    G.add_edge(1,2)
    G.add_edge(1,3)
    G.add_edge(1,9)
    G.add_edge(2,1)
    G.add_edge(2,3)
    G.add_edge(3,1)
    G.add_edge(3,2)
    G.add_edge(3,4)
    G.add_edge(3,6)
    G.add_edge(3,7)
    G.add_edge(3,8)
    G.add_edge(4,3)
    G.add_edge(4,5)
    G.add_edge(4,6)
    G.add_edge(4,9)
    G.add_edge(5,4)
    G.add_edge(5,6)
    G.add_edge(6,3)
    G.add_edge(6,4)
    G.add_edge(6,5)
    G.add_edge(6,9)
    G.add_edge(7,3)
    G.add_edge(7,8)
    G.add_edge(8,3)
    G.add_edge(8,7)
    G.add_edge(8,9)
    G.add_edge(9,1)
    G.add_edge(9,4)
    G.add_edge(9,6)
    G.add_edge(9,8)
    return G

def main():
    G = test_3()
    G.bfs(1)

if __name__ == '__main__':
    main()
