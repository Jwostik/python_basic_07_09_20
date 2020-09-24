'''
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''

with open("text.txt", "w") as f:
    f.write(input("Введите набор чисел, разделенных пробелами\n"))

try:
    with open("text.txt") as f:
        nums = map(int, f.read().split())
        print(sum(nums))
except IOError:
    print("Нет файла text.txt")
except ValueError:
    print("Неверные данные")
