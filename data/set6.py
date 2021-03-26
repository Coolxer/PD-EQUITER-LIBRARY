import numpy as np
from equiter.src.method.parameters import Parameters

parameters: Parameters = Parameters(
    A=np.array([[16, 3], [7, -1]]),
    b=np.array([11, 13]),
    max_iterations=7,
    tolerance=0.0001,
    x0=np.array([1, 1]),
    w=None
)

# Przewidywane wyniki (Gauss-Seidel):
# x0: [1.0000, 1.0000]
# x2: [0.5000, -0.8636]
# x3: [0.8494, -0.6413]
# x4: [0.8077, -0.6678]
# x5: [0.8127, -0.6646]
# x6: [0.8121, -0.6650]
# x7: [0.8122, -0.6650]
# x7: [0.8122, -0.6650]
