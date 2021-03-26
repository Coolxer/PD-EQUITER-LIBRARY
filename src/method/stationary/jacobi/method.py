import numpy as np

from equiter.src.method.abstract_method import AbstractMethod, Parameters
from equiter.src.method.validator import Validator


class JacobiMethod(AbstractMethod):
    # przygotowanie danych do obliczeń, indywidualne dla każdej metody (przeciążane)
    def _prepare(self, parameters: Parameters):

        # pobranie wielkości macierzy wejściowej A
        size = np.shape(parameters.A)[0]

        # początkowe przybliżenie (wektor x0) nie jest wymagany
        # dlatego jeśli nie został on podany to zostaje utworzony wektor zerowy
        if(parameters.x0 is None):
            x = np.zeros(size)
        else:
            x = parameters.x0

        # pobranie przekątnej D wejściowej macierzy A
        D = np.diag(parameters.A)

        # wyznaczenie L + U
        L = np.tril(parameters.A, -1)
        U = np.triu(parameters.A, 1)
        L_plus_U = L + U

        # alternatywny sposób to obliczenie różnicy wejściowej macierzy A i macierzy D, która ma wszystkie elementy zerowe, za wyjątkiem przekątnej (macierz diagonalna), która jest pobrana z macierzy wejściowej A
        # to sprawia, że wynikowa macierz L_plus_U na przekątnej będzie miała same zera
        # wynikiem jest suma macierzy górno- U i dolno- trójkątnej L
        # L_plus_U = self._params.A - np.diagflat(D)

        return {'x': x, 'L_plus_U': L_plus_U, 'D': D}

    # szukanie rozwiązania (iteracyjnie), indywidualne dla każdej metody (przeciążane)
    def _operation(self, parameters: Parameters, temp: dict):
        x = temp['x']

        # obliczenie macierzy odwrotnej D dla alternatywnego sposobu rozwiązania
        # D_inv = np.diagflat(np.linalg.inv(temp['D']))

        # pętla, która wykonuje się maksymalnie params.max_iterations-razy, chyba, że tolerancja zostanie wcześniej osiągnięta
        for i in range(parameters.max_iterations):
            # obliczenie kolejnego wektora przybliżenia rozwiązań
            x = (parameters.b - np.dot(temp['L_plus_U'], x)) / temp['D']

            # alternatywnie z wykorzystaniem D^(-1)
            # x = np.dot(parameters.b, D_inv) - np.dot(np.dot(temp['L_plus_U'], x), D_inv)

            # sprawdzenie czy została osiągnięta podana tolerancja (warunek kończący)
            if(sum(np.abs(np.dot(parameters.A, x) - parameters.b)) < parameters.tolerance):
                break

        # zwrocenie liczby wykonanych iteracji i wektora wynikowego
        return i, x
