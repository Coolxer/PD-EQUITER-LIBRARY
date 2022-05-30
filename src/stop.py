# Autor: Łukasz Miłoś
# Data: 2021 - 2022

# Plik definicji metody sprawdzającej warunek stopu

# -------------------------------------------------------------------------------------------------------------------------------------------------- #

# Import zależności
import numpy as np
from numpy.linalg import norm

"""
    Wejście:
        - A (macierz => np.ndarray) - macierz główna układu równań
        - b (wektor => np.ndarray) - wektor wyrazów wolnych
        - x (wektor => np.ndarray) - przybliżony wektor rozwiązań
        - tolerance (liczba zmiennoprzecinkowa => float) - zadana dokładność
        
    Wyjście:
         - (bool) - True - gdy warunek stopu jest spełniony / False - w przeciwnym wypadku
"""

# Definicja metody sprawdzającej spełnienie warunku stopu
def check_stop_condition(A: np.ndarray, b: np.ndarray, x: np.ndarray, tolerance: float) -> bool:
    return (norm(np.dot(A, x) - b) / norm(b)) < tolerance
