class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

    def bellman_ford(self, source):
        # Initialize distances from source to all vertices as infinite and distance to source itself as 0
        dist = {vertex: float('inf') for vertex in range(self.vertices)}
        dist[source] = 0

        # Relax all edges |V| - 1 times
        for _ in range(self.vertices - 1):
            for u, v, weight in self.edges:
                if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        # Check for negative-weight cycles
        for u, v, weight in self.edges:
            if dist[u] != float('inf') and dist[u] + weight < dist[v]:
                print("Graph contains negative weight cycle")
                return None
      return dist

def main():
    # Get number of vertices and edges
    vertices = int(input("Enter the number of vertices: "))
    edges_count = int(input("Enter the number of edges: "))

    # Create graph
    graph = Graph(vertices)

    # Get edges from user
    print("Enter the edges in the format 'u v weight':")
    for _ in range(edges_count):
        u, v, weight = map(int, input().split())
        graph.add_edge(u, v, weight)

    # Get the source vertex
    source_vertex = int(input("Enter the source vertex: "))

    # Run Bellman-Ford algorithm
    distances = graph.bellman_ford(source_vertex)

    # Print results
    if distances is not None:
        print("Vertex distances from source vertex", source_vertex)
        for vertex in range(vertices):
            print(f"Distance to vertex {vertex}: {distances[vertex]}")

if __name__ == "__main__":
    main()


### Explanation:


