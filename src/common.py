# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik definicji początkowej części wspólnej każdej z metod

########################################

# Import niezbędnych zależności
import time
import numpy as np

from validator import validator
from convergence import checkConditionOfConvergence

"""
    Wejście (Parametry metod) [wymagania dla parametrów -> patrz: validator]:
        - A (macierz) - kwadratowa dwuwymiarowa macierz główna układu równań
        - b (wektor) - wektor wyrazów wolnych
         - max_iterations (liczba całkowita) - maksymalna liczba iteracji, która determinuje koniec obliczeń, gdy nie osiągnięto założonej dokładności
        - tolerance (liczba zmiennoprzecinkowa) - zadana dokładność (tolerancja), która determinuje koniec obliczeń
        - x0 (wektor) [opcjonalne] - początkowy wektor przybliżeń rozwiązania
            - Jeśli argument nie został podany, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0
        - w (liczba zmiennoprzecinkowa) [tylko dla metody SOR] - parametr relaksacji (0, 2)
        

    Wyjście (Wartości zwracane przez metodę common):
        a) w przypadku poprawnych danych wejściowych
            - startTime (liczba zmiennoprzecinkowa) - czas rozpoczęcia operacji
            - size (krotka = tuple) - rozmiar macierzy głównej w postaci (n, m)
            - x (wektor) - początkowy wektor przybliżeń rozwiązania

        b) w przypadku błędnych danych wejściowych metoda przerywa swoje działanie i zwraca None, None, None
"""

# Definicja początkowej części wspólnej dla każdej z metod
def common(
    A: np.array,
    b: np.array,
    max_iterations: int,
    tolerance: float,
    x0: np.array = None,
    w: float = None,
):

    # Deklaracja zmiennej do oznaczenia poprawności danych wejściowych i inicjalizacja jej na None
    valid: bool = None

    # Pobranie czasu startu operacji
    startTime = time.time()

    # Walidacja danych wejściowych [patrz: validator]
    if not validator.validate(A, b, max_iterations, tolerance, x0, w):
        # Sprawdzenie warunku zbieżności metody
        if checkConditionOfConvergence(A):
            valid = True

    # Jeśli walidacja lub sprawdzenie warunku zbieżności się nie powiodło to zwróć None, None, None
    if valid is None:
        return None, None, None

    # Pobranie liczby wierszy macierzy
    size = np.shape(A)[0]

    # Sprawdzenie czy początkowy wektor  przybliżeń został podany
    # Jeśli nie, to tworzony jest wektor wypełniony zerami
    if x0 is None:
        x = np.zeros(size)  #
    # Jeśli wektor został podany to jest on kopiowany do zmiennej x
    else:
        x = x0.copy()

    # Zwrócenie czasu startu operacji, rozmiaru macierzy głównej i początkowego wektora przybliżeń
    return startTime, size, x
