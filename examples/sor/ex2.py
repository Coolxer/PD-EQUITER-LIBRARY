from numpy import array
from ...src.sor.method import sor


# Parametry wejściowe:
A = array([[4, -1, 0], [-1, 4, -1], [0, -1, 4]])
b = array([2, 6, 2])
max_iterations = 3
tolerance = 0.0001
w = 1.2

# Rozwiązanie układu:
# x = [1.0000, 2.0000, 1.0000]

# Przewidywane wyniki:
# x0: [0.0000, 0.0000, 0.0000]
# x1: [0.6000, 1.9800, 1.1940]
# x2: [1.0740, 2.0844, 0.9865]
# x3: [1.0105, 1.9822, 0.9974]
# ...
# x13: [1.0000, 2.0000, 1.0000]


def sor_example_2():
    print("##### Metoda iteracyjna stacjonarna - SOR - Przyklad 2 #####")
    x, i, t = sor(A, b, max_iterations, tolerance, w)

    print(f"Rozwiazanie: {x}")
    print(f"Liczba wykonanych iteracji: {i}")
    print(f"Czas obliczen: {t}s")
