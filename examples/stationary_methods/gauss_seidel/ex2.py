import numpy as np
from src.stationary_methods.gauss_seidel.method import gauss_seidel

# Parametry wejściowe:
A = np.array([[2, 3], [5, 7]])
b = np.array([11, 13])
max_iterations = 100
tolerance = 0.000001
x0 = np.array([1.1, 2.3])

# Przewidywane wyniki:
# Warunek konieczny zbieżnosci ciągu nie jest spełniony!

print("##### Metoda iteracyjna stacjonarna - Gauss Seidel - Przykład 2 #####")

gauss_seidel(A, b, max_iterations, tolerance, x0)
