import numpy as np

def g_contraintes(X):
    """
    Retourne les contraintes sous forme g(x) > 0
    """
    x, y = X

    return np.array([
        10 - (2*x + y),  # g1
        8 - (x + y),     # g2
        x,               # g3
        y                # g4
    ])