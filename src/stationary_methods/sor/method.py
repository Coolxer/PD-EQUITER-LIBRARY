import numpy as np
import time

from src.validator import validator
from src.stationary_methods.convergence import checkConditionOfConvergence

"""
    Wejście (Parametry metody) [wymagania dla parametrów -> patrz: validator]:
        - A (macierz) - kwadratowa dwuwymiarowa macierz układu równań
        - b (wektor)- wektor wartości po prawej stronie równiania Ax = b
         - max_iterations (liczba całkowita) - maksymalna liczba iteracji, która determinuje koniec operacji
        - tolerance (liczba zmiennoprzecinkowa, podwójnej precyzji) - zadana dokładność (tolerancja), która determinuje koniec operacji
        - w (liczba zmiennoprzecinkowa) - parametr relaksacji (0, 2)
        - x0 (wektor) [opcjonalne] - Początkowe przybliżenie niewiadomych układu
            - Jeśli argument nie został podany, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0

    Wyjście (Wartości zwracane przez funkcję):
        a) w przypadku poprawnych danych wejściowych
            - x - otrzymany wektor rozwiązań
            - iteration - numer ostatniej wykonanej iteracji
            - elapsedTime - czas obliczeń [s]

        b) w przypadku błędnych danych wejściowych funkcja przerwie swoje działanie i zwróci błąd -> [patrz: validator]
"""


def sor(A: np.array, b: np.array, max_iterations: int, tolerance: float, w: float, x0: np.array = None):

    # pobranie czasu startu operacji
    startTime = time.time()

    # walidacja danych wejściowych [patrz: validator]
    code: int = validator.validate(A, b, max_iterations, tolerance, x0)

    # jeśli wystąpił błąd to funkcja kończy swoje działanie
    if code:
        return code

    # sprawdzenie warunku zbieżności metody
    if(not checkConditionOfConvergence(A)):
        return

    # pobranie liczby wierszy macierzy
    size = np.shape(A)[0]

    # sprawdzenie czy wektor początkowych przybliżeń został podany
    # jeśli nie,to zostanie tworzony jest wektor wypełniony zerami
    if x0 is None:
        x = np.zeros(size)
    else:
        x = x0.copy()

    # pętla, która wykonuje się maksymalnie max_iterations-razy, chyba, że tolerancja zostanie wcześniej osiągnięta
    for iteration in range(max_iterations + 1):

        # zapisanie poprzedniego wektora przybliżeń
        x_old = x.copy()

        # obliczenie kolejnego wektora przybliżeń rozwiązania
        for i in range(size):
            x[i] = (1-w)*x[i] + (w / A[i, i])*(b[i] - np.dot(A[i, :i],
                                                             x[:i]) - np.dot(A[i, (i+1):], x_old[(i+1):]))

        # sprawdzenie czy została osiągnięta podana tolerancja (warunek kończący)
        if sum(np.abs(np.dot(A, x) - b)) < tolerance:
            break

    # obliczenie czasu operacji
    elapsedTime = time.time() - startTime

    # zwrocenie liczby wykonanych iteracji i wektora wynikowego
    return x, iteration, elapsedTime
