# Informator danych
# Autor: Łukasz Miłoś, 15.02.2021

import numpy as np
from tabulate import tabulate

# DataInformer służy do prezentacji danych o macierzy
# Uzyskiwane informacje to:
#   - liczba wszystkich elementów
#   - liczba niezerowych elementów
#   - liczba wierszy
#   - liczba kolumn
#   - typ elementów


class DataInformer:
    # konstruktor z wymaganą macierzą
    def __init__(self, matrix):
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
