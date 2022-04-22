# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik definicji metody walidującej parametry wejściowe metod iteracyjnych

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from .error import throw_error, SUCCESS

"""
    Wejście(+ Wymagania Parametrów) :
        - A (macierz => np.ndarray)
            - musi być typu 'np.ndarray'
            - nie może być pusta
            - musi być dwuwymiarowa
            - musi być kwadratowa

        - b (wektor => np.ndarray)
            - musi być typu 'np.ndarray'
            - nie może być pusty
            - musi być jednowymiarowy
            - musi mieć rozmiar adekwatny do stopnia macierzy A

        - max_iterations (liczba całkowita => int)
            - musi być całkowite
            - musi być dodatnie

        - tolerance (liczba zmiennoprzecinkowa => float)
            - musi być zmiennoprzecinkowe
            - musi być większe od 0

        [opcjonalny => walidacja tylko w przypadku podania parametru]
        - x0 (wektor => np.ndarray)
            - musi być typu 'np.ndarray'
            - nie może być pusty
            - musi być jednowymiarowy
            - musi mieć rozmiar adekwatny do stopnia macierzy A

        [opcjonalny => walidacja tylko w przypadku podania parametru]
        - w (liczba zmiennoprzecinkowa => float)
            - musi być zmiennoprzecinkowe
            - musi być z zakresu (0, 2)

    Wyjście:
        - wynik walidacji:
            - 0 (SUCCESS) -> gdy walidacja przebiegła pomyślnie
            - <1, ...> -> gdy walidacja nie przebiegła pomyślnie
"""

# Metoda  sprawdza, czy dane wejściowe metod są prawidłowe.
# Jeśli dane wejściowe są prawidłowe to zwracane jest 0 (SUCCESS),
# w innym przypadku zwracany jest kod błędu <1...> (ERROR) wraz z czytelną informacją.
def validate_input_parameters(
    A: np.ndarray,
    b: np.ndarray,
    max_iterations: int,
    tolerance: float,
    x0: np.ndarray = None,
    w: float = None,
) -> int:

    # Sprawdzenie czy macierz 'A' jest typu np.ndarray
    if not isinstance(A, np.ndarray):
        return throw_error(1)

    # Sprawdzenie czy macierz 'A' jest pusta
    if not A.size:
        return throw_error(2)

    # Sprawdzenie czy macierz 'A' jest dwuwymiarowa
    if A.ndim != 2:
        return throw_error(3)

    # Sprawdzenie czy macierz A jest kwadratowa
    if A.shape[0] <= 1 or (A.shape[0] != A.shape[1]):
        return throw_error(4)

    # Sprawdzenie czy wektor 'b' jest typu 'np.ndarray'
    if not isinstance(b, np.ndarray):
        return throw_error(5)

    # Sprawdzenie czy wektor 'b' jest pusty
    if not b.size:
        return throw_error(6)

    # Sprawdzenie czy wektor 'b' jest jednowymiarowy
    if b.ndim != 1:
        return throw_error(7)

    # Sprawdzenie czy wektor 'b' ma odpowiedni rozmiar
    if b.size != A.shape[0]:
        return throw_error(8)

    # Sprawdzenie czy liczba 'max_iterations' jest typu 'int'
    if not isinstance(max_iterations, int):
        return throw_error(9)

    # Sprawdzenie czy liczba 'max_iterations' jest dodatnia
    if max_iterations <= 0:
        return throw_error(10)

    # Sprawdzenie czy liczba 'tolerance' jest typu 'float'
    if not isinstance(tolerance, float):
        return throw_error(11)

    # Sprawdzenie czy liczba 'tolerance' jest dodatnia
    if tolerance <= 0.0:
        return throw_error(12)

    # Sprawdzenie czy wektor 'x0' został podany
    if x0 is not None:

        # Sprawdzenie czy wektor 'x0' jest typu 'np.ndarray'
        if not isinstance(x0, np.ndarray):
            return throw_error(13)

        # Sprawdzenie czy wektor 'x0'  jest pusty
        if not x0.size:
            return throw_error(14)

        # Sprawdzenie czy wektor 'x0' jest jednowymiarowy
        if x0.ndim != 1:
            return throw_error(15)

        # Sprawdzenie czy wektor 'x0' ma odpowiedni rozmiar
        if x0.size != A.shape[0]:
            return throw_error(16)

    # Sprawdzenie czy liczba 'w' została podana
    if w is not None:

        # Sprawdzenie czy liczba w' 'jest typu 'float'
        if not isinstance(w, float):
            return throw_error(17)

        # Sprawdzenie czy liczba 'w' jest z zakresu (0, 2)
        if w < 0.0 or w > 2.0:
            return throw_error(18)

    return SUCCESS
