import numpy as np
from equiter.src.method.parameters import Parameters

parameters: Parameters = Parameters(
    A=np.array([[4, -1, -6, 0], [-5, -4, 10, 8],
                [0, 9, 4, -2], [1, 0, -7, 5, 4]]),
    b=np.array([2, 21, -12, -6]),
    max_iterations=4,
    tolerance=0.000001,
    x0=None,
    w=0.5
)

# Dokładnie rozwiązanie układu (SOR):
# x = [3.000000, -2.000000, 2.000000, 1.000000]

# Przewidywane wyniki:
# x0: [0.000000, 0.000000, 0.000000, 0.000000]
# x1: [0.250000, -2.781250, -1.628906, 0.515234]
# x2: [1.249023, -2.244897, 1.968771, 0.910855]
# x3: [2.070478, -1.669679, 1.590488, 0.761721]
