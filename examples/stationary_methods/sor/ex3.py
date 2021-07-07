import numpy as np
from src.stationary_methods.sor.method import sor

# Parametry wejściowe:
A = np.array([[2, 0, 1], [0, 2, 1],
              [0, 1, 2]])
b = np.array([6, 3, 4.5])
max_iterations = 3
tolerance = 0.0001
w = 1.1

# Rozwiązanie układu:
# x = [2.0000, 0.5000, 2.0000]

# Przewidywane wyniki:
# x0: [0.0000, 0.0000, 0.0000]
# x1: [3.3000, 1.6500, 1.5675]
# x2: [2.1079, 0.6229, 1.9757]
# x3: [2.0026, 0.5011, 2.0018]
# ...
# x9: [2.0000, 0.5000, 2.0000]

print("##### Metoda iteracyjna stacjonarna - SOR - Przykład 3 #####")

sor(A, b, max_iterations, tolerance, w)
