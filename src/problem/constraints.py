def g1(x):
    return 10 - 2*x[0] - x[1]

def g2(x):
    return 8 - x[0] - x[1]

def g3(x):
    return x[0]

def g4(x):
    return x[1]


g = [g1, g2, g3, g4]


def grad_g1(x):
    return [-2, -1]

def grad_g2(x):
    return [-1, -1]

def grad_g3(x):
    return [1, 0]

def grad_g4(x):
    return [0, 1]


grad_g = [grad_g1, grad_g2, grad_g3, grad_g4]


def hess_zero(x):
    return [
        [0, 0],
        [0, 0]
    ]


hess_g = [hess_zero, hess_zero, hess_zero, hess_zero]