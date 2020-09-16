'''
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
'''


def my_func(x, y, z):
    return x + y + z - min(x, y, z)


try:
    x = float(input("Введите первое число\n"))
    y = float(input("Введите второе число\n"))
    z = float(input("Введите третье число\n"))
    print(my_func(x, y, z))
except ValueError:
    print("Неверный ввод")
