# Błąd
# Autor: Łukasz Miłoś, 15.02.2021

# Error ułatwia powiązanie pomiędzy kodami błędów (użyteczne dla programistów) a opisami błędów (użyteczne dla użytkowników)

class Error:
    codes: list = []
    descriptions: list = []

    # konstruktor, wymagany obiekt errors z kodami i opisami błędów
    def __init__(self, errors: dict):
        self.__organize(errors)

    # funkcja organizująca błędy, tzn. dzieląca kody i opisy błędów
    def __organize(self, errors: dict):
        for code in errors:
            self.codes.append(code)
            self.descriptions.append(errors[code])
