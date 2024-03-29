# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Źródło układu, dokładnego rozwiązania i przewidywanych wyników:
# https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method

# Plik przykładu nr 3 rozwiązania przy pomocy m. Gaussa-Seidela

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import NoReturn
import numpy as np
from ...src.gauss_seidel.method import gauss_seidel

# Parametry wejściowe
A = np.array([[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]])
b = np.array([6, 25, -11, 15])
max_iterations = 100
tolerance = 0.0001

# Rozwiązanie układu
# x = [1.0000, 2.0000, -1.0000, 1.0000]

# Przewidywane wyniki
# x0: [0.0000, 0.0000, 0.0000, 0.0000]
# x1: [0.6000, 2.3273, -0.9873, 0.8789]
# x2: [1.0302, 2.0369, -1.0145, 0.9843]
# x3: [1.0066, 2.0036, -1.0025, 0.9984]
# ...
# x9: [1.0000, 2.0000, -1.0000, 1.0000]

# Definicja metody przykładu
def gauss_seidel_example_3() -> NoReturn:
    print("##### Metoda iteracyjna stacjonarna - Gauss-Seidel - Przykład 3 #####")
    x, i, t = gauss_seidel(A, b, max_iterations, tolerance)

    print(f"Rozwiązanie: {x}")
    print(f"Liczba wykonanych iteracji: {i}")
    print(f"Czas obliczeń: {t}s")
