# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik przykładu nr 1 rozwiązania przy pomocy m. SOR

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import NoReturn
import numpy as np
from ...src.sor.method import sor

# Parametry wejściowe
A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])
b = np.array([2, 6, 2])
max_iterations = 3
tolerance = 0.0001
w = 1.1

# Rozwiązanie układu
# x = [1.0000, 2.0000, 1.0000]

# Przewidywane wyniki
# x0: [0.0000, 0.0000, 0.0000]
# x1: [0.5500, 1.8013, 1.0453]
# x2: [0.9903, 2.0297, 1.0036]
# x3: [1.0091, 2.0005, 0.9998]
# ...
# x10: [1.0000, 2.0000, 1.0000]

# Definicja metody przykładu
def sor_example_1() -> NoReturn:
    print("##### Metoda iteracyjna stacjonarna - SOR - Przykład 1 #####")
    x, i, t = sor(A, b, max_iterations, tolerance, w)

    print(f"Rozwiązanie: {x}")
    print(f"Liczba wykonanych iteracji: {i}")
    print(f"Czas obliczeń: {t}s")
