'''
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
'''

int_var = 123
float_var = 123.123
str_var = '123asd'

print(int_var, float_var, str_var)

input_message = "Введите целое число"

print(input_message)
a1 = input()

a2 = input(input_message + "\n")

input_message = "Введите дробное число\n"
b = input(input_message)

input_message = "Введите строку\n"
с = input(input_message)

print('Целые числа:', a1 + ',', a2)

print('Дробное число:', b)

print('Строка', с)