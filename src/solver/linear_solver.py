def solve_gauss(A, b):
    n = len(A)

    M = [A[i][:] + [b[i]] for i in range(n)]

    for i in range(n):
        pivot = M[i][i]

        if pivot == 0:
            raise ValueError("Pivot nul")

        for j in range(i, n + 1):
            M[i][j] /= pivot

        for k in range(n):
            if k != i:
                facteur = M[k][i]
                for j in range(i, n + 1):
                    M[k][j] -= facteur * M[i][j]

    return [M[i][n] for i in range(n)]