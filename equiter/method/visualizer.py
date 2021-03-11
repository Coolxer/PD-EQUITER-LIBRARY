# Wizualizator
# Autor: Łukasz Miłoś, 15.02.2021

import matplotlib.pyplot as plt

# Visualizer służy do prezentacji danych wejściowych (macierzy) i wyjściowych (wektora rozwiązań) metody  w postaci wykresów


class Visualizer:
    __data: list = []
    __solution: list = []

    # konstruktor
    def __init__(self, data, solution):
        self.__data = data
        self.__solution = solution

    def draw(self):
        self.__showColorizedPlot(self.__data)
        self.__showColorizedPlot(self.__solution)

    def __showColorizedPlot(self, matrix: list):
        plt.imshow(matrix)
        plt.colorbar()
        plt.show()
