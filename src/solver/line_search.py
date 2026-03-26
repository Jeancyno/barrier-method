def line_search(x, delta_x, g, alpha=1.0, beta=0.5):
    while True:
        x_new = [x[i] + alpha * delta_x[i] for i in range(len(x))]

        faisable = True
        for gi in g:
            if gi(x_new) <= 0:
                faisable = False
                break

        if faisable:
            return alpha

        alpha *= beta