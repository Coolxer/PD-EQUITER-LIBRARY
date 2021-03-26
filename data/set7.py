import numpy as np
from equiter.src.method.parameters import Parameters

parameters: Parameters = Parameters(
    A=np.array([[2, 3], [5, 7]]),
    b=np.array([11, 13]),
    max_iterations=2,
    tolerance=0.0001,
    x0=np.array([1.1, 2.3]),
    w=None
)

# Przewidywane wyniki (Gauss-Seidel):
# x0: [1.1000, 2.3000]
# x2: [2.0500, 0.3930]
# x3: [4.9110, -1.6510]
