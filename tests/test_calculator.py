import lib
import pytest

class TestCalculator:

    # Функция возвращает данные для выполнения теста - корректное вычисление
    @pytest.fixture
    def correct_example(self):
        return 2, 4, '*'

    # Функция возвращает данные для выполнения теста - неправильный оператор
    @pytest.fixture
    def bad_operator_example(self):
        return 8, 4, ';'

    # Функция возвращает данные для выполнения теста - деление на ноль
    @pytest.fixture
    def divide_by_zero_example(self):
        return 12, 0, '/'

    # Позитивный тест с корректными данными. Возвращает результат вычисления
    def test_positive_calc(self, correct_example):
        assert lib.calculator(*correct_example) == 8

    # Негативный тест с неподходящим оператором. Вызывается исключение ValueError
    def test_bad_operator_calc(self, bad_operator_example):
        with pytest.raises(ValueError):
            lib.calculator(*bad_operator_example)

    # Негативный тест с делением на ноль. Вызывается исключение ZeroDivisionError
    def test_zero_divide_calc(self, divide_by_zero_example):
        with pytest.raises(ZeroDivisionError):
            lib.calculator(*divide_by_zero_example)