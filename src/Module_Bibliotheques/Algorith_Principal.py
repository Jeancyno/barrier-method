from .Barriere_Logarithmique import calculer_gradient, calculer_hessienne
from .Solveur_Numeric import pivot_gauss_robuste, recherche_lineaire
import numpy as np




def boucle_newton(X, c, A, b, mu, tol_interne=1e-6):
    for i in range(50): # Max itérations Newton
        grad = calculer_gradient(X, c, A, b, mu)
        if np.linalg.norm(grad) < tol_interne:
            break
            
        H = calculer_hessienne(X, A, b, mu)
        delta = pivot_gauss_robuste(H, -grad)
        
        alpha = recherche_lineaire(X, delta, A, b)
        X = X + alpha * delta

    return X


def solveur_universel_barriere(c, A, b, epsilon=1e-7, max_iter=100):
    n_vars = len(c)
    # Départ très petit pour rester BIEN à l'intérieur du polyèdre
    X = np.full(n_vars, 0.01) 
    
    mu = 1.0
    theta = 0.5 # On descend plus doucement pour la 3D
    m = len(b)
    
    historique_X = [X.copy()]
    compteur = 0 # Sécurité
    
    print("Lancement de l'optimisation...")
    
    while (m * mu) > epsilon and compteur < max_iter:
        try:
            X = boucle_newton(X, c, A, b, mu)
            historique_X.append(X.copy())
            mu *= theta
            compteur += 1
            if compteur % 5 == 0:
                print(f"Itération {compteur} : mu = {mu:.5f}")
        except Exception as e:
            print(f"Erreur pendant le calcul : {e}")
            break # Arrêt propre en cas de problème numérique
            
    if compteur == max_iter:
        print("Attention : Nombre maximum d'itérations atteint !")
        
    return X, historique_X


