
from .Problem import g_contraintes, f_objectif
import numpy as np



def calculer_gradient(X, c, A, b, mu):
    """
    Formule : grad = c - mu * sum( grad_gi / gi )
    """
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

