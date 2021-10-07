import numpy as np

"""
    Metoda sprawdzająca spełnienie warunku zbieżności ciągu kolejnych przybliżeń rozwiązania.
    Warunek jest spełniony jeśli macierz jest diagonalnie dominująca.
"""


def checkConditionOfConvergence(A: np.array):
    # obliczenie wartości absolutnych głównej przekątnej macierzy wejściowej A
    D_abs = np.abs(np.diag(A))

    # obliczenie sumy absolutnych wartości poszczególnych elementów wierszy z wyjątkiem elementu leżącego na głównej przekątnej
    S = np.sum(np.abs(A), axis=1) - D_abs

    # sprawdzenie czy macierz jest diagonalnie dominująca (wartość absolutna elementu głównej przekątnej musi być większa niż suma wartości absolutnych pozostałych elementów danego wiersza)
    for i in range(np.shape(A)[0]):
        if np.abs(A[i][i]) <= S[i]:
            print("Warunek konieczny zbieżnosci ciągu nie jest spełniony")
            return False

    return True
