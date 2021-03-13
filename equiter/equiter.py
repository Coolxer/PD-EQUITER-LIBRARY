# Equiter
# Autor: Łukasz Miłoś, 15.02.2021

import numpy as np

from .method.parameters import Parameters
from .method.stationary.jacobi.jacobi import jacobi

# To jest podstawa biblioteki Equiter
# Użytkownik na początku powinien utworzyć obiekt klasy Equiter
# Za pomocą obiektu klasy Equiter użytkownik może wykorzystywać wszystkie metody iteracyjne


class Equiter:
    __jacobi = None

    # constructor that prepares all methods
    def __init__(self):
        self.__jacobi = jacobi

    def solve(self, method: str, params: Parameters, visualize: bool = False):
        if method == "jacobi":
            return jacobi.process(method, params, visualize)
        elif method == "gauss_seidel":
            return
        elif method == "sor":
            return
