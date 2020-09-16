'''
1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
'''


def division(x, y):
    if y:
        print(f"Результат через условный оператор: {x}/{y}={x / y}")
    else:
        print(f"Ошибка: деление на 0.")


def division_try(x, y):
    try:
        print(f"Результат через try: {x}/{y}={x / y}")
    except ZeroDivisionError:
        print(f"Ошибка: деление на 0.")


try:
    x = float(input("Введите первое число\n"))
    y = float(input("Введите второе число\n"))
    division(x, y)
    division_try(x, y)
except ValueError:
    print("Неверный ввод")
