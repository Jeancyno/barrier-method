from barrier.gradient import gradient_barriere
from barrier.hessian import hessian_barriere
from solver.linear_solver import solve_gauss
from solver.line_search import line_search


def newton_step(x, mu, grad_f, hess_f, g, grad_g, hess_g):
    grad = gradient_barriere(x, mu, grad_f, g, grad_g)
    H = hessian_barriere(x, mu, hess_f, g, grad_g, hess_g)

    minus_grad = [-val for val in grad]
    delta_x = solve_gauss(H, minus_grad)

    alpha = line_search(x, delta_x, g)

    x_new = [x[i] + alpha * delta_x[i] for i in range(len(x))]

    return x_new