def hessian_barriere(x, mu, hess_f, g, grad_g, hess_g):
    n = len(x)
    H = hess_f(x)

    for i in range(len(g)):
        gi = g[i](x)

        if gi <= 0:
            raise ValueError("Contrainte violée")

        grad_gi = grad_g[i](x)
        hess_gi = hess_g[i](x)

        for j in range(n):
            for k in range(n):
                term1 = (grad_gi[j] * grad_gi[k]) / (gi * gi)
                term2 = hess_gi[j][k] / gi
                H[j][k] += mu * (term1 - term2)

    return H