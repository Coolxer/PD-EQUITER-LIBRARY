# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik definicji metody Gaussa-Seidela

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import time
from typing import Tuple
import numpy as np
from numpy.linalg import inv, norm

from ..common import common

"""
    Wejście (Parametry metod) [wymagania dla parametrów -> patrz: validation]:
        - A (macierz => np.ndarray) - macierz główna układu równań
        - b (wektor => np.ndarray) - wektor wyrazów wolnych
        - max_iterations (liczba całkowita => int) - maksymalna liczba iteracji, która determinuje koniec obliczeń, gdy nie osiągnięto założonej dokładności
        - tolerance (liczba zmiennoprzecinkowa => float) - zadana dokładność (tolerancja) przybliżonego rozwiązania, która determinuje koniec obliczeń
        - x0 (wektor => np.ndarray) [opcjonalne] - początkowy wektor przybliżeń rozwiązania
            - Jeśli argument nie został podany, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0

    Wyjście (Wartości zwracane przez funkcję):
        a) w przypadku poprawnych danych wejściowych
            - x (wektor => np.ndarray) - wektor rozwiązań
            - iterations (liczba całkowita => int) - liczba wykonanych iteracji
            - elapsed_time (liczba zmiennoprzecinkowa => float) - czas obliczeń [s] z dokładnością do mikrosekundy

        b) w przypadku niepoprawnych danych wejściowych
            - None, None, None (krotka => Tuple)
"""

# Definicja metody Gaussa-Seidela
def gauss_seidel(
    A: np.ndarray,
    b: np.ndarray,
    max_iterations: int,
    tolerance: float,
    x0: np.ndarray = None,
) -> Tuple[np.ndarray, int, float]:

    # Wykonanie części wspólnej dla wszystkich metod
    # Obejmuje to m.in walidację danych wejściowych i sprawdzenie warunku zbieżności
    start_time, x, valid = common(A, b, max_iterations, tolerance, x0)

    # Jeśli dane wejściowe były nieprawidłowe to metoda przerywa działanie i zwraca (None, None, None)
    if not valid:
        return None, None, None

    # Wyznaczenie macierzy diagonalnej zbudowanej na podstawie głównej przekątnej macierzy 'A'
    D = np.diag(np.diag(A))

    # Wyznaczenie zmodyfikowanej macierzy dolno-trójkątnej (z zerowymi wartościami na głównej przekątnej)
    L = np.tril(A) - D

    # Wyznaczenie zmodyfikowanej macierzy górno-trójkątnej (z zerowymi wartościami na głównej przekątnej)
    U = np.triu(A) - D

    # Wyznaczenie odwrotności sumy macierzy  'D' i 'L'
    D_plus_L_inv = inv(D + L)

    # Pętla, która wykonuje się maksymalnie max_iterations-razy, chyba, że tolerancja zostanie wcześniej osiągnięta
    for iteration in range(max_iterations):

        # Obliczenie kolejnego wektora przybliżeń rozwiązania
        x = np.dot(D_plus_L_inv, b - np.dot(U, x))

        # Sprawdzenie czy została osiągnięta wymagana dokładność (warunek stopu)
        if (norm(np.dot(A, x) - b) / norm(b)) < tolerance:
            break

    # Obliczenie czasu operacji
    elapsed_time = time.time() - start_time

    # Zwrócenie liczby wykonanych iteracji i wektora wynikowego
    return x, iteration + 1, round(elapsed_time, 6)
