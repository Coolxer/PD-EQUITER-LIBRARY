# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik definicji początkowej części wspólnej każdej z metod

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import niezbędnych zależności
import time
import numpy as np

from .validator import validator
from .convergence import checkConditionOfConvergence

"""
    Wejście (Parametry metod) [wymagania dla parametrów -> patrz: validator]:
        - A (macierz => np.array) - macierz główna układu równań
        - b (wektor => np.array) - wektor wyrazów wolnych
         - max_iterations (liczba całkowita => int) - maksymalna liczba iteracji, która determinuje koniec obliczeń, gdy nie osiągnięto założonej dokładności
        - tolerance (liczba zmiennoprzecinkowa => float) - zadana dokładność (tolerancja), która determinuje koniec obliczeń
        - x0 (wektor => np.array) [opcjonalne] - początkowy wektor przybliżeń rozwiązania
            - Jeśli argument nie został podany, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0
        - w (liczba zmiennoprzecinkowa => float) [tylko dla metody SOR] - parametr relaksacji
        
    Wyjście (Wartości zwracane przez metodę common, a nie przez właściwą metodę):
            - startTime (liczba zmiennoprzecinkowa => float) - czas rozpoczęcia operacji
            - size (krotka => tuple) - rozmiar macierzy głównej w postaci (n, m)
            - x (wektor => np.array) - początkowy wektor przybliżeń rozwiązania
            - valid (True/False => bool) - informacja czy wszystko przebiegło pomyślnie (dla poprawnych danych wejściowych zawsze True)

            Dla niepoprawnych danych wejściowych metoda  zawsze zwraca (None, None, None, False)
"""

# Definicja początkowej części wspólnej dla każdej z metod
def common(
    A: np.array,
    b: np.array,
    max_iterations: int,
    tolerance: float,
    x0: np.array = None,
    w: float = None,
) -> tuple(float, tuple, np.array, bool):
    # Pobranie czasu startu operacji
    startTime = time.time()

    # Walidacja danych wejściowych [patrz: validator] i sprawdzenie warunku zbieżności metody [patrz: convergence]
    if validator.validate(
        A, b, max_iterations, tolerance, x0, w
    ) != validator.SUCCESS or not checkConditionOfConvergence(A):
        return None, None, None, False

    # Pobranie liczby wierszy macierzy
    size = np.shape(A)[0]

    # Sprawdzenie czy początkowy wektor  przybliżeń został podany
    # Jeśli nie, to tworzony jest wektor wypełniony zerami
    if x0 is None:
        x = np.zeros(size)
    # Jeśli wektor został podany to jest on kopiowany do zmiennej x
    else:
        x = x0.copy()

    # Zwrócenie czasu startu operacji, rozmiaru macierzy głównej, początkowego wektora przybliżeń i informacji, że wszystko przebiegło pomyślnie
    return startTime, size, x, True
