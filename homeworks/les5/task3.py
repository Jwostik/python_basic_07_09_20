'''
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
'''
try:
    with open("text.txt") as f:
        content = f.readlines()
        data = {}
        for elem in content:
            name, value = elem.split()
            value = int(value)
            data[name] = value
            if value < 20000:
                print(name)
        print(sum(data.values()) / len(data))
except IOError:
    print("Нет файла text.txt")
except ValueError:
    print("Неверные данные")
