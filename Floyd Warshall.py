def floyd_warshall(graph):
    # Number of vertices in the graph
    V = len(graph)
    
    # Initialize distance matrix with the given graph
    dist = [[float('inf')] * V for _ in range(V)]
    for i in range(V):
        for j in range(V):
            dist[i][j] = graph[i][j]
    
    # Floyd-Warshall algorithm
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
    return dist

def main():
    # Dynamic input of graph
    V = int(input("Enter the number of vertices: "))
    graph = []
    print("Enter the adjacency matrix of the graph (use 'inf' for infinity):")
    for i in range(V):
        row = list(map(str, input().split()))
        for j in range(V):
            if row[j].lower() == 'inf':
                row[j] = float('inf')
            else:
                row[j] = int(row[j])
        graph.append(row)
    
    # Run Floyd-Warshall algorithm
    shortest_distances = floyd_warshall(graph)
    
    # Print shortest distances
    print("\nShortest distances between every pair of vertices:")
    for i in range(V):
        for j in range(V):
            if shortest_distances[i][j] == float('inf'):
                print("INF", end=" ")
            else:
                print(shortest_distances[i][j], end=" ")
        print()

if __name__ == "__main__":
    main()
