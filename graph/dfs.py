from graph import Graph


def test_1():
    G = Graph()
    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(1, 2)
    G.add_edge(2, 0)
    G.add_edge(2, 3)
    G.add_edge(3, 3)
    return G

def test_2():
    G = Graph()
    G.add_edge(1, 2)
    G.add_edge(2, 1)
    G.add_edge(2, 4)
    G.add_edge(4, 2)
    G.add_edge(1, 3)
    G.add_edge(3, 1)
    G.add_edge(3, 4)
    G.add_edge(4, 3)
    G.add_edge(3, 5)
    G.add_edge(5, 3)
    G.add_edge(5, 6)
    G.add_edge(6, 5)
    return G

def main():
    G = test_2()
    # visited = [False] * len(G.graph)
    # G.dfs_helper(2, visited)
    G.dfs()
    G.print_pre_post()

if __name__ == '__main__':
    main()
