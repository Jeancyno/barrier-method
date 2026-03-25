import numpy as np
from src.barrier.gradient import gradient_barriere
from src.barrier.hessian import calculer_hessienne
from src.solver.linear_solver import pivot_gauss
from src.solver.line_search import recherche_lineaire

def boucle_newton(X, mu, tol=1e-6, max_iter=50):
    """
    Algorithme de Newton pour la fonction barrière
    """

    for i in range(max_iter):

        # 1. Gradient
        grad = gradient_barriere(X, mu)

        # 2. Hessienne
        H = calculer_hessienne(X, mu)

        # 3. Direction de Newton
        deltaX = -pivot_gauss(H, grad)

        # 4. Critère d'arrêt
        if np.linalg.norm(deltaX) < tol:
            print(f"Convergence atteinte en {i} itérations")
            break

        # 5. Recherche du pas
        alpha = recherche_lineaire(X, deltaX)

        # 6. Mise à jour
        X = X + alpha * deltaX

    return X