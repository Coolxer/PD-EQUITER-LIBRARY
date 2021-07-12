import numpy as np

# Zadanie 1. Utwórz skrypt main.m i stwórz zmienne A i b
A = np.array([[3, 1, -1], [-1, 5, -1], [2, 4, 8]])
b = np.array([6, 10, 2])

# --------------------------------------------------------------------

# Zadanie 2. Rozwiąż powyższy układ równań (Ax = b)
x = np.linalg.solve(A, b)

# --------------------------------------------------------------------

# Zadanie 3. Napisz funkcję f gauss na podstawie przedstawionego algorytmu (wzory
# 9,9), która będzie implementacją metody eliminacji Gaussa bez wyboru
# elementu podstawowego

# --------------------------------------------------------------------

# Zadanie 4. Wywołaj napisaną przez siebie funkcję f gauss na rzecz zmiennych A, b.
# Sprawdź poprawność funkcji porównując jej wynik z rozwiązaniem otrzymanym w zad. 2.

# x, Ar = f_gauss(A, b)

# --------------------------------------------------------------------

# Zadanie 5. Dokonaj rozkładu macierzy A na macierze trójkątną dolną i górną przy
# pomocy funkcji języka python i biblioteki numpy

L = np.tril(A)
U = np.triu(A)

# --------------------------------------------------------------------

# Zadanie 6. Zaimplementuj rozkład LU przy pomocy metody Gaussa-Doolittle’a bez
# wyboru elementu podstawowego (wzór 18). Wywołanie funkcji powinno
# wyglądać następująco:

# --------------------------------------------------------------------

# Zadanie 7. Sprawdź poprawność zaimplementowanej przez siebie funkcji porównując
# jej wynik z rezultatem wywołania funkcji lu.

# L, U = f_gauss_doolittle(A)

# --------------------------------------------------------------------

# Zadanie 8. Napisz funkcję rozwiązującą URL przy pomocy metody iteracji prostej
# (wzory 20-22). Jej deklaracja powinna wyglądać:
# [xx, kk] = f jacobi(A,b, k max, tol)
# gdzie A – kwadratowa macierz współczynników, b – wektor wyrazów wolnych, k max - maksymalna ilość iteracji, tol – żądana dokładność rozwiązania. xx – wektor szukanych (rozwiązanie URL), kk – numer iteracji na
# której zakończono obliczenia.

# --------------------------------------------------------------------

# Zadanie 9. Napisz funkcję f gauss jordan na podstawie algorytmu przedstawionego
# w rozdziale (1.2). Postać jej wywołania to:
# [x] = f gauss jordan(A,b)
# gdzie A - kwadratowa macierz współczynników, b - wektor wyrazów wolnych, x - wektor szukanych (rozwiązanie URL)

# --------------------------------------------------------------------

# Zadanie 10. (Dla zaawansowanych) Przepisz funkcje f gauss, f gauss jordan oraz
# f jacobi, tak aby obliczenia wykonywać na całych wierszach (operator :),
# a nie na każdym elemencie wiersza z osobna.

# --------------------------------------------------------------------

# Zadanie 11. (Dla zaawansowanych) Spróbuj rozwiązać za pomocą napisanej przez siebie funkcji f gauss układ równań liniowych.

# A = np.array([[1, 1, 2], [1, 1, 1], [-2, 1, 3]])
# b = np.array([1, 2, -3])
# x, Ar = f_gauss(A, b)

# --------------------------------------------------------------------
