import time
import matplotlib.pyplot as plt
import numpy

# W czasie zajęć będziemy szukać rozwiązania układu równań liniowych postaci:
# 3x1 + x2 − x3 = 6
# −x1 + 5x2 − x3 = 10   (30)
# 2x1 + 4x2 + 8x3 = 2

# Zadanie 1. Utwórz skrypt main.py, a w nim zdefiniuj zmienne A i b będące odpowiednio macierzą współczynników i wektorem wyrazów wolnych układu (30).
A = numpy.array([[3, 1, -1], [-1, 5, -1], [2, 4, 8]])
b = numpy.array([6, 10, 2])

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Zadanie 2. Rozwiąż powyższy układ równań przy pomocy poznanych metod biblioteki
# numpy (rozwiązaniem są liczby całkowite).
x = numpy.linalg.solve(A, b)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Zadanie 5. Dokonaj rozkładu macierzy A na macierze trójkątną dolną i górną.

L = numpy.tril(A)
U = numpy.triu(A)

# Zadanie 11. Napisz funkcję rozwiązującą URL przy pomocy metody Jacobiego (iteracji prostej)
# (rozdział 1.2.1 → wzory (24) albo (25). Jej deklaracja powinna wyglądać
# następująco:
# [xx, kk] = f_jacobi(A, b, k_max, tol)
# Uwaga: Ze względu na prostotę implementacji, zalecanym sposobem jest
# wykorzystanie wzoru (24) (dzięki czemu łatwo będzie można zmodyfikować
# funkcję celem implementacji kolejnych metod, por. wzory (26) i (28)).


def f_jacobi(A, b, k_max, tol):
    # sprawdzanie warunku zbieżności metody

    # obliczenie wartości absolutnych głównej przekątnej macierzy wejściowej A
    D_abs = numpy.diag(numpy.abs(A))

    # obliczenie sumy absolutnych wartości poszczególnych elementów wierszy z wyjątkiem elementu leżącego na głównej przekątnej
    S = numpy.sum(numpy.abs(A), axis=1) - D_abs

    # sprawdzenie czy macierz jest diagonalnie dominująca (wartość absolutna elementu głównej przekątnej musi być większa niż suma wartości absolutnych pozostałych elementów danego wiersza)
    for i in range(numpy.shape(A)[0]):
        if(numpy.abs(A[i][i]) <= S[i]):
            print('Warunek konieczny zbieżnosci ciągu nie jest spełniony')
            return

    # koniec sprawdzania warunku zbieżności

    # pobranie liczby wierszy macierzy
    size = numpy.shape(A)[0]

    # utworzenie początkowego wektora przybliżeń
    x = numpy.zeros(size)

    # wyznaczenie przekątnej macierzy A
    D = numpy.diag(A)

    # wyznaczenie odwrotności przekątnej macierzy
    D_inv = numpy.linalg.inv(numpy.diag(D))

    # wyznaczenie sumy macierzy dolno- i górno- trójkątnych
    L_plus_U = A - numpy.diag(D)

    # pętla, która wykonuje się maksymalnie max_iterations-razy, chyba, że tolerancja zostanie wcześniej osiągnięta
    for iteration in range(k_max):

        # zapisanie poprzedniego wektora przybliżeń
        x_old = x.copy()

        # obliczenie kolejnego wektora przybliżeń rozwiązania
        x = numpy.dot(D_inv, b - numpy.dot(L_plus_U, x_old))

        # sprawdzenie czy została osiągnięta podana tolerancja (warunek kończący)
        if sum(numpy.abs(x - x_old)) < tol:
            break

    # zwrocenie wektora wynikowego iliczby wykonanych iteracji
    return x, iteration

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Zadanie 12. Rozwiąż układ równań z zadania 1 przy pomocy funkcji f jacobi . Czy ten
# układ równań spełnia warunki zbieżności metody iteracji prostej? Podaj
# przykład takiego URL, dla którego metoda Jacobiego będzie rozbieżna.
# Sprawdź działanie swojej metody dla tego przykładu.


solution, iterations = f_jacobi(A, b, 10, 0.001)

# Odpowiedź: Tak, układ równań spełnia warunek zbieżności metody iteracji prostej.

# Próba rozwiązania innego układu, dla którego warunek zbieżności nie będzie spełniony
AA = numpy.array([[2, 3], [5, 7]])
bb = numpy.array([11, 13])

# Warunek konieczny zbieżnosci ciągu nie jest spełniony
solution, iterations = f_jacobi(AA, bb, 10, 0.001)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Zadanie 13. Napisz funkcję rozwiązującą URL przy pomocy metody Gaussa-Seidel’a
# (rozdział 1.2.2) → wzory (26) albo (27). Jej deklaracja powinna wyglądać następująco:
# def f_gauss_seidel(A, b, k max, tol)
# gdzie A – kwadratowa macierz współczynników, b – wektor wyrazów wolnych, k max - -maksymalna ilość iteracji, tol – żądana dokładność rozwiązania.
# Funkcja powinna zwracać wektor rozwiązań oraz liczbę wykonanych iteracji.


def f_gauss_seidel(A, b, k_max, tol):
    # sprawdzanie warunku zbieżności metody

    # obliczenie wartości absolutnych głównej przekątnej macierzy wejściowej A
    D_abs = numpy.diag(numpy.abs(A))

    # obliczenie sumy absolutnych wartości poszczególnych elementów wierszy z wyjątkiem elementu leżącego na głównej przekątnej
    S = numpy.sum(numpy.abs(A), axis=1) - D_abs

    # sprawdzenie czy macierz jest diagonalnie dominująca (wartość absolutna elementu głównej przekątnej musi być większa niż suma wartości absolutnych pozostałych elementów danego wiersza)
    for i in range(numpy.shape(A)[0]):
        if(numpy.abs(A[i][i]) <= S[i]):
            print('Warunek konieczny zbieżnosci ciągu nie jest spełniony')
            return

    # koniec sprawdzania warunku zbieżności

    # pobranie liczby wierszy macierzy
    size = numpy.shape(A)[0]

    # utworzenie początkowego wektora przybliżeń
    x = numpy.zeros(size)

    # wyznaczenie macierzy dolno-trójkątnej
    L = numpy.tril(A)

    # wyznaczenie macierzy U
    U = A - L

    # wyznaczenie sumy macierzy L i D
    L_plus_D = A - U

    # wyznaczenie odwrotności sumy macierzy L i D
    L_plus_D_inv = numpy.linalg.inv(L_plus_D)

    # pętla, która wykonuje się maksymalnie max_iterations-razy, chyba, że tolerancja zostanie wcześniej osiągnięta
    for iteration in range(k_max):

        # zapisanie poprzedniego wektora przybliżeń
        x_old = x.copy()

        # obliczenie kolejnego wektora przybliżeń rozwiązania
        x = numpy.dot(L_plus_D_inv, b - numpy.dot(U, x_old))

        # sprawdzenie czy została osiągnięta podana tolerancja (warunek kończący)
        if sum(np.abs(x - x_old)) < tol:
            break

    # zwrocenie liczby wykonanych iteracji i wektora wynikowego
    return x, iteration


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Zadanie 14. Rozwiąż układ równań z zadania 1 przy pomocy funkcji f_gauss_seidel.

solution, iterations = f_gauss_seidel(A, b, 10, 0.001)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Zadanie 15. Napisz funkcję rozwiązującą URL przy pomocy metody SOR (rozdział
# 1.2.3) → wzory (28) albo (29). Jej deklaracja powinna wyglądać następująco:
# def f sor(A, b, k max, tol, w)
# gdzie A – kwadratowa macierz współczynników, b – wektor wyrazów wolnych, k max – maksymalna ilość iteracji, tol – żądana dokładność rozwiązania, w – parametr nadrelaksacji.
# Funkcja powinna zwracać wektor rozwiązań oraz liczbę wykonanych iteracji.


def f_sor(A, b, k_max, tol, w):
    # sprawdzanie warunku zbieżności metody

    # obliczenie wartości absolutnych głównej przekątnej macierzy wejściowej A
    D_abs = numpy.diag(numpy.abs(A))

    # obliczenie sumy absolutnych wartości poszczególnych elementów wierszy z wyjątkiem elementu leżącego na głównej przekątnej
    S = numpy.sum(numpy.abs(A), axis=1) - D_abs

    # sprawdzenie czy macierz jest diagonalnie dominująca (wartość absolutna elementu głównej przekątnej musi być większa niż suma wartości absolutnych pozostałych elementów danego wiersza)
    for i in range(numpy.shape(A)[0]):
        if(numpy.abs(A[i][i]) <= S[i]):
            print('Warunek konieczny zbieżnosci ciągu nie jest spełniony')
            return

    # koniec sprawdzania warunku zbieżności

    # pobranie liczby wierszy macierzy
    size = numpy.shape(A)[0]

    # utworzenie początkowego wektora przybliżeń
    x = numpy.zeros(size)

    # pętla, która wykonuje się maksymalnie max_iterations-razy, chyba, że tolerancja zostanie wcześniej osiągnięta
    for iteration in range(k_max):

        # zapisanie poprzedniego wektora przybliżeń
        x_old = x.copy()

        # obliczenie kolejnego wektora przybliżeń rozwiązania
        for i in range(size):
            x[i] = (1-w)*x[i] + (w / A[i, i])*(b[i] - numpy.dot(A[i, :i],
                                                                x[:i]) - numpy.dot(A[i, (i+1):], x_old[(i+1):]))

        # sprawdzenie czy została osiągnięta podana tolerancja (warunek kończący)
        if sum(np.abs(x - x_old)) < tol:
            break

    # zwrocenie liczby wykonanych iteracji i wektora wynikowego
    return x, iteration

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Zadanie 16. Rozwiąż układ równań z zadania 1 przy pomocy funkcji f_sor .


solution, iterations = f_sor(A, b, 10, 0.001, 1.1)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Zadanie 17. Dobierz eksperymentalnie optymalną wartość parametru relaksacji w metodzie SOR dla układu równań (30).

# Podpowiedź: Wywołuj funkcję SOR dla różnych wartości parametru
# nadrelaksacji. Zapisanie liczby iteracji potrzebnych na uzyskanie zbieżności dla każdej wartości parametru nadrelaksacji pozwoli odczytać (przybliżoną) optymalną wartość z wykresu zależności
# liczby iteracji od wartości parametru nadrelaksacji.

w_values = [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]

iters = []

for i in range(len(w_values)):
    _, iterations = f_sor(A, b, 100, 0.001, w_values[i])

    iters.append(iterations)

plt.plot(w_values, iters)
plt.show()

# Odpowiedź: W tym przypadku najbardziej trafiona wartość współczynika nadrelaksacji (w) to 0.75,
# ponieważ dla tej wartości potrzebne było wykonanie najmniejszej ilości iteracji.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Zadanie 18. Porównaj zbieżność metod iteracyjnych stacjonarnych napisanych przez Ciebie (Jacobiego, Gaussa-Seidela, SOR) wykorzystanych do
# rozwiązania układu (30)

_, j_iterations = f_jacobi(A, b, 100, 0.001)

_, gs_iterations = f_gauss_seidel(A, b, 100, 0.001)

_, s_iterations = f_sor(A, b, 100, 0.001, 0.75)

# Porównanie liczby wykonanych iteracji
print("Liczba wykonanych iteracji: ")
print("--------------------------")
print("Metoda Jacobiego: ", j_iterations)
print("Metoda Gaussa-Seidela: ", gs_iterations)
print("Metoda SOR: ", s_iterations)

# Odpowiedź: Dla tego układu równań (30) i ustalonej dokładności (0.001) najszybciej zbieżna
# jest metoda SOR (7 iteracji).

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Zadanie 19. Porównaj szybkość działania poszczególnych metod iteracyjnych stacjonarnych.

startTime = time.time()

solution, iterations = f_jacobi(A, b, 1000, 0.000001)

print("Szybkość rozwiązania metodą Jacobiego: ", time.time() - startTime)

startTime = time.time()

solution, iterations = f_gauss_seidel(A, b, 1000, 0.000001)

print("Szybkość rozwiązania metodą Gaussa-Seidela: ", time.time() - startTime)

startTime = time.time()

solution, iterations = f_sor(A, b, 1000, 0.000001, 0.75)

print("Szybkość rozwiązania metodą SOR: ", time.time() - startTime)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
