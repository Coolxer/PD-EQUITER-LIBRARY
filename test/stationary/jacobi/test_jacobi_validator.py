# Testy dla walidatora metody Jacobiego
# Autor: Łukasz Miłoś, 15.02.2021

from equiter.method.stationary.jacobi.validator import JacobiValidator


class TestJacobiValidator:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert x is 'hello'
