import numpy as np
from src.jacobi.method import jacobi

# Parametry wejściowe:
A = np.array([[3, 1, -1], [-1, 5, -1], [2, 4, 8]])
b = np.array([6, 10, 2])
max_iterations = 3
tolerance = 0.0001

# Rozwiązanie układu:
# x = [1.0000, 2.0000, -1.0000]

# Przewidywane wyniki:
# x0: [0.0000, 0.0000, 0.0000]
# x1: [2.0000, 2.0000, 0.2500]
# x2: [1.4167, 2.4500, -1.2500]
# x3: [0.7667, 2.0333, -1.3292]
# ...
# x29: [1.0000, 2.0000, -1.0000]

print("##### Metoda iteracyjna stacjonarna - Jacobi - Przykład 1 #####")

jacobi(A, b, max_iterations, tolerance)
