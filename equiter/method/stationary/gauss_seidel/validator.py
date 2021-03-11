# Walidator metody Jacobiego (iteracji prostej)

# Autor: Łukasz Miłoś, 15.02.2021

import numpy as np

'''
    Walidator sprawdza, czy dane wejściowe metody są prawidłowe.

    Wymagania Argumentów funkcji:
        - A (macierz)
            - macierz nie może być pusta
            - macierz musi być kwadratowa
            - na głównej przekątnej macierzy nie może być 0

        - b (wektor)
            - Wektor nie może być pusty


        - k (wartość całkowita) - maksymalna liczba iteracji, która determinuje koniec operacji
            * Wymagania
                - Liczba całkowita dodatnia

        - tol (double) - zadana dokladnosc (tolerancja), która determinuje koniec operacji
            * Wymagania
                - Liczba różna od 0

    Kod błędu:
                1a - Macierz A nie może być pusta!
                1b - Macierz A musi być kwadratowa!
                1c - Na głównej przekątnej macierzy nie może być 0!
                2a - Wektor b nie może być pusty!
                3a - Liczba k musi być całkowita dodatnia!
                4a - Liczba tol musi być różna od 0!
'''


def jacobi_validator(A, b, k, tol):
    # sprawdzenie czy macierz A nie jest pusta
    if (not A.size):
        print('Macierz A nie moze byc pusta!')
        return '1a'

    # sprawdzenie czy macierz A jest kwadratowa
    if(A.shape[0] != A.shape[1]):
        print('Macierz A musi byc kwadratowa!')
        return '1b'

    # sprawdzenie czy na głównej przekątnej macierzy A nie ma 0

    # pobranie głównej przekątnej macierzy A i zapisanie w postaci wektora
    diag = np.diag(A)
    for value in diag:
        if(value == 0):
            print('Na glownej przekatnej macierzy nie może byc 0!')
            return '1c'

    # sprawdzenie czy wektor b nie jest pusty
    if(not b.size):
        print('Wektor b nie może byc pusty!')
        return '2a'

    # sprawdzenie czy liczba k jest całkowita i dodatnia
    if(not isinstance(k, int) or k <= 0):
        print('Liczba k musi być calkowita dodatnia!')
        return '3a'

    # sprawdzenie czy liczba tol jest różna od 0
    if(tol == 0):
        print('Liczba tol musi być rozna od 0!')
        return '4a'

    return ''
