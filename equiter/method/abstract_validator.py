# Walidator abstrakcyjny
# Autor: Łukasz Miłoś, 15.02.2021

import numpy as np
from .error import Error

"""
# AbstractValidator stanowi bazę (interfejs) dla wszystkich pozostałych walidatorów

# Pozwala ujednolicić strukturę wszystkich walidatorów do jednego schematu i sprawia, że wszystkie walidatory są spójne

# Każdy walidator
    - ma wejście (Input), czyli parametry i wyjście (Output), czyli wynik walidacji: udana lub kod błędu
    - zdefiniowane kody błędów (dla programisty), a także tekstową czytelną alternatywę (dla użytkownika)
"""


class AbstractValidator:
    __errors: Error = None

    # konstruktor
    def __init__(self, errors: Error):
        self.__errors = errors

    # funkcja sprawdzająca poprawność parametrów
    def validate(self, params: dict, showErrorCodes: bool = false):
        return 0
