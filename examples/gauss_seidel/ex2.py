# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Źródło układu, dokładnego rozwiązania i przewidywanych wyników:
# https://en.wikipedia.org/wiki/Gauss%E2%80%93Seidel_method

# Plik przykładu nr 2 rozwiązania przy pomocy m. Gaussa-Seidela

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import NoReturn
import numpy as np
from ...src.gauss_seidel.method import gauss_seidel

# Parametry wejściowe
A = np.array([[2, 3], [5, 7]])
b = np.array([11, 13])
max_iterations = 100
tolerance = 0.0001
x0 = np.array([1.1, 2.3])

# Przewidywane wyniki
# Warunek zbieżnosci nie jest spełniony!

# Definicja metody przykładu
def gauss_seidel_example_2() -> NoReturn:
    print("##### Metoda iteracyjna stacjonarna - Gauss-Seidel - Przykład 2 #####")
    x, i, t = gauss_seidel(A, b, max_iterations, tolerance, x0)

    print(f"Rozwiązanie: {x}")
    print(f"Liczba wykonanych iteracji: {i}")
    print(f"Czas obliczeń: {t}s")
