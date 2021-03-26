import numpy as np
from equiter.src.method.parameters import Parameters

parameters: Parameters = Parameters(
    A=np.array([[10, -1, 2, 0], [-1, 11, -1, 3],
                [2, -1, 10, -1], [0, 3, -1, 8]]),
    b=np.array([6, 25, -11, 15]),
    max_iterations=5,
    tolerance=0.000001,
    x0=None,
    w=None
)

# Dokładnie rozwiązanie układu:
# x = [1.000000, 2.000000, -1.000000, 1.000000]

# Przewidywane wyniki (Jacobi):
# x0: [0.000000, 0.000000, 0.000000, 0.000000]
# x1: [0.600000, 2.272700, -1.100000, 1.875000]
# x2: [1.047270, 1.715900, -0.805220, 0.885220]
# x3: [0.932630, 2.053300, -1.049300, 1.130880]
# x4: [1.015190, 1.953690, -0.968100, 0.973840]
# x5: [0.988990, 2.011400, -1.010200, 1.021350]
