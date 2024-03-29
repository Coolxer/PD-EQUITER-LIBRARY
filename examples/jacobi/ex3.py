# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Źródło układu, dokładnego rozwiązania i przewidywanych wyników:
# https://en.wikipedia.org/wiki/Jacobi_method

# Plik przykładu nr 3 rozwiązania przy pomocy m. Jacobiego

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import NoReturn
import numpy as np
from ...src.jacobi.method import jacobi

# Parametry wejściowe
A = np.array([[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]])
b = np.array([6, 25, -11, 15])
max_iterations = 100
tolerance = 0.0001

# Rozwiązanie układu
# x = [1.0000, 2.0000, -1.0000, 1.0000]

# Przewidywane wyniki
# x0: [0.0000, 0.0000, 0.0000, 0.0000]
# x1: [0.6000, 2.2727, -1.1000, 1.8750]
# x2: [1.0473, 1.7159, -0.8052, 0.8852]
# x3: [0.9326, 2.0533, -1.0493, 1.1309]
# ...
# x23: [1.0000, 2.0000, -1.0000, 1.0000]

# Definicja metody przykładu
def jacobi_example_3() -> NoReturn:
    print("##### Metoda iteracyjna stacjonarna - Jacobi - Przykład 3 #####")
    x, i, t = jacobi(A, b, max_iterations, tolerance)

    print(f"Rozwiązanie: {x}")
    print(f"Liczba wykonanych iteracji: {i}")
    print(f"Czas obliczeń: {t}s")
