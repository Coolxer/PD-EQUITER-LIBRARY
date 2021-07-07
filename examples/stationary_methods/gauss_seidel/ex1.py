import numpy as np
from src.stationary_methods.gauss_seidel.method import gauss_seidel

# Parametry wejściowe:
A = np.array([[16, 3], [7, -11]])
b = np.array([11, 13])
max_iterations = 3
tolerance = 0.0001
x0 = np.array([1, 1])

# Rozwiązanie układu:
# x = [0.8122, -0.6650]

# Przewidywane wyniki:
# x0: [1.0000, 1.0000]
# x1: [0.5000, -0.8636]
# x2: [0.8494, -0.6413]
# x3: [0.8077, -0.6678]
# ...
# x5: [0.8122, -0.6650]

print("##### Metoda iteracyjna stacjonarna - Gauss Seidel - Przykład 1 #####")

gauss_seidel(A, b, max_iterations, tolerance, x0)
