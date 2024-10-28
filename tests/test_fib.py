import lib
import pytest

class TestFibonacci:

    # Позитивный тест с корректными данными. Возвращает последовательность Фибоначчи
    def test_positive_fibonacci(self):
        assert lib.fibonacci(5).tolist() == [0, 1, 1, 2, 3]

    # Негативный тест с n <= 0. Если мы подаем на вход n <= 0, то программа с последовательностью Фибоначчи выдает ошибку
    # Вызывается исключение ValueError
    def test_negative_fibonacci(self):
        with pytest.raises(ValueError):
            lib.fibonacci(0)