import os
import json

from equiter.src.method.parameters import Parameters


"""
    Klasa Validator sprawdza, czy dane wejściowe metody są prawidłowe.
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

        - k (wartość całkowita) - maksymalna liczba iteracji, która determinuje koniec operacji
            - Liczba całkowita dodatnia

        - tol (double) - zadana dokladnosc (tolerancja), która determinuje koniec operacji
            - Liczba różna od 0

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

        try:
            file = open(path)
            self.__errors = json.load(file)
            file.close()
        except:
            print('Nie znaleziono kodu błędów errors.json')

    # pokazuje błąd na ekranie i zwraca kod błędu
    def __throwError(self, code: int):
        print(self.__errors[str(code)])
        return code

    # sprawdza poprawność parametrów, jeśli wszystko jest w porządku to zwraca 0, inaczej zwraca kod błędu <1, ...>
    def validate(self, parameters: Parameters):
        # sprawdzenie czy macierz A jest pusta
        if not parameters.A.size:
            return self.__throwError(1)

        # sprawdzenie czy macierz A jest dwuwymiarowa
        if parameters.A.ndim != 2:
            return self.__throwError(2)

         # sprawdzenie czy macierz A jest kwadratowa
        if parameters.A.shape[0] <= 1 or (parameters.A.shape[0] != parameters.A.shape[1]):
            return self.__throwError(3)

        # sprawdzenie czy wektor b jest pusty
        if not parameters.b.size:
            return self.__throwError(4)

        # sprawdzenie czy wektor b jest jednowymiarowy
        if parameters.b.ndim != 1:
            return self.__throwError(5)

        # sprawdzenie czy wektor b ma odpowiedni rozmiar
        if parameters.b.size != parameters.A.shape[0]:
            return self.__throwError(6)

        # sprawdzenie czy liczba max_iterations jest całkowita i dodatnia
        if not isinstance(parameters.max_iterations, int) or parameters.max_iterations <= 0:
            return self.__throwError(7)

        # sprawdzenie czy liczba tolerance jest różna od 0
        if parameters.tolerance == 0:
            return self.__throwError(8)

        # sprwadzenie czy x0 jest prawidłowe (jeśli podane)
        if parameters.x0 is not None:
            # sprawdzenie czy wektor  jest pusty
            if not parameters.x0.size:
                return self.__throwError(9)

            # sprawdzenie czy wektor b jest jednowymiarowy
            if parameters.x0.ndim != 1:
                return self.__throwError(10)

            # sprawdzenie czy wektor b ma odpowiedni rozmiar
            if parameters.x0.size != parameters.A.shape[0]:
                return self.__throwError(11)

        # sprawdzenie czy liczba w jest z zakresu (0, 2)
        if parameters.w is not None and (parameters.w <= 0.0 or parameters.w >= 2.0):
            return self.__throwError(12)

        return self._SUCCESS


# utworzenie walidatora
validator: Validator = Validator()
