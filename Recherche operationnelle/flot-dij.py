import heapq

class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    # Dijkstra pour trouver le chemin augmentant
    def dijkstra(self, source, sink, parent):
        min_heap = [(0, source)]
        heapq.heapify(min_heap)
        visited = set()

        while min_heap:
            (weight, node) = heapq.heappop(min_heap)

            if node == sink:
                return True

            visited.add(node)

            for neighbor, capacity in enumerate(self.graph[node]):
                if capacity > 0 and neighbor not in visited:
                    parent[neighbor] = node
                    heapq.heappush(min_heap, (weight + 1, neighbor))

        return False

    # Algorithme de Ford-Fulkerson avec Dijkstra
    def FordFulkerson(self, source, sink):
        parent = [-1] * self.ROW
        max_flow = 0

        while self.dijkstra(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            parent = [-1] * self.ROW  # Réinitialiser parent pour le prochain Dijkstra

        return max_flow


# Exemple d'utilisation
graph = [[0, 6, 8, 0, 0, 0], [0, 0, 0, 6, 3, 0], [0, 0, 0, 3, 3, 0], [0, 0, 0, 0, 0, 8], [0, 0, 0, 0, 0, 6], [0, 0, 0, 0, 0, 0]]

g = Graph(graph)

source = 0
sink = 5

print("Le flot maximal possible est : %d " % g.FordFulkerson(source, sink))