import sys
import os

# Ajouter src au path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from algorithm.mainbarriere import main_barrier
from problem.objective import grad_f, hess_f
from problem.constraints import g, grad_g, hess_g

def main():
    x0 = [1.0, 1.0]
    mu_init = 1.0
    theta = 0.5
    epsilon = 1e-4

    solution = main_barrier(
        x0,
        mu_init,
        theta,
        epsilon,
        grad_f,
        hess_f,
        g,
        grad_g,
        hess_g
    )

    print("\n✅ Solution optimale :", solution)


if __name__ == "__main__":
    main()