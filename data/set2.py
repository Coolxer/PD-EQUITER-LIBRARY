import numpy as np
from equiter.src.method.parameters import Parameters

parameters: Parameters = Parameters(
    A=np.array([[3, 1, -1], [-1, 5, -1], [2, 4, 8]]),
    b=np.array([6, 10, 2]),
    max_iterations=3,
    tolerance=0.0001,
    x0=None,
    w=None
)

# Dokładnie rozwiązanie układu:
# x = [1.0000, 2.0000, -1.0000]

# Przewidywane wyniki (Jacobi):
# x0: [0.0000, 0.0000, 0.0000]
# x1: [2.0000, 2.0000, 0.2500]
# x2: [1.4166, 2.4500, -1.2500]
# x3: [0.7667, 2.0333, -1.3292]
