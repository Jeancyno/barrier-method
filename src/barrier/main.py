import numpy as np
from src.barrier.gradient import fonction_barriere, gradient_barriere

X = np.array([1.0, 1.0])
mu = 1.0

print("phi(X) =", fonction_barriere(X, mu))
print("grad phi(X) =", gradient_barriere(X, mu))

# import numpy as np
# from src.barrier.hessian import calculer_hessienne

# X = np.array([1.0, 1.0])
# mu = 1.0

# H = calculer_hessienne(X, mu)

# print("Hessienne =\n", H)