import numpy as np
from src.problem.constraints import g_contraintes

def recherche_lineaire(X, deltaX, alpha=1.0, beta=0.5):
    """
    Trouve un pas alpha pour rester dans le domaine
    """
    while True:
        X_new = X + alpha * deltaX
        g = g_contraintes(X_new)

        if np.all(g > 0):
            break

        alpha *= beta

    return alpha