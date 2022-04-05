# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik przygotowujący kody i wiadomości błędów oraz zawierający
# definicję metody wypisującej wiadomość błędu i zwracającej kod dla tego błędu

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import os
import json

# ------------------------------------------------ Przygotowanie słownika błędów ------------------------------------------------ #

# Definicja słownika błędów i kodu braku błędu
errors = None
SUCCESS = 0

# Definicja katalogu i ścieżki pliku błędów
directory = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(directory, "errors.json")

# Wczytanie kodów i treści błędów z pliku errors.json
try:
    file = open(path)
    errors = json.load(file)
    file.close()
except:
    print("Nie znaleziono pliku błędów errors.json")
    exit()

# --------------------------------------------- Definicja metody wyświetlenia błędu -------------------------------------------- #

"""
    Wejście:
        - code (kod => int) - kod błędu
        
    Wyjście:
         - (int) - kod błędu

    Metoda ma jednakową wartość na wejściu i wyjściu, ale jej głównym celem jest wyświetlenie komunikatu błędu.
    Użycie tej metody pozwala znacznie skrócić kod metody walidującej.
"""

# Metoda wyświetla treść błędu na ekranie i zwraca jego kod
def throw_error(code: int) -> int:
    print(errors[str(code)])
    return code
