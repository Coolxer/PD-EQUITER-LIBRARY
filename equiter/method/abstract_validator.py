# Walidator abstrakcyjny
# Autor: Łukasz Miłoś, 15.02.2021

import numpy as np
from .parameters import Parameters

"""
# AbstractValidator stanowi bazę (interfejs) dla wszystkich pozostałych walidatorów

# Pozwala ujednolicić strukturę wszystkich walidatorów do jednego schematu i sprawia, że wszystkie walidatory są spójne

# Każdy walidator
    - ma wejście (Input), czyli parametry i wyjście (Output), czyli wynik walidacji: udana lub kod błędu
    - zdefiniowane kody błędów (dla programisty), a także tekstową czytelną alternatywę (dla użytkownika)
"""


class AbstractValidator:
    _errors: dict = None
    _SUCCESS: bool = 0

    # konstruktor
    def __init__(self, errors: dict):
        self._errors = errors

    # przetwarza błąd, pokazuje go na ekranie i zwraca kod błędu
    def _error(self, code: int):
        print(self._errors[code])
        return code

    # sprawdza poprawność parametrów, jeśli wszystko jest w porządku to zwraca 0, inaczej zwraca kod błędu <1, ...>
    def validate(self, params: Parameters):
        return 0
