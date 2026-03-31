import numpy as np

def f_objectif(X, c):
    """
    Calcule la valeur de la fonction coût : Z = cᵀ * X
    
    Paramètres :
    - X : Vecteur de décision actuel.
    - c : Vecteur des coefficients de l'objectif.
    """
    return np.dot(c, X)

def g_contraintes(X, A, b):
    """
    Calcule le vecteur d'écart : g(x) = b - AX
    
    Note : Pour que le point soit à l'intérieur du domaine, 
    chaque composante de ce vecteur doit être strictement positive (> 0).
    """
    return b - np.dot(A, X)
