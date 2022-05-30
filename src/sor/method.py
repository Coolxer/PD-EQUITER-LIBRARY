# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik definicji metody SOR

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import time
from typing import Tuple
import numpy as np
from numpy.linalg import inv, norm

from ..common import common

"""
    Wejście (Parametry metody) [wymagania dla parametrów -> patrz: validation]:
        - A (macierz => np.ndarray) - macierz główna układu równań
        - b (wektor => np.ndarray) - wektor wyrazów wolnych
        - max_iterations (liczba całkowita => int) - maksymalna liczba iteracji, która determinuje koniec obliczeń
        - tolerance (liczba zmiennoprzecinkowa => float) - zadana dokładność (tolerancja) przybliżonego rozwiązania, która determinuje koniec obliczeń
        - w (liczba zmiennoprzecinkowa =>  float) - parametr relaksacji
        - x0 (wektor => np.ndarray) [opcjonalne] - Początkowe przybliżenie rozwiązania
            - Jeśli argument nie został podany, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0
       
    Wyjście (Wartości zwracane przez funkcję):
        a) w przypadku poprawnych danych wejściowych
            - x (wektor => np.ndarray) - wektor rozwiązań
            - iterations (liczba całkowita => int) - liczba wykonanych iteracji
            - elapsed_time (liczba zmiennoprzecinkowa => float) - czas obliczeń [s] z dokładnością do mikrosekundy

        b) w przypadku niepoprawnych danych wejściowych
            - None, None, None (krotka => Tuple)
"""

# Definicja metody SOR
def sor(
    A: np.ndarray,
    b: np.ndarray,
    max_iterations: int,
    tolerance: float,
    w: float,
    x0: np.ndarray = None,
) -> Tuple[np.ndarray, int, float]:

    # Wykonanie części wspólnej dla wszystkich metod
    # Obejmuje to m.in. walidację danych wejściowych i sprawdzenie warunku zbieżności
    start_time, x, valid = common(A, b, max_iterations, tolerance, x0, w)

    # Jeśli dane wejściowe były nieprawidłowe to metoda przerywa działanie i zwraca (None, None, None)
    if not valid:
        return None, None, None

    # Wyznaczenie macierzy diagonalnej zbudowanej na podstawie głównej przekątnej macierzy 'A'
    D = np.diag(np.diag(A))

    # Wyznaczenie zmodyfikowanej macierzy dolno-trójkątnej (z zerowymi wartościami na głównej przekątnej)
    L = np.tril(A) - D

    # Wyznaczenie zmodyfikowanej macierzy górno-trójkątnej (z zerowymi wartościami na głównej przekątnej)
    U = np.triu(A) - D

    # Wyznaczenie odwróconej sumy macierzy 'D' i iloczynu parametru 'w' z macierzą 'L'
    D_plus_wL_inv = inv(D + (w * L))

    # Wyznaczenie iloczynu parametru 'w' z wektorem 'b'
    wb = w * b

    # Wyznaczenie kolejnego składnika wzoru metody
    wU_plus_w_min_1_dot_D = (w * U) + ((w - 1) * D)

    # Pętla, która wykonuje się maksymalnie max_iterations-razy, chyba, że tolerancja zostanie wcześniej osiągnięta
    for iteration in range(max_iterations):

        # Obliczenie kolejnego wektora przybliżeń rozwiązania
        x = np.dot(D_plus_wL_inv, (wb - np.dot(wU_plus_w_min_1_dot_D, x)))

        # Sprawdzenie czy została osiągnięta wymagana dokładność (warunek stopu)
        if (norm(np.dot(A, x) - b) / norm(b)) < tolerance:
            break

    # Obliczenie czasu operacji
    elapsed_time = time.time() - start_time

    # Zwrócenie liczby wykonanych iteracji i wektora wynikowego
    return x, iteration + 1, round(elapsed_time, 6)
