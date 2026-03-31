
from .Problem import g_contraintes, f_objectif
import numpy as np


def recherche_lineaire(X, delta, A, b):
    """
    Détermine le pas alpha pour rester dans le domaine réalisable (Ax < b).
    
    Paramètres :
    - X : Position actuelle.
    - delta : Direction de déplacement (pas de Newton).
    - tau : Marge de sécurité (0.99) pour ne pas heurter la frontière.
    """
    alpha = 1.0
    tau = 0.99 
    
    def g(x_test):
        return b - np.dot(A, x_test)

    # Réduit alpha par moitié tant que le prochain point viole une contrainte
    while np.any(g(X + alpha * delta) <= (1 - tau) * b): 
        alpha *= 0.5
        
        # Sécurité : évite le blocage si aucune progression n'est possible
        if alpha < 1e-12:
            return 0.0
            
    return alpha

def pivot_gauss_robuste(A, b):
    """
    Résout le système linéaire Ax = b par élimination de Gauss avec pivotage.
    
    Paramètres :
    - A : Matrice du système (Hessienne).
    - b : Second membre (Gradient négatif).
    """
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)]).astype(float)
    epsilon_machine = 1e-15 

    for i in range(n):
        # Pivotage partiel : échange de lignes pour maximiser le pivot (stabilité)
        max_row = np.argmax(abs(Ab[i:, i])) + i
        
        # Régularisation si le pivot est presque nul (matrice singulière)
        if abs(Ab[max_row, i]) < epsilon_machine:
            Ab[i, i] += epsilon_machine 
            
        Ab[i], Ab[max_row] = Ab[max_row].copy(), Ab[i].copy()
        
        # Élimination vers le bas
        for j in range(i + 1, n):
            facteur = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= facteur * Ab[i, i:]
            
    # Substitution inverse pour extraire les solutions x
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        pivot = Ab[i, i]
        # Protection finale contre la division par zéro
        if abs(pivot) < epsilon_machine:
            pivot = epsilon_machine if pivot >= 0 else -epsilon_machine
        
        somme_connue = np.dot(Ab[i, i+1:n], x[i+1:n])
        x[i] = (Ab[i, n] - somme_connue) / pivot
        
    return x
