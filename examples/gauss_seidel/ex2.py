from numpy import array
from ...src.gauss_seidel.method import gauss_seidel


# Parametry wejściowe:
A = array([[2, 3], [5, 7]])
b = array([11, 13])
max_iterations = 100
tolerance = 0.000001
x0 = array([1.1, 2.3])

# Przewidywane wyniki:
# Warunek konieczny zbieżnosci ciągu nie jest spełniony!


def gauss_seidel_example_2():
    print(
        "##### Metoda iteracyjna stacjonarna - Gauss-Seidel - Przyklad 2 #####"
    )
    x, i, t = gauss_seidel(A, b, max_iterations, tolerance)(
        A, b, max_iterations, tolerance
    )

    print(f"Rozwiazanie: {x}")
    print(f"Liczba wykonanych iteracji: {i}")
    print(f"Czas obliczen: {t}s")
