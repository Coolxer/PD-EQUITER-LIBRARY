# Parametry
# Autor: Łukasz Miłoś, 15.02.2021

import numpy as np

# Klasa reprezentuje strukturę parametrów metod iteracyjnych


class Parameters:
    A: np.array = []
    b: np.array = []
    max_iterations: int = 0
    tolerance: float = 0.0
    x0: np.array = None

    def __init__(self, A: np.array, b: np.array, max_iterations, tolerance, x0: np.array = None):
        self.A = A
        self.b = b
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.x0 = x0
