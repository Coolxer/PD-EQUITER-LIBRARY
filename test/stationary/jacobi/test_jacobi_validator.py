# Testy dla walidatora metody Jacobiego
# Autor: Łukasz Miłoś, 15.02.2021

import pytest
import numpy as np

from equiter.src.method.stationary.jacobi.validator import JacobiValidator, errors
from equiter.src.method.parameters import Parameters


class TestJacobiValidator:
    __validator: JacobiValidator

    def setup_class(self):
        self.__validator = JacobiValidator(errors)

    @pytest.mark.parametrize("A", [np.array([[]])])
    def test_validate_should_give_error_1_which_mean_empty_matrix(self, A):
        code = self.__validator.validate(Parameters(A, [], 0, 0, 0))
        assert code == 1

    @pytest.mark.parametrize("A", [np.array([1]), np.array([1, 2]), np.array([[[1], [2], [3]]])])
    def test_validate_should_give_error_2_which_mean_not_two_dimensional_matrix(self, A):
        code = self.__validator.validate(Parameters(A, [], 0, 0, 0))
        assert code == 2

    @ pytest.mark.parametrize("A", [np.array([[1]]), np.array([[1], [2]]), np.array([[1, 2, 3], [4, 5, 6]])])
    def test_validate_should_give_error_3_which_mean_no_square_matrix(self, A):
        code = self.__validator.validate(Parameters(A, [], 0, 0))
        assert code == 3

    @ pytest.mark.parametrize("b", [np.array([])])
    def test_validate_should_give_error_4_which_mean_empty_vector(self, b):
        code = self.__validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), b, 0, 0))
        assert code == 4

    @ pytest.mark.parametrize("b", [np.array([[1]]), np.array([[1], [2]]), np.array([[[1]]])])
    def test_validate_should_give_error_5_which_mean_vector_multi_dimensional(self, b):
        code = self.__validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), b, 0, 0))
        assert code == 5

    @ pytest.mark.parametrize("b", [np.array([1]), np.array([1, 2, 3])])
    def test_validate_should_give_error_6_which_mean_vector_invalid_dimension(self, b):
        code = self.__validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), b, 0, 0))
        assert code == 6

    @ pytest.mark.parametrize("k", [-3, -0.1, 0, 0.1, 5.5])
    def test_validate_should_give_error_7_which_mean_max_iterations_invalid_number(self, k):
        code = self.__validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), np.array([1, 2]), k, 0))
        assert code == 7

    @ pytest.mark.parametrize("tol", [0])
    def test_validate_should_give_error_6_which_mean_tolerance_is_0(self, tol):
        code = self.__validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), np.array([1, 2]), 50, tol))
        assert code == 8


# musze uzupelnic test dla wektora (rozmiar taki jak macierzy)
