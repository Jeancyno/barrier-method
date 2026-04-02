from .barriere_logarithmique import calculer_gradient, calculer_hessienne
from .solveur_numeric import pivot_gauss_robuste, recherche_lineaire
import numpy as np



def boucle_newton(X, c, A, b, mu, tol_interne=1e-6):
    """
    Minimise la fonction barrière pour un mu fixe via la méthode de Newton.
    
    Paramètres :
    - X : Point de départ.
    - tol_interne : Seuil de convergence pour le gradient.
    """
    for i in range(50):
        grad = calculer_gradient(X, c, A, b, mu)
        # Condition d'arrêt : si le gradient est quasi nul, on a trouvé le minimum local
        if np.linalg.norm(grad) < tol_interne:
            break
            
        H = calculer_hessienne(X, A, b, mu)
        # Résolution du système H * delta = -grad pour trouver la direction de descente
        delta = pivot_gauss_robuste(H, -grad)
        
        # Recherche du pas alpha pour ne pas sortir du domaine réalisable
        alpha = recherche_lineaire(X, delta, A, b)
        X = X + alpha * delta

    return X

def solveur_universel_barriere(c, A, b, epsilon=1e-7, max_iter=100):
    """
    Algorithme global des points intérieurs (Méthode de la barrière).
    
    Paramètres :
    - epsilon : Précision globale (m * mu) attendue.
    - max_iter : Sécurité pour éviter les boucles infinies.
    
    Retourne : La solution optimale et l'historique des points pour le tracé.
    """
    n_vars = len(c)
    # X0 initial à l'intérieur du domaine (proche de l'origine)
    X = np.full(n_vars, 0.01) 
    
    mu = 1.0
    theta = 0.5 # Facteur de réduction du paramètre de barrière
    m = len(b)
    
    historique_X = [X.copy()]
    compteur = 0 
    
    print("Lancement de l'optimisation...")
    
    # Boucle principale : on réduit mu jusqu'à atteindre la précision epsilon
    while (m * mu) > epsilon and compteur < max_iter:
        try:
            # Appel de Newton pour converger vers le chemin central pour le mu actuel
            X = boucle_newton(X, c, A, b, mu)
            historique_X.append(X.copy())
            
            mu *= theta
            compteur += 1
            if compteur % 5 == 0:
                print(f"Itération {compteur} : mu = {mu:.5f}")
        except Exception as e:
            print(f"Erreur numérique : {e}")
            break
            
    return X, historique_X

