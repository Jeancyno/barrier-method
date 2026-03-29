
from .Problem import g_contraintes, f_objectif
import numpy as np

"""

def recherche_lineaire(X, delta, A, b):
    #Trouve le pas alpha maximal pour rester dans le domaine (gi > 0)
    alpha = 1.0
    tau = 0.99 # Marge de sécurité pour ne pas toucher le bord
    while np.any(g_contraintes(X + alpha * delta, A, b) <= 0):
        alpha *= 0.5
    return alpha * tau
"""

def recherche_lineaire(X, delta, A, b):
    """
    Trouve le pas alpha maximal tel que b - A(X + alpha*delta) > 0
    """
    alpha = 1.0
    tau = 0.99  # On s'arrête à 99% du chemin vers la contrainte
    
    # On définit g(x) = b - Ax
    def g(x_test):
        return b - np.dot(A, x_test)

    # Tant que le point testé (avec marge tau) touche ou dépasse une contrainte
    # On réduit alpha par itération
    while np.any(g(X + alpha * delta) <= (1 - tau) * b): 
        alpha *= 0.5
        
        # Sécurité pour éviter une boucle infinie si la direction est mauvaise
        if alpha < 1e-12:
            return 0.0
            
    return alpha


def pivot_gauss_robuste(A, b):
    n = len(b)
    Ab = np.hstack([A, b.reshape(-1, 1)]).astype(float)
    epsilon_machine = 1e-15 # Seuil de sécurité

    for i in range(n):
        # Pivotage partiel : on cherche l'élément max dans la colonne
        max_row = np.argmax(abs(Ab[i:, i])) + i
        if abs(Ab[max_row, i]) < epsilon_machine:
            # Si le pivot est trop petit, on ajoute une petite régularisation 
            # (souvent nécessaire en optimisation quand mu est minuscule)
            Ab[i, i] += epsilon_machine 
            
        Ab[i], Ab[max_row] = Ab[max_row].copy(), Ab[i].copy()
        
        for j in range(i + 1, n):
            facteur = Ab[j, i] / Ab[i, i]
            Ab[j, i:] -= facteur * Ab[i, i:]
            
    # Substitution inverse avec protection
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        pivot = Ab[i, i]
        if abs(pivot) < epsilon_machine:
            pivot = epsilon_machine if pivot >= 0 else -epsilon_machine
        
        somme_connue = np.dot(Ab[i, i+1:n], x[i+1:n])
        x[i] = (Ab[i, n] - somme_connue) / pivot
        
    return x

