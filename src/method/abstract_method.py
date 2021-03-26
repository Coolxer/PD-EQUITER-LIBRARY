import time
import numpy as np

from equiter.src.method.parameters import Parameters
from equiter.src.method.validator import validator
from equiter.src.core.visualizer import Visualizer

"""
    Klasa AbstractMethod stanowi bazę (interfejs) dla wszystkich pozostałych metod

    Pozwala ujednolicić strukturę wszystkich metod do jednego schematu i sprawia, że wszystkie metody są spójne

    Każda metoda
        - ma wejście (Input), czyli parametry i wyjście (Output), czyli wynik (błąd lub rozwiązania)
        - zawiera walidator danych wejściowych dla jej poprawnego działania
        - ma mierzony czas działania (przygotowanie do obliczeń + same obliczenia, bez walidacji i bez wizualizacji)
        - możliwa jest także wizualizacja danych [opcjonalne]

    Dla przejrzystości i schematyczności wyróżniono 3 etapy wykonywania metody:
        - walidacja (checkout) - sprawdzanie danych wejściowych przy użyciu walidatora [UWAGA: kończy działanie metody w przypadku nieprawidłowych danych]
        - przygotowanie do obliczeń (prepare) - przygotowanie danych pomocniczych (np. pobranie przekątnej, utworzenie wektora pomocniczego) lub przekształcenie danych wejściowych
        - szukanie rozwiązania (operation) - faza zasadnicza, czyli poszukiwanie rozwiązań iteracyjnych (zazwyczaj przy użyciu jawnych pętli, bądź wielokrotnych operacji na macierzach z numpy)
        - wizualizacja (visualize)[opcjonalne] - przedstawienie danych wejściowych i wynikowych w postaci graficznej
"""


class AbstractMethod:
    # sprawdzenie warunku zbieżności ciągu kolejnych przybliżeń rozwiązania
    def __checkConditionOfConvergence(self, parameters: Parameters):
        # obliczenie wartości absolutnych głównej przekątnej macierzy wejściowej A
        D_abs = np.diag(np.abs(parameters.A))

        # obliczenie sumy absolutnych wartości poszczególnych elementów wierszy z wyjątkiem elementu leżącego na głównej przekątnej
        S = np.sum(np.abs(parameters.A), axis=1) - D_abs

        # sprawdzenie czy macierz jest diagonalnie dominująca (wartość absolutna elementów głównej przekątnej musi być większa niż suma wartości absolutnych pozostałych elementów danego wiersza)
        if(np.all(D_abs < S)):
            print('Warunek konieczny zbieżnosci ciągu nie jest spełniony')
            return False

        return True

    # przygotowanie danych do obliczeń, indywidualne dla każdej metody (przeciążane)
    def _prepare(self, parameters: Parameters):
        return {}

    # szukanie rozwiązania (iteracyjnie), indywidualne dla każdej metody (przeciążane)
    def _operation(self, parameters: Parameters, temp: dict):
        return 0, 0

    # wizualizacja danych wejściowych i wynikowych
    def __visualize(self, data: np.array, solution: np.array):
        Visualizer.draw(data)
        Visualizer.draw(solution)

    # wyszukiwanie rozwiązania konkretną metodą
    # wymagane są parametry dla danej metody
    # możliwa jest także wizualizacja danych wejściowych i wyników
    @staticmethod
    def process(self, method: str, parameters: Parameters, visualize: bool = False):

        print('\n####### METODA : ', method, ' #######')
        print('\n-> Walidacja danych wejściowych')

        # walidacja danych wejściowych
        if validator.validate(parameters):
            print('Metoda przerwała działanie. Błąd danych wejściowych. Patrz powyżej.')
            return

        # sprawdzenie warunku zbieżności kolejnych rozwiązań
        if not self.__checkConditionOfConvergence(parameters):
            return

        # pobranie aktualnego czasu przed rozpoczęciem wykonywania metody
        start = time.time()

        print('-> Przygotowywanie do obliczeń')

        # przygotowanie danych wejściowych do obliczeń (np. pobranie przekątnej, utworzenie wektora pomocniczego, itp.)
        temp = self._prepare(parameters)

        print('-> Trwa poszukiwanie rozwiązania')

        # poszukiwanie rozwiązań układu równań
        iterations, solution = self._operation(parameters, temp)

        # pobranie aktualnego czasu po zakończeniu obliczeń
        end = time.time()

        # obliczenie czasu trwania obliczeń
        executionTime = start - end

        # opcjonalna wizualizacja danych
        if(visualize is True):
            self.__visualize(parameters.A, solution)

        print('Czas: ', executionTime)
        print('Liczba iteracji: ', iterations)
        print('Rozwiązanie: ', solution)
        print('#################################')

        # zwrócenie wyników
        return {'iterations': iterations, 'solution': solution, 'time': executionTime}
