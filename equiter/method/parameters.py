# Parametry
# Autor: Łukasz Miłoś, 15.02.2021

# Klasa reprezentuje strukturę parametrów metod iteracyjnych

class Parameters:
    A: list = []
    b: list = []
    max_iterations: int = 0
    tolerance: float = 0.0
    x0: list = None

    def __init__(self, A, b, max_iterations, tolerance, x0=None):
        self.A = A
        self.b = b
        self.max_iterations = max_iterations
        self.tolerance = tolerance
        self.x0 = x0
