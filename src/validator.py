# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik walidatora danych wejściowych

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

"""
    Walidator sprawdza, czy dane wejściowe metod są prawidłowe.
    Jeśli dane wejściowe są prawidłowe to zwracane jest 0 (SUCCESS), w innym przypadku zwracany jest kod błędu <1...> (ERROR) wraz z czytelną informacją.

    Wymagania Parametrów:
        - A (macierz => np.array)
            - nie może być pusta
            - musi być dwuwymiarowa
            - musi być kwadratowa

        - b (wektor => np.array)
            - nie może być pusty
            - musi być jednowymiarowy
            - musi mieć rozmiar adekwatny do rozmiaru macierzy A

        - max_iterations (liczba całkowita => int)
            - liczba całkowita dodatnia

        - tolerance (liczba zmiennoprzecinkowa => float)
            - liczba zmiennoprzecinkowa większa od 0

        [opcjonalny => walidacja tylko w przypadku podania parametru]
        - x0 (wektor => np.array)
            - nie może być pusty
            - musi być jednowymiarowy
            - musi mieć rozmiar adekwatny do rozmiaru macierzy A

        [opcjonalny => walidacja tylko w przypadku podania parametru]
        - w (liczba zmiennoprzecinkowa => float)
            - liczba z zakresu (0, 2)
"""

# Import zależności
import os
import json
import numpy as np

# Klasa walidatora
class Validator:
    __errors: dict = None
    SUCCESS: bool = 0

    # Konstruktor przygotowujący kody i opisy błędów
    def __init__(self) -> None:
        directory = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(directory, "errors.json")

        # Wczytanie kodów i treści błędów z pliku errors.json.
        try:
            file = open(path)
            self.__errors = json.load(file)
            file.close()
        except:
            print("Nie znaleziono pliku błędów errors.json")

    # Metoda wyświetla treść błędu na ekranie i zwraca jego kod
    def __throw_error(self, code: int) -> int:
        print(self.__errors[str(code)])
        return code

    # Metoda sprawdza poprawność parametrów, jeśli wszystko jest w porządku to zwraca SUCCESS (0), inaczej zwraca kod błędu <1, ...>
    def validate(
        self,
        A: np.array,
        b: np.array,
        max_iterations: int,
        tolerance: float,
        x0: np.array = None,
        w: float = None,
    ) -> int:
        # Sprawdzenie czy macierz A jest pusta
        if not A.size:
            return self.__throw_error(1)

        # Sprawdzenie czy macierz A jest dwuwymiarowa
        if A.ndim != 2:
            return self.__throw_error(2)

        # Sprawdzenie czy macierz A jest kwadratowa
        if A.shape[0] <= 1 or (A.shape[0] != A.shape[1]):
            return self.__throw_error(3)

        # Sprawdzenie czy wektor b jest pusty
        if not b.size:
            return self.__throw_error(4)

        # Sprawdzenie czy wektor b jest jednowymiarowy
        if b.ndim != 1:
            return self.__throw_error(5)

        # Sprawdzenie czy wektor b ma rozmiar adekwatny do rozmiaru macierzy A
        if b.size != A.shape[0]:
            return self.__throw_error(6)

        # Sprawdzenie czy liczba max_iterations jest całkowita i dodatnia
        if not isinstance(max_iterations, int) or max_iterations <= 0:
            return self.__throw_error(7)

        # Sprawdzenie czy liczba tolerance jest dodatnia
        if tolerance <= 0.0:
            return self.__throw_error(8)

        # Sprawdzenie czy wektor x0 został podany
        if x0 is not None:
            # Sprawdzenie czy wektor x0  jest pusty
            if not x0.size:
                return self.__throw_error(9)

            # Sprawdzenie czy wektor x0 jest jednowymiarowy
            if x0.ndim != 1:
                return self.__throw_error(10)

            # Sprawdzenie czy wektor x0 ma odpowiedni rozmiar
            if x0.size != A.shape[0]:
                return self.__throw_error(11)

        # Sprawdzenie czy liczba w jest z zakresu (0, 2)
        if w is not None and (w < 0.0 or w > 2.0):
            return self.__throw_error(12)

        return self.SUCCESS


# Utworzenie obiektu walidatora
validator: Validator = Validator()
