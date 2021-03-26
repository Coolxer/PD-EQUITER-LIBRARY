# Metoda Gaussa-Seidela

import numpy as np

from equiter.src.method.abstract_method import AbstractMethod
from equiter.src.method.stationary.jacobi.validator import JacobiValidator

"""
    Wejście (Parametry metody) [wymagania dla parametrów -> patrz: validator]:
        - A (macierz) - kwadratowa dwuwymiarowa macierz układu równań
        - b (wektor)- wektor wartości po prawej stronie równiania Ax = b
        - x0 (wektor) [opcjonalne] - Początkowe przybliżenie niewiadomych układu
            - Jeśli argument nie został podany, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0
        - k (liczba całkowita) - maksymalna liczba iteracji, która determinuje koniec operacji
        - tol (liczba zmiennoprzecinkowa, podwójnej precyzji) - zadana dokładność (tolerancja), która determinuje koniec operacji

    Wyjście (Wartości zwracane przez funkcję):
        a) w przypadku poprawnych danych wejściowych
            - x - otrzymany wektor rozwiązań
            - kn - iteracja po ktorej metoda osiagnela zadana dokładność

        b) w przypadku błędnych danych wejściowych funkcja przerwie swoje działanie i zwróci błąd -> (patrz: validator)
"""


class GaussSeidelMethod(AbstractMethod):
    # konstruktor
    def __init__(self, validator: JacobiValidator):
        super().__init__(validator)

    # przygotowanie danych do obliczeń, indywidualne dla każdej metody (przeciążane)
    def _prepare(self):
        # pobranie wielkości macierzy wejściowej A
        size = np.shape(self._params.A)[0]

        # początkowe przybliżenie (wektor x0) nie jest wymagany
        # dlatego jeśli nie został on podany to zostaje utworzony wektor zerowy
        if(self._params.x0 is None):
            x = np.zeros(size)
        else:
            x = self._params.x0

        # pobranie przekątnej D wejściowej macierzy A
        D = np.diag(self._params.A)

        # wyznaczenie L + D
        L = np.tril(self._params.A, -1)
        L_plus_D = L + D

        return {'x': x, 'L_plus_D': L_plus_D, 'D': D}

    # szukanie rozwiązania (iteracyjnie), indywidualne dla każdej metody (przeciążane)
    def _operation(self, temp: dict):
        x = temp['x']

        # pętla, która wykonuje się maksymalnie params.max_iterations-razy, chyba, że tolerancja zostanie wcześniej osiągnięta
        for i in range(self._params.max_iterations):
            # obliczenie kolejnego wektora przybliżenia rozwiązań
            x = (self._params.b - np.dot(temp['L_plus_U'], x)) / temp['D']

            # sprawdzenie czy została osiągnięta podana tolerancja (warunek kończący)
            if(sum(np.abs(np.dot(self._params.A, x) - self._params.b)) < self._params.tolerance):
                break

        # zwrocenie liczby wykonanych iteracji i wektora wynikowego
        return i, x
