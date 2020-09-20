'''
5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce


def multiply(a, b):
    return a * b


even_list = [num for num in range(100, 1001) if not num % 2]
print(reduce(multiply, even_list))
