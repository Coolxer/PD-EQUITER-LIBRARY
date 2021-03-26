import numpy as np
from equiter.src.method.parameters import Parameters

parameters: Parameters = Parameters(
    A=np.array([[4, -1, -1], [-2, 6, 1], [-1, 1, 7]]),
    b=np.array([3, 9, -6]),
    max_iterations=6,
    tolerance=0.0001,
    x0=None,
    w=None
)

# Dokładnie rozwiązanie układu:
# x = [1.0000, 2.0000, -1.0000]

# Przewidywane wyniki (Gauss-Seidel):
# x0: [0.0000, 0.0000, 0.0000]
# x1: [0.7500, 1.7500, -1.0000]
# x2: [0.9380, 1.9790, -1.0060]
# x3: [0.9930, 1.9990, -1.0010]
# x4: [0.9990, 2.0000, -1.0000]
# x5: [1.0000, 2.0000, -1.0000]
