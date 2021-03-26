# Testy dla walidatora metody Jacobiego
# Autor: Łukasz Miłoś, 15.02.2021

import pytest
import numpy as np

from equiter.src.method.validator import validator
from equiter.src.method.parameters import Parameters


class TestValidator:

    @pytest.mark.parametrize("A", [np.array([[]])])
    def test_validate_should_give_error_1_which_mean_empty_matrix(self, A):
        code = validator.validate(Parameters(A, [], 0, 0, 0))
        assert code == 1

    @pytest.mark.parametrize("A", [np.array([1]), np.array([1, 2]), np.array([[[1], [2], [3]]])])
    def test_validate_should_give_error_2_which_mean_not_two_dimensional_matrix(self, A):
        code = validator.validate(Parameters(A, [], 0, 0, 0))
        assert code == 2

    @ pytest.mark.parametrize("A", [np.array([[1]]), np.array([[1], [2]]), np.array([[1, 2, 3], [4, 5, 6]])])
    def test_validate_should_give_error_3_which_mean_no_square_matrix(self, A):
        code = validator.validate(Parameters(A, [], 0, 0))
        assert code == 3

    @ pytest.mark.parametrize("b", [np.array([])])
    def test_validate_should_give_error_4_which_mean_empty_vector(self, b):
        code = validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), b, 0, 0))
        assert code == 4

    @ pytest.mark.parametrize("b", [np.array([[1]]), np.array([[1], [2]]), np.array([[[1]]])])
    def test_validate_should_give_error_5_which_mean_vector_multi_dimensional(self, b):
        code = validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), b, 0, 0))
        assert code == 5

    @ pytest.mark.parametrize("b", [np.array([1]), np.array([1, 2, 3])])
    def test_validate_should_give_error_6_which_mean_vector_invalid_dimension(self, b):
        code = validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), b, 0, 0))
        assert code == 6

    @ pytest.mark.parametrize("max_iterations", [-3, -0.1, 0, 0.1, 5.5])
    def test_validate_should_give_error_7_which_mean_max_iterations_invalid_number(self, max_iterations):
        code = validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), np.array([1, 2]), max_iterations, 0))
        assert code == 7

    @ pytest.mark.parametrize("tolerance", [0])
    def test_validate_should_give_error_8_which_mean_tolerance_is_0(self, tolerance):
        code = validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), np.array([1, 2]), 50, tolerance))
        assert code == 8

    @ pytest.mark.parametrize("x0", [np.array([])])
    def test_validate_should_give_error_9_which_mean_empty_vector(self, x0):
        code = validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), np.array([1, 2]), 50, 0.0001, x0))
        assert code == 9

    @ pytest.mark.parametrize("x0", [np.array([[1]]), np.array([[1], [2]]), np.array([[[1]]])])
    def test_validate_should_give_error_10_which_mean_vector_multi_dimensional(self, x0):
        code = validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), np.array([1, 2]), 50, 0.0001, x0))
        assert code == 10

    @ pytest.mark.parametrize("x0", [np.array([1]), np.array([1, 2, 3])])
    def test_validate_should_give_error_11_which_mean_vector_invalid_dimension(self, x0):
        code = validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), np.array([1, 2]), 50, 0.0001, x0))
        assert code == 11

    @ pytest.mark.parametrize("w", [-1, 0, 2, 5])
    def test_validate_should_give_error_12_which_mean_w_is_not_in_range(self, w):
        code = validator.validate(Parameters(
            np.array([[1, 2], [3, 4]]), np.array([1, 2]), 50, 0.0001, None, w))
        assert code == 12
