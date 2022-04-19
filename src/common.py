# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik definicji początkowej części wspólnej każdej z metod

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import time
from typing import Tuple
import numpy as np

from .validation import validate_input_parameters, SUCCESS
from .convergence import check_condition_of_convergence

"""
    Wejście (Parametry metod) [wymagania dla parametrów -> patrz: validation]:
        - A (macierz => np.ndarray) - macierz główna układu równań
        - b (wektor => np.ndarray) - wektor wyrazów wolnych
        - max_iterations (liczba całkowita => int) - maksymalna liczba iteracji, która determinuje koniec obliczeń, gdy nie osiągnięto założonej dokładności
        - tolerance (zmiennoprzecinkowa => float) - zadana dokładność (tolerancja) przybliżonego rozwiązania, która determinuje koniec obliczeń
        - x0 (wektor => np.ndarray) [opcjonalne] - początkowy wektor przybliżeń rozwiązania
            - Jeśli argument nie został podany, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0
        - w (zmiennoprzecinkowa => float) [tylko dla metody SOR] - parametr relaksacji
        
    Wyjście (Wartości zwracane przez metodę common, a nie przez właściwą metodę):
            - start_time (liczba zmiennoprzecinkowa => float) - czas rozpoczęcia operacji
            - x (wektor => np.ndarray) - początkowy wektor przybliżeń rozwiązania
            - valid (True/False => bool) - informacja czy wszystko przebiegło pomyślnie (dla poprawnych danych wejściowych zawsze True)

            Dla niepoprawnych danych wejściowych metoda  zawsze zwraca (None, None, None, False)
"""

# Definicja początkowej części wspólnej dla każdej z metod obejmujej uruchomienie licznika, walidację parametrów i przygotowanie początkowego wektora przybliżeń
def common(
    A: np.ndarray,
    b: np.ndarray,
    max_iterations: int,
    tolerance: float,
    x0: np.ndarray = None,
    w: float = None,
) -> Tuple[float, tuple, np.ndarray, bool]:

    # Pobranie czasu startu operacji
    start_time = time.time()

    # Walidacja danych wejściowych [patrz: validation] i sprawdzenie warunku zbieżności metody [patrz: convergence]
    if validate_input_parameters(
        A, b, max_iterations, tolerance, x0, w
    ) != SUCCESS or not check_condition_of_convergence(A):
        return None, None, None, False

    # Pobranie liczby wierszy macierzy
    size = np.shape(A)[0]

    # Sprawdzenie czy początkowy wektor przybliżeń został podany
    # Jeśli nie, to tworzony jest wektor wypełniony zerami
    if x0 is None:
        x = np.zeros(size)
    # Jeśli wektor został podany to jest on kopiowany do zmiennej 'x'
    else:
        x = x0.copy()

    # Zwrócenie czasu startu operacji, rozmiaru macierzy głównej, początkowego wektora przybliżeń i informacji, że wszystko przebiegło pomyślnie
    return start_time, x, True
