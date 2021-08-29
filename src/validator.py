import os
import json
import numpy as np

"""
    Validator sprawdza, czy dane wejściowe metod są prawidłowe.
    Jeśli dane są prawidłowe to zwraca SUCCESS (0), w innym przypadku zwraca kod błędu wraz z czytelną informacją.

    Wymagania Parametrów:
        - A (macierz)
            - nie może być pusta
            - powinna być dwuwymiarowa
            - musi być kwadratowa

        - b (wektor)
            - musi być wektorem (1 wymiar)
            - nie może być pusty
            - musi mieć rozmiar adekwatny do macierzy A

        - max_iterations (wartość całkowita) - maksymalna liczba iteracji, która determinuje koniec operacji
            - Liczba całkowita dodatnia

        - tolerance (double) - zadana dokladność (tolerancja), która determinuje koniec operacji
            - Liczba zmiennoprzecinkowa większa od 0

        [opcjonalny, walidacja tylko w przypadku podania parametru]
        - x0 (wektor)
            - musi być wektorem (1 wymiar)
            - nie może być pusty
            - musi mieć rozmiar adekwatny do macierzy A

        [opcjonalny, walidacja tylko w przypadku podania parametru]
        - w (double) - współczynnik relaksacji dla metody SOR
            - Liczba z zakresu (0, 2)
"""


class Validator:
    __errors: dict = None
    _SUCCESS: bool = 0

    # konstruktor przygotowujący kody i opisy błędów
    def __init__(self):
        directory = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(directory, 'errors.json')

        # wczytanie kodów i treści błędów z pliku errors.json.
        try:
            file = open(path)
            self.__errors = json.load(file)
            file.close()
        except:
            print('Nie znaleziono pliku błędów errors.json')

    # wyświetla treść błędu na ekranie i zwraca jego kod
    def __throwError(self, code: int):
        print(self.__errors[str(code)])
        return code

    # sprawdza poprawność parametrów, jeśli wszystko jest w porządku to zwraca _SUCCESS (0), inaczej zwraca kod błędu <1, ...>
    def validate(self, A: np.array, b: np.array, max_iterations: int, tolerance: float, x0: np.array = None, w: float = None):
        # sprawdzenie czy macierz A jest pusta
        if not A.size:
            return self.__throwError(1)

        # sprawdzenie czy macierz A jest dwuwymiarowa
        if A.ndim != 2:
            return self.__throwError(2)

         # sprawdzenie czy macierz A jest kwadratowa
        if A.shape[0] <= 1 or (A.shape[0] != A.shape[1]):
            return self.__throwError(3)

        # sprawdzenie czy wektor b jest pusty
        if not b.size:
            return self.__throwError(4)

        # sprawdzenie czy wektor b jest jednowymiarowy
        if b.ndim != 1:
            return self.__throwError(5)

        # sprawdzenie czy wektor b ma odpowiedni rozmiar
        if b.size != A.shape[0]:
            return self.__throwError(6)

        # sprawdzenie czy liczba max_iterations jest całkowita i dodatnia
        if not isinstance(max_iterations, int) or max_iterations <= 0:
            return self.__throwError(7)

        # sprawdzenie czy liczba tolerance jest mniejsza badz rowna 0
        if tolerance <= 0.0:
            return self.__throwError(8)

        # sprwadzenie czy x0 jest prawidłowe (jeśli podane)
        if x0 is not None:
            # sprawdzenie czy wektor  jest pusty
            if not x0.size:
                return self.__throwError(9)

            # sprawdzenie czy wektor x0 jest jednowymiarowy
            if x0.ndim != 1:
                return self.__throwError(10)

            # sprawdzenie czy wektor x0 ma odpowiedni rozmiar
            if x0.size != A.shape[0]:
                return self.__throwError(11)

        # sprawdzenie czy liczba w jest z zakresu (0, 2)
        if w is not None and (w < 0.0 or w > 2.0):
            return self.__throwError(12)

        return self._SUCCESS


# utworzenie walidatora
validator: Validator = Validator()
