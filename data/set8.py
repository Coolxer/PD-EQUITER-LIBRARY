import numpy as np
from equiter.src.method.parameters import Parameters

parameters: Parameters = Parameters(
    A=np.array([[10, -1, 2, 0], [-1, 11, -1, 3],
                [2, -1, 10, -1], [0, 3, -1, 8]]),
    b=np.array([6, 25, -11, 15]),
    max_iterations=4,
    tolerance=0.000001,
    x0=None,
    w=None
)

# Dokładnie rozwiązanie układu:
# x = [1.000000, 2.000000, -1.000000, 1.000000]

# Przewidywane wyniki (Gauss-Seidel):
# x0: [0.000000, 0.000000, 0.000000, 0.000000]
# x1: [0.600000, 2.327270, -0.987273, 0.878864]
# x2: [1.030180, 2.036940, -1.014460, 0.984341]
# x3: [1.006590, 2.003560, -1.002530, 0.998351]
# x4: [1.000860, 2.000300, -1.000310, 0.999850]
