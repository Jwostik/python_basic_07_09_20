'''
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
'''
n = input("Введите целое положительное число n\n")

if n.isdigit():
    n = int(n)
    max = 0
    while n:
        if n % 10 > max:
            max = n % 10
        n //= 10
    print(max)
else:
    print("Неверный ввод")