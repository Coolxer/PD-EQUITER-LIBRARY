import numpy as np
from equiter.src.method.parameters import Parameters

parameters: Parameters = Parameters(
    A=np.array([[2, 1], [-5, 7]]),
    b=np.array([11, 13]),
    max_iterations=25,
    tolerance=0.000001,
    x0=np.array([1, 1]),
    w=None
)

# Przewidywane wyniki (Jacobi):
# x0: [1.0000, 1.0000]
# x25: [7.1110, -3.2220]
