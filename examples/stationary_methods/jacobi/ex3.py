import numpy as np
from src.stationary_methods.jacobi.method import jacobi

# Parametry wejściowe:
A = np.array([[10, -1, 2, 0], [-1, 11, -1, 3],
              [2, -1, 10, -1], [0, 3, -1, 8]])
b = np.array([6, 25, -11, 15])
max_iterations = 3
tolerance = 0.0001

# Rozwiązanie układu:
# x = [1.0000, 2.0000, -1.0000, 1.0000]

# Przewidywane wyniki :
# x0: [0.0000, 0.0000, 0.0000, 0.0000]
# x1: [0.6000, 2.2727, -1.1000, 1.8750]
# x2: [1.0473, 1.7159, -0.8052, 0.8852]
# x3: [0.9326, 2.0533, -1.0493, 1.1309]
# ...
# x23: [1.0000, 2.0000, -1.0000, 1.0000]

print("##### Metoda iteracyjna stacjonarna - Jacobi - Przykład 3 #####")

jacobi(A, b, max_iterations, tolerance)
