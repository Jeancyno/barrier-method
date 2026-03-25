import numpy as np

def f_objectif(X):
    """
    f(x, y) = 3x + 2y
    """
    x, y = X
    return -(3*x + 2*y)