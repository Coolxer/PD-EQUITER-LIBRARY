# Solver
# Autor: Łukasz Miłoś, 15.02.2021


# This is fundamental solver of equiter library
# It resolving equations with given method
# It helps to get informations about Input and Output
# It handles time of operation and visualize data

from method.stationary.jacobi.method import jacobi_method


class Solver:
    def solve(self, method, params):
        if method == "jacobi":
            jacobi_method(params.A, params.b, params.k, params.tol, params.x0)
        elif method == "gauss_seidel":
            return
        elif method == "sor":
            return
