# Metoda abstrakcyjna
# Autor: Łukasz Miłoś, 15.02.2021

import time

from .abstract_validator import AbstractValidator
from .visualizer import Visualizer

"""
# KlasaAbstractMethod stanowi bazę (interfejs) dla wszystkich pozostałych metod

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

    # konstruktor, wymagany jest obiekt walidatora
    def __init__(self, validator: AbstractValidator):
        self.__validator = validator

    # wyszukiwanie rozwiązania konkretną metodą
    # wymagane są parametry dla danej metody
    # możliwa jest także wizualizacja danych wejściowych i wyników

    def __process(self, params: dict, visualize: bool = False):
        if not self.__checkout(params):
            return 'Błąd danych wejściowych. Patrz powyżej'

        # pobranie aktualnego czasu przed rozpoczęciem wykonywania metody
        start = time.time()

        # przygotowanie danych wejściowych do obliczeń (np. pobranie przekątnej, utworzenie wektora pomocniczego, itp.)
        self.__prepare()

        # poszukiwanie rozwiązań układu równań
        solution = self.__operation()

        # pobranie aktualnego czasu po zakończeniu obliczeń
        end = time.time()

        # obliczenie czasu trwania obliczeń
        executionTime = start - end

        # utworzenie obiektu wynikowego
        output = {"solution": solution, "time": executionTime}

        # opcjonalna wizualizacja danych
        if(visualize is True):
            self.__visualize(params['matrix'], output)

        # zwrócenie czasu i wektora wynikowego
        return output

    # sprawdzanie danych wejściowych (walidacja)
    def __checkout(self, params: dict):
        return self.__validator.validate(params)

    # przygotowanie danych do obliczeń, indywidualne dla każdej metody (przeciążane)
    def __prepare(self):
        pass

    # szukanie rozwiązania (iteracyjnie), indywidualne dla każdej metody (przeciążane)
    def __operation(self):
        return {}

    # wizualizacja danych wejściowych i wynikowych
    def __visualize(self, params: list, output: list):
        visualizer = Visualizer(params, output)
        visualizer.draw()
