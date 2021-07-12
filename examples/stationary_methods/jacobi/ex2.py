import numpy as np
from src.stationary_methods.jacobi.method import jacobi

# Parametry wejściowe:
A = np.array([[2, 1], [5, 7]])
b = np.array([11, 13])
max_iterations = 3
tolerance = 0.0001
x0 = np.array([1, 1])

# Rozwiązanie układu:
# x = [7.1111, -3.2222]

# Przewidywane wyniki:
# x0: [1.0000, 1.0000]
# x1: [5.0000, 1.1429]
# x2: [4.9286, -1.7143]
# x3: [6.3571, 1.6633]
# ...
# x40: [7.1111, -3.2222]

print("##### Metoda iteracyjna stacjonarna - Jacobi - Przykład 2 #####")

jacobi(A, b, max_iterations, tolerance, x0)
