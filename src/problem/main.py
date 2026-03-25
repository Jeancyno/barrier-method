import numpy as np
from src.problem.objective import f_objectif
from src.problem.constraints import g_contraintes

X = np.array([1.0, 1.0])

print("f(X) =", f_objectif(X))
print("g(X) =", g_contraintes(X))