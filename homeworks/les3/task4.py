'''
4. Программа принимает действительное положительное число x и целое отрицательное число y.
Необходимо выполнить возведение числа x в степень y.
Задание необходимо реализовать в виде функции my_func(x, y).
При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
'''


def my_func_operation(x, y):
    try:
        return x ** y
    except ZeroDivisionError:
        raise ZeroDivisionError


def my_func_cycle(x, y):
    try:
        res = 1 / x
        for _ in range(abs(y) - 1):
            res *= 1 / x
        return res
    except ZeroDivisionError:
        raise ZeroDivisionError


try:
    x = float(input("Введите действительное положительное число\n"))
    y = int(input("Введите целое отрицательное число число\n"))
    if y >= 0:
        raise ValueError
    print(f'Результат через оператор **: {my_func_operation(x, y)}')
    print(f'Результат через цикл: {my_func_cycle(x, y)}')
except ValueError:
    print("Неверный ввод")
except ZeroDivisionError:
    print("0 не может быть возведен в отрицательную степень")
