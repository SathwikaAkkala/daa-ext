import heapq

def dijkstra(graph, start):
    # Initialize the priority queue
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    # Initialize distances dictionary
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # If the current distance is greater than the recorded shortest distance, skip
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # If found a shorter path to the neighbor, update the distance and add to the priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
def main():
    # Read input graph from the user
    graph = {}
    num_nodes = int(input("Enter the number of nodes in the graph: "))
    
    for _ in range(num_nodes):
        node = input("Enter node name: ")
        graph[node] = {}
        num_edges = int(input(f"Enter the number of edges for node {node}: "))
        for _ in range(num_edges):
            neighbor, weight = input(f"Enter neighbor and weight for edge (separated by space) from {node}: ").split()
            weight = int(weight)
            graph[node][neighbor] = weight

    # Read the start node
    start_node = input("Enter the start node: ")

    # Compute shortest paths
    distances = dijkstra(graph, start_node)
    print(f"Shortest distances from {start_node}: {distances}")

if __name__ == "__main__":
    main()



