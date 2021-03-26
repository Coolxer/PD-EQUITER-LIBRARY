import numpy as np
import matplotlib.pyplot as plt

# Klasa Visualizer służy do prezentacji danych macierzy w postaci wykresów


class Visualizer:
    @staticmethod
    def draw(matrix: np.array):
        plt.imshow(matrix)
        plt.colorbar()
        plt.show()
