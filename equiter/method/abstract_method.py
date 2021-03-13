# Metoda abstrakcyjna
# Autor: Łukasz Miłoś, 15.02.2021

import time
import numpy as np

from .parameters import Parameters
from .abstract_validator import AbstractValidator
from .visualizer import Visualizer

"""
# AbstractMethod stanowi bazę (interfejs) dla wszystkich pozostałych metod

# Pozwala ujednolicić strukturę wszystkich metod do jednego schematu i sprawia, że wszystkie metody są spójne

# Każda metoda
    - ma wejście (Input), czyli parametry i wyjście (Output), czyli wynik (błąd lub rozwiązania)
    - zawiera walidator danych wejściowych dla jej poprawnego działania
    - ma mierzony czas działania (przygotowanie do obliczeń + same obliczenia, bez walidacji i bez wizualizacji)
    - możliwa jest także wizualizacja danych [opcjonalne]
    
# Dla przejrzystości i schematyczności wyróżniono 3 etapy wykonywania metody:
    - walidacja (checkout) - sprawdzanie danych wejściowych przy użyciu walidatora [UWAGA: kończy działanie metody w przypadku nieprawidłowych danych]
    - przygotowanie do obliczeń (prepare) - przygotowanie danych pomocniczych (np. pobranie przekątnej, utworzenie wektora pomocniczego) lub przekształcenie danych wejściowych
    - szukanie rozwiązania (operation) - faza zasadnicza, czyli poszukiwanie rozwiązań iteracyjnych (zazwyczaj przy użyciu jawnych pętli, bądź wielokrotnych operacji na macierzach z numpy)
    - wizualizacja (visualize)[opcjonalne] - przedstawienie danych wejściowych i wynikowych w postaci graficznej
"""


class AbstractMethod:
    __validator: AbstractValidator = None
    _params: Parameters

    # konstruktor, wymagany jest obiekt walidatora
    def __init__(self, validator: AbstractValidator):
        self.__validator = validator

    # wyszukiwanie rozwiązania konkretną metodą
    # wymagane są parametry dla danej metody
    # możliwa jest także wizualizacja danych wejściowych i wyników
    def process(self, method: str, params: Parameters, visualize):
        self._params = params

        print('\n####### METODA : ', method, ' #######')
        print('\n-> Walidacja danych wejsciowych')

        # walidacja danych wejściowych
        if self.__checkout():
            print('Metoda przerwala dzialanie. Blad danych wejsciowych. Patrz powyzej.')
            return

        # sprawdzenie wartunku zbieżności kolejnych rozwiązań
        if(not self.__checkConditionOfConvergence(params))
        return

        # pobranie aktualnego czasu przed rozpoczęciem wykonywania metody
        start = time.time()

        print('-> Przygotowywanie do obliczen')

        # przygotowanie danych wejściowych do obliczeń (np. pobranie przekątnej, utworzenie wektora pomocniczego, itp.)
        temp = self._prepare()

        print('-> Trwa poszukiwanie rozwiazania')

        # poszukiwanie rozwiązań układu równań
        iterations, solution = self._operation(temp)

        # pobranie aktualnego czasu po zakończeniu obliczeń
        end = time.time()

        # obliczenie czasu trwania obliczeń
        executionTime = start - end

        # opcjonalna wizualizacja danych
        if(visualize is True):
            self.__visualize(self._params.A, solution)

        print('\nCzas: ', executionTime)
        print('Liczba iteracji: ', iterations)
        print('Rozwiazanie: ', solution)
        print('\n#################################')

        # zwrócenie wyników
        return {'iterations': iterations, 'solution': solution, 'time': executionTime}

    # sprawdzanie danych wejściowych (walidacja)
    def __checkout(self):
        return self.__validator.validate(self._params)

    # przygotowanie danych do obliczeń, indywidualne dla każdej metody (przeciążane)
    def _prepare(self):
        return {}

    # sprawdzenie warunku zbieżności ciągu kolejnych przybliżeń rozwiązania
    def __checkConditionOfConvergence(self, params: Parameters):
        # obliczenie wartości absolutnych głównej przekątnej macierzy wejściowej A
        D_abs = np.diag(np.abs(params.A))

        # obliczenie sumy absolutnych wartości poszczególnych elementów wierszy z wyjątkiem elementu leżącego na głównej przekątnej
        S = np.sum(np.abs(params.A), axis=1) - D_abs

        # sprawdzenie czy macierz jest diagonalnie dominująca (wartość absolutna elementów głównej przekątnej musi być większa niż suma wartości absolutnych pozostałych elementów danego wiersza)
        if(np.all(D_abs < S)):
            print('Warunek konieczny zbieznosci ciagu nie jest spelniony')
            return False

        return True

     # szukanie rozwiązania (iteracyjnie), indywidualne dla każdej metody (przeciążane)
    def _operation(self, temp: dict):
        return 0, 0

    # wizualizacja danych wejściowych i wynikowych
    def __visualize(self, data: list, solution: list):
        visualizer = Visualizer(data, solution)
        visualizer.draw()
