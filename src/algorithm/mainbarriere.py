from algorithm.newton import newton_step


def main_barrier(x0, mu_init, theta, epsilon,
                 grad_f, hess_f, g, grad_g, hess_g):

    x = x0[:]
    mu = mu_init

    iteration = 0

    while mu > epsilon:
        print(f"\n=== Iteration barriere {iteration} | mu = {mu} ===")

        for k in range(20):
            x = newton_step(x, mu, grad_f, hess_f, g, grad_g, hess_g)
            print(f"Newton {k} -> x = {x}")

        mu *= theta
        iteration += 1

    return x