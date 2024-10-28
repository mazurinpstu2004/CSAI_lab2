import numpy as np

# Функция определения чисел Фибоначчи
# Принимает n чисел
# Возвращает список последовательности Фибоначчи = n
# Пример: n = 10 => [0 1 1 2 3 5 8 13 21 34]
def fibonacci(n):
    if n <= 0:
        raise ValueError("need n > 0")
    fib_arr = np.zeros(n)
    fib_arr[1] = 1
    for i in range(2, n):
        fib_arr[i] = fib_arr[i - 2] + fib_arr[i - 1]
    return fib_arr

# Функция сортировки массива Пузырьком
# Принимает массив чисел
# Возвращает отсортированный массив
# Пример: [3 2 1 2] => [1 2 2 3]
def bubble_sort(array):
    if len(array) <= 0:
        raise ValueError("Null array")
    if len(array) <= 0:
        raise
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    return array

# Функция - калькулятор
# Принимает 2 числа и оператор
# Возвращает результат расчета
# Пример: 1, 2, '+' => 3
def calculator(numb1, numb2, operator):
    result = 0
    if operator == '+':
        result = numb1 + numb2
    elif operator == '-':
        result = numb1 - numb2
    elif operator == '*':
        result = numb1 * numb2
    elif operator == '/':
        if numb2 == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        result = numb1 / numb2
    else:
        raise ValueError("Invalid operator" , operator)
    return result
