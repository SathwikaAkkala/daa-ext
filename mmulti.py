
import sys

def matrix_chain_order(p):
    n = len(p) - 1  # Number of matrices
    m = [[0 for _ in range(n)] for _ in range(n)]  # DP table to store minimum multiplications
    s = [[0 for _ in range(n)] for _ in range(n)]  # Table to store split points

    # m[i][i] = 0 for all i
    for i in range(n):
        m[i][i] = 0

    # l is chain length
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i + l - 1
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k

    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        print(f"A{i+1}", end="")
    else:
        print("(", end="")
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(")", end="")

# Example usage
p = [30, 35, 15, 5, 10, 20, 25]  # Dimensions of matrices A1, A2, ..., A6
m, s = matrix_chain_order(p)

print("Minimum number of multiplications is:", m[0][len(p) - 2])
print("Optimal parenthesization is:", end=" ")
print_optimal_parens(s, 0, len(p) - 2)
print()
