import numpy as np

def f_objectif(X, c):
    """Calcule c^T * X"""
    return np.dot(c, X)

def g_contraintes(X, A, b):
    """Calcule l'écart b - AX (doit être > 0)"""
    return b - np.dot(A, X)
