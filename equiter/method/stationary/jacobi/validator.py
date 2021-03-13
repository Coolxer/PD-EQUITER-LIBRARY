# Walidator metody Jacobiego (iteracji prostej)

# Autor: Łukasz Miłoś, 15.02.2021

from ...parameters import Parameters
from ...abstract_validator import *

'''
    Walidator sprawdza, czy dane wejściowe metody są prawidłowe.
    Jeśli dane są prawidłowe to zwraca 0, w innym przypadku zwraca kod błędu wraz z czytelną informacją

    Wymagania Argumentów funkcji:
        - A (macierz)
            - nie może być pusta
            - musi być kwadratowa

        - b (wektor)
            - nie może być pusty
            - musi mieć rozmiar adekwatny do macierzy A

        - k (wartość całkowita) - maksymalna liczba iteracji, która determinuje koniec operacji
            - Liczba całkowita dodatnia

        - tol (double) - zadana dokladnosc (tolerancja), która determinuje koniec operacji
            - Liczba różna od 0
'''

# Kody błędów wraz z opisami
errors: dict = {
    1: "Macierz A nie moze byc pusta!",
    2: "Macierz A musi byc kwadratowa!",
    3: "Wektor b nie moze byc pusty!",
    4: "Wektor b musi mieć odpowiedni rozmiar",
    5: "Liczba k musi byc calkowita dodatnia!",
    6: "Liczba tol musi byc rozna od 0!"
}


class JacobiValidator(AbstractValidator):
    def __init__(self, errors: dict):
        super().__init__(errors)

    def validate(self, params: Parameters):
        # sprawdzenie czy macierz A jest pusta
        if (not params.A.size):
            return self._error(1)

        # sprawdzenie czy macierz A jest kwadratowa
        if(params.A.shape[0] != params.A.shape[1]):
            return self._error(2)

        # sprawdzenie czy wektor b jest pusty
        if(not params.b.size):
            return self._error(3)

        # sprawdzenie czy wektor b ma odpowiedni rozmiar
        if(params.b.size != params.A.shape[0]):
            return self._error(4)

        # sprawdzenie czy liczba max_iterations jest całkowita i dodatnia
        if(not isinstance(params.max_iterations, int) or params.max_iterations <= 0):
            return self._error(5)

        # sprawdzenie czy liczba tolerance jest różna od 0
        if(params.tolerance == 0):
            return self._error(6)

        return self._SUCCESS
