import numpy as np
from equiter.src.method.parameters import Parameters

parameters: Parameters = Parameters(
    A=np.array([[4, -1, 0], [-1, 4, -1], [0, 1, 4]]),
    b=np.array([2, 6, 2]),
    max_iterations=5,
    tolerance=0.0000001,
    x0=None,
    w=None
)

# Dokładnie rozwiązanie układu:
# x = [1.0000, 2.0000, 1.0000]


# Przewidywane wyniki (dla Gaussa-Seidla):
# x0: [0.0000, 0.0000, 0.0000]
# x1: [0.5000, 1.6250, 0.9062]
# x2: [0.9062, 1.9531, 0.9883]
# x3: [0.9883, 1.9941, 0.9985]
# x4: [0.9885, 1.9993, 0.9998]

# Przewidywane wyniki (dla SOR, dla w = 1.2):
# x0: [0.0000, 0.0000, 0.0000]
# x1: [0.6000, 1.9800, 1.1940]
# x2: [1.0740, 2.0844, 0.9865]
# x3: [1.0105, 1.9822, 0.9974]
# x4: [0.9925, 2.0005, 1.0007]

# Przewidywane wyniki (dla SOR, dla w = 1.1):
# x0: [0.0000, 0.0000, 0.0000]
# x1: [0.5500, 1.8013, 1.0453]
# x2: [0.9903, 2.0297, 1.0036]
# x3: [1.0091, 2.0005, 0.9998]
# x4: [0.9998, 1.9997, 0.9999]
