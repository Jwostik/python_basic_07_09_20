'''
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию
и не завершиться с ошибкой.
'''


class ZeroDivisionErr(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    inp_data = input("Введите делимое и делитель через пробел: ")

    try:
        a, b = map(int, inp_data.split())
        if b == 0:
            raise ZeroDivisionErr("Деление на 0!")
        print(a / b)
    except ValueError:
        print("Неверный ввод!")
    except ZeroDivisionErr as err:
        print(err)
        continue
