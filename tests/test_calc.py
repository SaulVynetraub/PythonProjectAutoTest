import pytest
from app.calculator import Calculator


class TestCalc:
    """Тестовый класс для проверки методов класса Calculator."""

    def setup(self):  # создание образца класса
        self.calc = Calculator

    def test_adding_success(self):  # позитивный, сумма
        assert self.calc.adding(self, 1, 2) == 3

    def test_adding_unsuccess(self):  # негативный, сумма
        assert self.calc.adding(self, 1, 2) == 4

    def test_multiply_correctly(self):  # позитивный, умножение
        assert self.calc.multiply(self, 2, 20) == 40

    def test_multiply_uncorrectly(self):  # негативный, умножение
        assert self.calc.multiply(self, 2, 20) == 50

    def test_division_pass(self):  # позитивный, деление
        assert self.calc.division(self, 20, 10) == 2

    def test_division_failed(self):  # негативный, деление
        assert self.calc.division(self, 20, 10) == 3

    def test_substraction_pass(self):  # позитивный, вычитание
        assert self.calc.subtraction(self, 15, 10) == 5

    def test_substraction_failed(self):  # негативный, вычитание
        assert self.calc.subtraction(self, 15, 10) == 10

    def test_zero_division(self):  # вызов исключения - деление на ноль
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self, 2, 0)

    def teardown(self):
        print('The end - teardown')
