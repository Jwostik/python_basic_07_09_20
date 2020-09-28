'''
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и
дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
'''


class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        try:
            self._income["wage"] = int(wage)
            self._income["bonus"] = int(bonus)
        except ValueError:
            print("Неверный ввод")

    def get_full_name(self):
        return f"Имя: {self.name}, Фамилия: {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


str = input("Введите имя, фамилию, должность, оклад и премию через пробел\n").split()
man = Position(str[0], str[1], str[2], str[3], str[4])

print(man.get_full_name())
print(man.get_total_income())
