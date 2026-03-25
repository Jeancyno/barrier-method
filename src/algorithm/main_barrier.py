from src.algorithm.newton import boucle_newton

def main_barrier(X0, mu_init=1.0, epsilon=1e-6, theta=0.5):
    """
    Algorithme principal de la méthode des barrières
    """

    X = X0
    mu = mu_init

    iteration = 0

    while mu > epsilon:
        print(f"\n--- Itération barrière {iteration} | mu = {mu} ---")

        # Optimisation avec Newton
        X = boucle_newton(X, mu)

        # Diminuer mu
        mu *= theta
        iteration += 1

    return X