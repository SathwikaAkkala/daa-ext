import numpy as np

# Example distance matrix for 5 cities
distance_matrix = np.array([
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 7],
    [10, 4, 8, 0, 5],
    [7, 3, 7, 5, 0]
])

def held_karp_tsp(distance_matrix):
    n = distance_matrix.shape[0]
    # Dictionary to store the cost of reaching each set of nodes
    C = {}

    # Initialize the base cases
    for k in range(1, n):
        C[(1 << k, k)] = (distance_matrix[0][k], 0)

    # Iterate subsets of increasing length and store the minimum cost to reach each subset
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit
            for k in subset:
                prev_bits = bits & ~(1 << k)
                result = []
                for m in subset:
                    if m == 0 or m == k:
                        continue
                    result.append((C[(prev_bits, m)][0] + distance_matrix[m][k], m))
                C[(bits, k)] = min(result)

    # We're interested in the subset consisting of all nodes except the start node
    bits = (2**n - 1) - 1

    # Find the minimum cost to return to the start node
    result = []
    for k in range(1, n):
        result.append((C[(bits, k)][0] + distance_matrix[k][0], k))
    opt, parent = min(result)

    # Backtrack to find the full path
    path = []
    for i in range(n - 1):
        path.append(parent)
        bits, parent = bits & ~(1 << parent), C[(bits, parent)][1]
    path.append(0)
    path.reverse()

    return opt, path

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

opt, path = held_karp_tsp(distance_matrix)
print(f"Optimal tour cost: {opt}")
print(f"Optimal tour path: {path}")
