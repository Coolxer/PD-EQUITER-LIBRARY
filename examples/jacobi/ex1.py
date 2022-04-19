# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Źródło układu, dokładnego rozwiązania i przewidywanych wyników:
# "Metody Numeryczne, Wykład 5, Układy równań liniowych - metody iteracyjne",
# dr inż. prof. PRz Mariusz Borkowski

# Plik przykładu nr 1 rozwiązania przy pomocy m. Jacobiego

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import NoReturn
import numpy as np
from ...src.jacobi.method import jacobi

# Parametry wejściowe
A = np.array([[3, 1, -1], [-1, 5, -1], [2, 4, 8]])
b = np.array([6, 10, 2])
max_iterations = 100
tolerance = 0.0001

# Rozwiązanie układu
# x = [1.0000, 2.0000, -1.0000]

# Przewidywane wyniki
# x0: [0.0000, 0.0000, 0.0000]
# x1: [2.0000, 2.0000, 0.2500]
# x2: [1.4167, 2.4500, -1.2500]
# x3: [0.7667, 2.0333, -1.3292]
# ...
# x29: [1.0000, 2.0000, -1.0000]

# Definicja metody przykładu
def jacobi_example_1() -> NoReturn:
    print("##### Metoda iteracyjna stacjonarna - Jacobi - Przykład 1 #####")
    x, i, t = jacobi(A, b, max_iterations, tolerance)

    print(f"Rozwiązanie: {x}")
    print(f"Liczba wykonanych iteracji: {i}")
    print(f"Czas obliczeń: {t}s")
