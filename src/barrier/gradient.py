import numpy as np
from src.problem.objective import f_objectif
from src.problem.constraints import g_contraintes

def fonction_barriere(X, mu):
    """
    phi(X) = f(X) - mu * sum(log(g_i(X)))
    """
    g = g_contraintes(X)

    # Vérifier domaine
    if np.any(g <= 0):
        return np.inf

    return f_objectif(X) - mu * np.sum(np.log(g))

def gradient_barriere(X, mu):
    """
    Gradient de la fonction barrière
    """
    x, y = X

    # Gradient de f
    grad_f = np.array([-3, -2])
    

    # Contraintes
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

    sum_term = np.zeros(2)

    for i in range(len(g)):
        sum_term += grad_g[i] / g[i]

    return grad_f - mu * sum_term