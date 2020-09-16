'''
5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее
сумме и после этого завершить программу.
'''


def adder(current_sum, numbers):
    return current_sum + sum(numbers)


current_sum = 0
while True:
    numbers_str = input("Введите строку чисел, "
                        "разделенных пробелом, или символ % для выхода из программы.\n").split(' ')
    if '%' in numbers_str:
        numbers = [int(number) for i, number in enumerate(numbers_str) if i < numbers_str.index('%')]
        current_sum = adder(current_sum, numbers)
        print(current_sum)
        break
    else:
        numbers = [int(number) for number in numbers_str]
        current_sum = adder(current_sum, numbers)
        print(current_sum)
