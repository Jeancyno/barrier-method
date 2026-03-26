def gradient_barriere(x, mu, grad_f, g, grad_g):
    n = len(x)
    grad = grad_f(x)

    for i in range(len(g)):
        gi = g[i](x)

        if gi <= 0:
            raise ValueError("Contrainte violée")

        grad_gi = grad_g[i](x)

        for j in range(n):
            grad[j] -= mu * (grad_gi[j] / gi)

    return grad