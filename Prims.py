import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    def min_key(self, key, mst_set):
        min_value = sys.maxsize
        min_index = None

        for v in range(self.V):
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]
                min_index = v

        return min_index

    def prim_mst(self):
        parent = [None] * self.V
        key = [sys.maxsize] * self.V
        mst_set = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    parent[v] = u
                    key[v] = self.graph[u][v]

        return parent

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight


# Example usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
g.add_edge(2, 4, 7)
g.add_edge(3, 4, 9)

mst = g.prim_mst()

print("Edge \tWeight")
for i in range(1, g.V):
    print(f"{mst[i]} - {i}\t{g.graph[i][mst[i]]}")
