import numpy as np
from src.problem.constraints import g_contraintes

def calculer_hessienne(X, mu):
    """
    Hessienne de la fonction barrière
    """
    g = g_contraintes(X)

    if np.any(g <= 0):
        raise ValueError("Point hors domaine")

    # Gradients des contraintes
    grad_g = [
        np.array([-2, -1]),  # g1
        np.array([-1, -1]),  # g2
        np.array([1, 0]),    # g3
        np.array([0, 1])     # g4
    ]

    H = np.zeros((2, 2))

    for i in range(len(g)):
        gi = g[i]
        grad = grad_g[i].reshape(2, 1)

        # Produit matriciel
        H += (grad @ grad.T) / (gi**2)

    return mu * H