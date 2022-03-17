# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik definicji metody SOR

#########################################

# Import niezbędnych zależności
import time
import numpy as np

from ..common import common

"""
    Wejście (Parametry metody) [wymagania dla parametrów -> patrz: validator]:
        - A (macierz) - kwadratowa dwuwymiarowa macierz główna układu równań
        - b (wektor) - wektor wyrazów wolnych
        - max_iterations (liczba całkowita) - maksymalna liczba iteracji, która determinuje koniec obliczeń
        - tolerance (liczba zmiennoprzecinkowa) - zadana dokładność (tolerancja), która determinuje koniec obliczeń
        - w (liczba zmiennoprzecinkowa) - parametr relaksacji (0, 2)
        - x0 (wektor) [opcjonalne] - Początkowe przybliżenie rozwiązania
            - Jeśli argument nie został podany, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0
       
    Wyjście (Wartości zwracane przez funkcję):
        a) w przypadku poprawnych danych wejściowych
            - x (wektor) - wektor rozwiązań
            - iteration (liczba całkowita) - numer ostatniej wykonanej iteracji
            - elapsedTime (liczba zmiennoprzecinkowa) - czas obliczeń [s]
"""

# Definicja metody SOR
def sor(
    A: np.array,
    b: np.array,
    max_iterations: int,
    tolerance: float,
    w: float,
    x0: np.array = None,
):

    # Wykonanie części wspólnej dla wszystkich metod
    # Obejmuje to m.in walidację danych wejściowych i sprawdzenie warunku zbieżności
    startTime, size, x = common(A, b, max_iterations, tolerance, x0, w)

    # Pętla, która wykonuje się maksymalnie max_iterations-razy, chyba, że tolerancja zostanie wcześniej osiągnięta
    for iteration in range(max_iterations):

        # Zapisanie poprzedniego wektora przybliżeń
        x_old = x.copy()

        # Obliczenie kolejnego wektora przybliżeń rozwiązania
        for i in range(size):
            x[i] = (1 - w) * x[i] + (w / A[i, i]) * (
                b[i] - np.dot(A[i, :i], x[:i]) - np.dot(A[i, (i + 1) :], x_old[(i + 1) :])
            )

        # Sprawdzenie czy została osiągnięta podana tolerancja (warunek kończący)
        if sum(np.abs(x - x_old)) < tolerance:
            break

    # Obliczenie czasu operacji
    elapsedTime = time.time() - startTime

    # Zwrócenie liczby wykonanych iteracji i wektora wynikowego
    return x, iteration + 1, elapsedTime
