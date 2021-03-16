# Jacobi
# Autor: Łukasz Miłoś, 15.02.2021

from equiter.src.method.stationary.jacobi.method import JacobiMethod
from equiter.src.method.stationary.jacobi.validator import JacobiValidator, errors

# Przygotowanie metody Jacobiego do pracy

# Utworzenie walidatora dla metody Jacobiego
validator: JacobiValidator = JacobiValidator(errors)

# Utworzenie obiektu metody jacobiego
jacobi: JacobiMethod = JacobiMethod(validator)
