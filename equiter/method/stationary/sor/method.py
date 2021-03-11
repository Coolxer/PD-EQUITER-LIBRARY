# Metoda Jacobiego (iteracji prostej)
# Autor: Łukasz Miłoś, 15.02.2021

import numpy as np
import matplotlib as mpl

from .validator import jacobi_validator

'''
    Metoda pozwala na obliczenie kwadratowego układu n-równań z n-niewiadomymi przy maksymalnej liczbe iteracji z zadaną dokładnością.
    Oznacza to, że jeśli algorytm osiągnie wcześniej minimalną wymaganą dokładność, to przerwie swoje działanie przed wykonaniem k-operacji.
    Z drugiej strony algorytm przerwie swoje działanie po wykonaniu k-operacji, nawet jeśli nie osiągnie wymaganej dokładności.
    Algorytm sprawdza też warunek zbieżności ciągu kolejnych przybliżeń i w razie braku spełnienia warunku, kończy działanie.

    Im więcej iteracji tym rozwiązanie jest dokładniejsze.
    Nie należy jednak przesadzać z liczbą iteracji.
    Należy wybrać złoty środek pomiędzy czasem, a dokładnością obliczeń

    # Teoretyczny opis metody:
        Układ Ax = b

        Macierz wejściowa A układu przedstawiana jest jako:
        A = L + D + U

        gdzie:
            L - macierz dolna trójkątna
            D - macierz diagonalna
            U - macierz górna trójkątna

        Zatem układ wygląda następująco:
        (L + D + U)x = b

        Skąd
        Dx = -(L + U)x + b

        Jeśli  macierz D jest nieosobliwa(wyznacznik det(D) != 0)
        x = -D ^ (-1)(L + U)x + D ^ (-1)b

        Wzór iteracyjny dla metody Jacobiego w zapisie macierzowym
        x ^ (n+1) = -D ^ (-1)(L + U)x ^ n + D(-1)b

        Wzór iteracyjny dla metody Jacobiego w zapisie elementowym
        xi^(n + 1) = (1 / aii) * (bi - SUM(aij*xj^n, {j = 1,2...,n, j != i }))

        Warunek kończący wykonywanie iteracji(związany z dokładnością obliczeń)
        SUM(xi^(n + 1) - xi^n, {i = 1,2,...,n}) < tol
        ,gdzie tol - tolerancja, z góry zakładana dokładność

        Warunek konieczny zbieżności kolejnych przybliżeń
        ^iE{1,2...,n}|aii| > SUM(|aij|, {j={1,2...,n, j != i}})
'''

'''
    Wejście (Argumenty funkcji) [wymagania dla argumentów -> patrz: validator]:
        - A (macierz) - kwadratowa macierz układu równań
        - b (wektor)- wektor wartości po prawej stronie równiania Ax = b
        - x0 (wektor) [opcjonalne] - Początkowe przybliżenie niewiadomych układu
            - Jeśli argument nie zostao podane, to jako pierwsze przybliżenie x0 przyjmuje się wektor złożony z samych 0
        - k (liczba całkowita) - maksymalna liczba iteracji, która determinuje koniec operacji
        - tol (liczba zmiennoprzecinkowa, podwójnej precyzji) - zadana dokladnosc (tolerancja), która determinuje koniec operacji

    Wyjście (Wartości zwracane przez funkcję):
        a) w przypadku poprawnych danych wejściowych
            - x - otrzymany wektor rozwiązań
            - kn - iteracja po ktorej metoda osiagnela zadana dokladnosc

        b) w przypadku błędnych danych wejściowych funkcja przerwie swoje działanie i zwróci błąd -> (patrz: validator)
'''

'''
    Zamiast liczyć iteracyjnie, pisząc implementację w czystym pythonie, warto wykorzystać bibliotekę numpy,
    bo działa znacznie lepiej i szybciej i pozwala przyspieszyć obliczenia, co jest bardzo istotne w przypadku dużych układów
'''


def jacobi_method(A, b, k, tol, x0=None):

    # sprawdzenie argumentów funkcji przy użyciu walidatora
    incorrect = jacobi_validator(A, b, k, tol)

    # jeśli wystąpił jakiś błąd w danych wejściowych to funkcja przerywa działanie
    if(incorrect):
        return

    # pobranie wielkości macierzy wejściowej A
    size = np.shape(A)[0]

    # początkowe przybliżenie (wektor x0) nie jest wymagany
    # dlatego jeśli nie został on podany to zostaje utworzony wektor zerowy
    if(x0 is None):
        x = np.zeros(size)
    else:
        x = x0

    # pobranie przekątnej D wejściowej macierzy A
    D = np.diag(A)

    # obliczenie wartości absolutnych głównej przekątnej
    D_abs = np.abs(D)

    # obliczenie sumy absolutnych wartości poszczególnych elementów wierszy z wyjątkiem elementu leżącego na głównej przekątnej
    S = np.sum(np.abs(A), axis=1) - D_abs

    # sprawdzenie czy element głównej przekątnej jest większy niż suma pozostałych elementów
    # uwzględniane są wartości absolutne
    if(np.all(D_abs <= S)):
        print('Warunek konieczny zbieżności ciągu nie jest spełniony')
        return

    # wyznaczenie L + U na podstawie wzoru
    # A = L + D + U
    # A = D + (L + U)
    # (L + U) = A - D

    # obliczenie różnicy wejściowej macierzy A i macierzy D, która ma wszystkie elementy zerowe, za wyjątkiem przekątnej (macierz diagonalna), która jest pobrana z macierzy wejściowej A
    # to sprawia, że wynikowa macierz L_plus_U na przekątnej będzie miała same zera
    # wynikiem jest suma macierzy górno- U i dolno- trójkątnej L
    L_plus_U = A - np.diagflat(D)

    # Alternatywny sposób polega na wyznaczeniu osobno macierzy L i U bez znajomości macierzy D na tym etapie
    # L = np.tril(A, -1)
    # U = np.triu(A, 1)
    # L_plus_U = L + U

    # Ax = b

    # Przekształcenie wyjściowego wzoru
    '''
        A = L + D + U
        (L + D + U)x = b
        Lx + Dx + Ux = b
        Dx + (L + U)x = b       // - (L + U)x
        Dx = b - (L + U)x       // /D
        x = (b - (L + U)x) / D
    '''

    # pętla, która wykonuje się maksymalnie k-razy, chyba, że tolerancja zostanie wcześniej osiągnięta
    for i in range(k):
        # obliczenie kolejnego wektora przybliżenia rozwiązań
        x = (b - np.dot(L_plus_U, x)) / D

        # sprawdzenie czy została osiągnięta podana tolerancja
        if(sum(abs(np.dot(A, x) - b)) < tol):
            break

    # zwrocenie liczby wykonanych iteracji i wektora wynikowego
    return i, x
