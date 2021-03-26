import numpy as np

from equiter.src.method.parameters import Parameters

from equiter.src.method.stationary.jacobi.method import JacobiMethod

# Klasa Equiter stanowi podstawę działania biblioteki


class Equiter:
    @staticmethod
    def solve(method: str, parameters: Parameters, visualize: bool = False):
        if method == "jacobi":
            return JacobiMethod.process(method, parameters, visualize)
        elif method == "gauss_seidel":
            return
        elif method == "sor":
            return
