# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik definicji metody sprawdzającej warunek zbieżności

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np


"""
    Wejście:
        - A (macierz => np.ndarray) - macierz główna układu równań
        
    Wyjście:
         - (bool) - True - gdy warunek zbieżności jest spełniony / False - gdy warunek zbieżności nie jest spełniony
"""

# Definicja metody sprawdzającej spełnienie warunku zbieżności
def check_condition_of_convergence(A: np.ndarray) -> bool:

    # Obliczenie  absolutnych wartości głównej przekątnej macierzy wejściowej A
    D_abs = np.abs(np.diag(A))

    # Obliczenie sumy absolutnych wartości poszczególnych elementów wierszy z wyjątkiem elementu leżącego na głównej przekątnej
    S = np.sum(np.abs(A), axis=1) - D_abs

    # Sprawdzenie czy macierz jest diagonalnie dominująca
    # (wartość absolutna elementu głównej przekątnej musi być większa niż suma wartości absolutnych pozostałych elementów danego wiersza)
    for i in range(np.shape(A)[0]):
        if np.abs(A[i][i]) <= S[i]:
            print("Warunek konieczny zbieżności ciągu nie jest spełniony")
            return False

    # Jeśli warunek jest spełniony to zwróć True
    return True
