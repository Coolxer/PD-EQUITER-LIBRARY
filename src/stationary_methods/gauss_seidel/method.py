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
        - x0 (wektor) [opcjonalne] - Początkowe przybliżenie niewiadomych układu
            - Jeśli argument nie został podany, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0

    Wyjście (Wartości zwracane przez funkcję):
        a) w przypadku poprawnych danych wejściowych
            - x - otrzymany wektor rozwiązań
            - iteration - numer ostatniej wykonanej iteracji
            - elapsedTime - czas obliczeń [s]

        b) w przypadku błędnych danych wejściowych funkcja przerwie swoje działanie i zwróci błąd -> [patrz: validator]
"""


def gauss_seidel(A: np.array, b: np.array, max_iterations: int, tolerance: float, x0: np.array = None):

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

    # wyznaczenie macierzy dolno-trójkątnej
    L = np.tril(A)

    # wyznaczenie macierzy U
    U = A - L

    # wyznaczenie sumy macierzy L i D
    L_plus_D = A - U

    # wyznaczenie odwrotności sumy macierzy L i D
    L_plus_D_inv = np.linalg.inv(L_plus_D)

    # pętla, która wykonuje się maksymalnie max_iterations-razy, chyba, że tolerancja zostanie wcześniej osiągnięta
    for iteration in range(max_iterations + 1):

        # zapisanie poprzedniego wektora przybliżeń
        x_old = x.copy()

        # obliczenie kolejnego wektora przybliżeń rozwiązania
        x = np.dot(L_plus_D_inv, b - np.dot(U, x_old))

        # sprawdzenie czy została osiągnięta podana tolerancja (warunek kończący)
        if sum(np.abs(np.dot(A, x) - b)) < tolerance:
            break

    # obliczenie czasu operacji
    elapsedTime = time.time() - startTime

    # zwrocenie liczby wykonanych iteracji i wektora wynikowego
    return x, iteration, elapsedTime