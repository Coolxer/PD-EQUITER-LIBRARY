# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik przykładu nr 2 rozwiązania przy pomocy m. SOR

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
from typing import NoReturn
import numpy as np
from ...src.sor.method import sor

# Parametry wejściowe
A = np.array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])
b = np.array([2, 6, 2])
max_iterations = 100
tolerance = 0.0001
w = 1.2

# Rozwiązanie układu
# x = [1.0000, 2.0000, 1.0000]

# Przewidywane wyniki
# x0: [0.0000, 0.0000, 0.0000]
# x1: [0.6000, 1.9800, 1.1940]
# x2: [1.0740, 2.0844, 0.9865]
# x3: [1.0105, 1.9822, 0.9974]
# ...
# x13: [1.0000, 2.0000, 1.0000]

# Definicja metody przykładu
def sor_example_2() -> NoReturn:
    print("##### Metoda iteracyjna stacjonarna - SOR - Przykład 2 #####")
    x, i, t = sor(A, b, max_iterations, tolerance, w)

    print(f"Rozwiązanie: {x}")
    print(f"Liczba wykonanych iteracji: {i}")
    print(f"Czas obliczeń: {t}s")
