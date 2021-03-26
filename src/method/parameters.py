import numpy as np

# Klasa Parameters reprezentuje strukturę parametrów metod iteracyjnych

"""
    Opisy poszczególnych parametrów:
        A - macierz wejściowa układu
        b - wektor danych
        max_iterations - maksymalna liczba iteracji
        x0 - początkowy wektor przybliżeń [opcjonalny]
        w - parametr relaksacji [opcjonalny] 
            [wymagany jedynie dla metody stacjonarnej SOR, jeśli nie podany to wynosi 1 => metoda Gaussa Seidla]
"""


class Parameters:
    A: np.array = []
    b: np.array = []
    max_iterations: int = 0
    tolerance: float = 0.0
    x0: np.array = None
    w: float = None

    def __init__(self, A: np.array, b: np.array, max_iterations, tolerance, x0: np.array = None, w: float = None):
        self.A = A
        self.b = b
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.x0 = x0
        self.w = w
