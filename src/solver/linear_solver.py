import numpy as np

def pivot_gauss(A, B):
    """
    Résout AX = B
    """
    return np.linalg.solve(A, B)