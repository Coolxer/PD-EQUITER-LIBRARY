
import numpy as np
from tabulate import tabulate

# Klasa View jest klasą pomocniczą i umożliwia wyświetlanie macierzy i informacji o tej macierzy


class View:
    @staticmethod
    def showMatrixInformations(matrix: np.array):
        headers = ['Parametr', 'Wartosc']
        data = []

        # uzupełnianie tabeli poszczególnymi danymi
        data.append(['Liczba wszystkich elementow', matrix.size])
        data.append(['Liczba niezerowych elementow', np.count_nonzero(matrix)])
        data.append(['Liczba wierszy', matrix.shape[0]])
        data.append(['Liczba kolumn', matrix.shape[1]])
        data.append(['Typ elementow', matrix.dtype.name])

        # wyświetlenie nagłówka
        print('\n------- Szczegoly dotyczace macierzy -------')

        # wyświetlenie tabeli
        print(tabulate(data, headers=headers, tablefmt="grid"))

    @staticmethod
    def drawMatrix(matrix: np.array):
        for i in range(3):
            for j in range(3):
                print("{0:.4f}".format(matrix[i][j]), end="  ")
        print()
