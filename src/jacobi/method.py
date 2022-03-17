# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik definicji metody Jacobiego

#########################################

# Import niezbędnych zależności
import time
import numpy as np

from ..common import common

"""
    Wejście (Parametry metod) [wymagania dla parametrów -> patrz: validator]:
        - A (macierz) - kwadratowa dwuwymiarowa macierz główna układu równań
        - b (wektor) - wektor wyrazów wolnych
         - max_iterations (liczba całkowita) - maksymalna liczba iteracji, która determinuje koniec obliczeń, gdy nie osiągnięto założonej dokładności
        - tolerance (liczba zmiennoprzecinkowa) - zadana dokładność (tolerancja), która determinuje koniec obliczeń
        - x0 (wektor) [opcjonalne] - początkowy wektor przybliżeń rozwiązania
            - Jeśli argument nie został podany, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0

    Wyjście (Wartości zwracane przez funkcję):
        a) w przypadku poprawnych danych wejściowych
            - x (wektor) - wektor rozwiązań
            - iteration (liczba całkowita) - liczba wykonanych iteracji
            - elapsedTime (liczba zmiennoprzecinkowa) - czas obliczeń [s]
"""

# Definicja metody Jacobiego
def jacobi(
    A: np.array,
    b: np.array,
    max_iterations: int,
    tolerance: float,
    x0: np.array = None,
):

    # Wykonanie części wspólnej dla wszystkich metod
    # Obejmuje to m.in walidację danych wejściowych i sprawdzenie warunku zbieżności
    startTime, _, x = common(A, b, max_iterations, tolerance, x0)

    # Wyznaczenie przekątnej macierzy A
    D = np.diag(A)

    # Wyznaczenie odwrotności przekątnej macierzy
    D_inv = np.linalg.inv(np.diag(D))

    # Wyznaczenie sumy macierzy dolno- i górno- trójkątnych
    L_plus_U = A - np.diag(D)

    # Pętla, która wykonuje się maksymalnie max_iterations-razy, chyba, że tolerancja zostanie wcześniej osiągnięta
    for iteration in range(max_iterations):

        # Zapisanie poprzedniego wektora przybliżeń
        x_old = x.copy()

        # Obliczenie kolejnego wektora przybliżeń rozwiązania
        x = np.dot(D_inv, b - np.dot(L_plus_U, x_old))

        # Sprawdzenie czy została osiągnięta podana tolerancja (warunek kończący)
        if sum(np.abs(x - x_old)) < tolerance:
            break

    # Obliczenie czasu operacji
    elapsedTime = time.time() - startTime

    # Zwrócenie liczby wykonanych iteracji i wektora wynikowego
    return x, iteration + 1, elapsedTime
