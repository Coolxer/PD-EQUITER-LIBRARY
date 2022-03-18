# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik udostępnia najważniejsze elementy biblioteki do dyspozycji użytkownika końcowego

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import przybliżonych metod stacjonarnych rozwiązywania URL
from .src.jacobi.method import jacobi
from .src.gauss_seidel.method import gauss_seidel
from .src.sor.method import sor

# Import przykładów rozwiązań przy pomocy metody Jacobiego
from .examples.jacobi.ex1 import jacobi_example_1
from .examples.jacobi.ex2 import jacobi_example_2
from .examples.jacobi.ex3 import jacobi_example_3

# Import przykładów rozwiązań przy pomocy metody Gaussa-Seidela
from .examples.gauss_seidel.ex1 import gauss_seidel_example_1
from .examples.gauss_seidel.ex2 import gauss_seidel_example_2
from .examples.gauss_seidel.ex3 import gauss_seidel_example_3

# Import przykładów rozwiązań przy pomocy metody SOR
from .examples.sor.ex1 import sor_example_1
from .examples.sor.ex2 import sor_example_2
from .examples.sor.ex3 import sor_example_3
