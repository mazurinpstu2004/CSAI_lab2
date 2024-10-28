import lib
import pytest

class TestBubbleSort:

    # Позитивный тест с корректными данными. Возвращает отсортированный массив
    def test_positive_bubble_sort(self):
        assert lib.bubble_sort([1, 9, 5, 3]) == [1, 3, 5, 9]

    # Негативный тест с пустым массивом. Вызывается исключение ValueErrorм
    def test_negative_bubble_sort(self):
        with pytest.raises(ValueError):
            lib.bubble_sort([])