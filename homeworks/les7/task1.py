'''
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.

Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух
объектов класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.

Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
'''
from functools import reduce


class Matrix:
    def __init__(self, list_of_rows):
        if not isinstance(list_of_rows, list):
            raise ValueError("Неверный ввод")
        if not all([isinstance(row, list) for row in list_of_rows]):
            raise ValueError("Неверный ввод")
        if not reduce(lambda x, y: x == y, [len(row) for row in list_of_rows]):
            raise ValueError("Неверный ввод")
        self.list_of_rows = list_of_rows

    def __str__(self):
        return '\n'.join([''.join(['{:4}'.format(elem) for elem in row]) for row in self.list_of_rows])

    def __add__(self, other_matrix):
        if not isinstance(other_matrix, Matrix):
            raise ValueError("Складываются не матрицы")
        if len(self.list_of_rows) != len(other_matrix.list_of_rows):
            raise ValueError("Несоответстиве размеров матриц")
        if len(self.list_of_rows[0]) != len(other_matrix.list_of_rows[0]):
            raise ValueError("Несоответстиве размеров матриц")
        return Matrix([[first_elem + second_elem for first_elem, second_elem in zip(first_row, second_row)] for
                       first_row, second_row in zip(self.list_of_rows, other_matrix.list_of_rows)])


try:
    a = Matrix([[1, 2, 2], [1, 3, 2]])
    b = Matrix([[1, 2, 2], [1, 3, 2]])
    print(a + b)
except ValueError as ve:
    print(ve)
