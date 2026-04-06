import numpy as np
from src.modules.solveur_numeric import pivot_gauss

"""
PROBLEMES RESOLUS DANS CE TEST :

1. Système Standard :
   3x + 2y = 1
   1x + 2y = 0
   Solution : x = 0.5, y = -0.25

2. Système avec Pivot Nul (nécessite un échange de lignes) :
   0x + 1y = 2
   1x + 1y = 3
   Solution : x = 1.0, y = 2.0
"""

def test_pivot_gauss():
    A = np.array([[3.0, 2.0], [1.0, 2.0]], dtype=float)
    b = np.array([1.0, 0.0], dtype=float)
    
    x = pivot_gauss(A, b)
    
    assert np.allclose(x, [0.5, -0.25])

    A_zero = np.array([[0.0, 1.0], [1.0, 1.0]], dtype=float)
    b_zero = np.array([2.0, 3.0], dtype=float)
    
    x_zero = pivot_gauss(A_zero, b_zero)
    assert np.allclose(x_zero, [1.0, 2.0])

if __name__ == "__main__":
    test_pivot_gauss()
    print("Tests réussis : Les deux problèmes sont résolus correctement.")
    