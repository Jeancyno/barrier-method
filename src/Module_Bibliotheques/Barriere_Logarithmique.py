
from .Problem import g_contraintes, f_objectif
import numpy as np


from .Problem import g_contraintes, f_objectif
import numpy as np

def calculer_gradient(X, c, A, b, mu):
    """
    Calcule le gradient de la fonction barrière : ∇B(x) = c + μ * Aᵀ * (1/g)
    
    Paramètres :
    - X  : Point actuel (vecteur n).
    - c  : Vecteur des coûts de l'objectif.
    - A, b : Matrice et vecteur des contraintes (Ax <= b).
    - mu : Paramètre de pénalité de la barrière.
    """
    gi = g_contraintes(X, A, b)
    # Terme de répulsion des contraintes
    term_barriere = np.dot(A.T, (1.0 / gi))
    return c + mu * term_barriere

def calculer_hessienne(X, A, b, mu):
    """
    Calcule la Hessienne de la barrière : H(x) = μ * Aᵀ * diag(1/g²) * A
    
    Paramètres :
    - X, A, b, mu : Identiques au gradient.
    """
    gi = b - np.dot(A, X)
    # Sécurité pour éviter la division par zéro
    gi = np.maximum(gi, 1e-9) 
    
    # Matrice diagonale des poids des contraintes
    D2 = np.diag(1.0 / (gi**2))
    H = mu * np.dot(A.T, np.dot(D2, A))
    
    # Régularisation pour garantir l'inversibilité (Stabilité numérique)
    return H + np.eye(len(X)) * 1e-8
























"""

def calculer_gradient(X, c, A, b, mu):
    
    # Formule : grad = c - mu * sum( grad_gi / gi )
    
    gi = g_contraintes(X, A, b)
    # Gradient de la barrière pour les contraintes b - AX
    # La dérivée de b - AiX par rapport à X est -Ai
    term_barriere = np.dot(A.T, (1.0 / gi))
    return c + mu * term_barriere

# Dans votre fonction de calcul de Hessienne :
def calculer_hessienne(X, A, b, mu):
    gi = b - np.dot(A, X)
    # Protection contre les gi <= 0
    gi = np.maximum(gi, 1e-9) 
    
    D2 = np.diag(1.0 / (gi**2))
    H = mu * np.dot(A.T, np.dot(D2, A))
    
    # AJOUT D'UNE RÉGULARISATION (La clé de la robustesse)
    # On ajoute une matrice identité minuscule
    return H + np.eye(len(X)) * 1e-8 

"""