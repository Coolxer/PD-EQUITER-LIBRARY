# Jacobi
# Autor: Łukasz Miłoś, 15.02.2021

from .method import JacobiMethod
from .validator import errors, JacobiValidator

# Przygotowanie metody Jacobiego do pracy

# Utworzenie walidatora dla metody Jacobiego
validator: JacobiValidator = JacobiValidator(errors)

# Utworzenie obiektu metody jacobiego
jacobi: JacobiMethod = JacobiMethod(validator)
