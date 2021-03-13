# Metoda Jacobiego (iteracji prostej)
# Autor: Łukasz Miłoś, 15.02.2021

import numpy as np
from ...abstract_method import AbstractMethod
from .validator import JacobiValidator

"""
    Wejście (Argumenty funkcji) [wymagania dla argumentów -> patrz: validator]:
        - A (macierz) - kwadratowa macierz układu równań
        - b (wektor)- wektor wartości po prawej stronie równiania Ax = b
        - x0 (wektor) [opcjonalne] - Początkowe przybliżenie niewiadomych układu
            - Jeśli argument nie został podany, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0
        - k (liczba całkowita) - maksymalna liczba iteracji, która determinuje koniec operacji
        - tol (liczba zmiennoprzecinkowa, podwójnej precyzji) - zadana dokladnosc (tolerancja), która determinuje koniec operacji

    Wyjście (Wartości zwracane przez funkcję):
        a) w przypadku poprawnych danych wejściowych
            - x - otrzymany wektor rozwiązań
            - kn - iteracja po ktorej metoda osiagnela zadana dokladnosc

        b) w przypadku błędnych danych wejściowych funkcja przerwie swoje działanie i zwróci błąd -> (patrz: validator)
"""


class JacobiMethod(AbstractMethod):
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

        # wyznaczenie L + U na podstawie wzoru
        # A = L + D + U
        # A = D + (L + U)
        # (L + U) = A - D

        # obliczenie różnicy wejściowej macierzy A i macierzy D, która ma wszystkie elementy zerowe, za wyjątkiem przekątnej (macierz diagonalna), która jest pobrana z macierzy wejściowej A
        # to sprawia, że wynikowa macierz L_plus_U na przekątnej będzie miała same zera
        # wynikiem jest suma macierzy górno- U i dolno- trójkątnej L
        L_plus_U = self._params.A - np.diagflat(D)

        # Alternatywny sposób polega na wyznaczeniu osobno macierzy L i U bez znajomości macierzy D na tym etapie
        # L = np.tril(A, -1)
        # U = np.triu(A, 1)
        # L_plus_U = L + U

        # Ax = b

        '''
            Przekształcenie wyjściowego wzoru
        
            A = L + D + U
            (L + D + U)x = b
            Lx + Dx + Ux = b
            Dx + (L + U)x = b       // - (L + U)x
            Dx = b - (L + U)x       // /D      ||     // * D^-1
            x = (b - (L + U)x) / D             ||     x = (b - (L + U)x) * D^-1
        '''

        return {'x': x, 'L_plus_U': L_plus_U, 'D': D}

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
