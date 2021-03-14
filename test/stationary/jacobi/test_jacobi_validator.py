# Testy dla walidatora metody Jacobiego
# Autor: Łukasz Miłoś, 15.02.2021

import pytest
import numpy as np

#from ....equiter.method.stationary.jacobi.validator import JacobiValidator, errors

import equiter.method.stationary.jacobi.validator.JacobiValidator
import equiter.method.stationary.jacobi.validator.errors

#from ....equiter.method.parameters import Parameters


class TestJacobiValidator:
    __validator: JacobiValidator

    def setup_class(self):
        self.__validator = JacobiValidator(errors)

    @pytest.mark.parametrize("A", np.array(0))
    def test_validate_should_give_error_1_which_mean_empty_matrix(self, A):
        code = self.__validator.validate(Parameters(A, 0, 0, 0, 0))
        assert code == 1


'''
    @pytest.mark.parametrize("A", np.array([1, 2, 3]))
    def test_validate_should_give_error_2_which_mean_no_square_matrix(self, A):
        self.__validator.validate(Parameters(A, 0, 0, 0, 0))
'''
