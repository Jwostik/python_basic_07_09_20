'''
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
А также класс «Оргтехника», который будет базовым для классов-наследников.
Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов.
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием.
Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием.
Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
'''


class OfficeEquipment:
    name = ''
    cost = 0

    @classmethod
    def get_class_name(cls):
        return cls.__name__


class Printer(OfficeEquipment):
    is_color = False

    def __init__(self, name=OfficeEquipment.name, cost=OfficeEquipment.cost, is_color=is_color):
        if not isinstance(cost, int) or not isinstance(is_color, bool):
            raise ValueError("Неверный ввод")
        self.name = name
        self.cost = cost
        self.is_color = is_color


class Scanner(OfficeEquipment):
    scanning_speed = 1

    def __init__(self, name=OfficeEquipment.name, cost=OfficeEquipment.cost, scanning_speed=scanning_speed):
        if not isinstance(cost, int) or not isinstance(scanning_speed, int):
            raise ValueError("Неверный ввод")
        self.name = name
        self.cost = cost
        self.scanning_speed = scanning_speed


class Xerox(OfficeEquipment):
    length_width_height = [1, 1, 1]

    def __init__(self, name=OfficeEquipment.name, cost=OfficeEquipment.cost, length_width_height=length_width_height):
        if not isinstance(cost, int) or not isinstance(length_width_height, list):
            raise ValueError("Неверный ввод")
        if len(length_width_height) != 3:
            raise ValueError("Неверный ввод")
        self.name = name
        self.cost = cost
        self.length_width_height = length_width_height


class OfficeEquipmentStorage:
    name = ''
    stored_equipment = []
    stored_equipment_quantity = {'Printer': 0,
                                 'Scanner': 0,
                                 'Xerox': 0}

    def __init__(self, name=name, stored_equipment=stored_equipment,
                 stored_equipment_quantity=stored_equipment_quantity):
        self.name = name
        self.stored_equipment = stored_equipment
        self.stored_equipment_quantity = stored_equipment_quantity

    def get_equipment(self, equipment):
        if equipment.get_class_name() not in ['Printer', 'Scanner', 'Xerox']:
            raise ValueError("Склад предназначен только для оргтехники")
        self.stored_equipment.append(equipment)
        self.stored_equipment_quantity[equipment.get_class_name()] += 1

    def give_equipment(self, equipment):
        if equipment not in self.stored_equipment:
            raise ValueError("На складе нет такой оргтехники")
        self.stored_equipment.remove(equipment)
        self.stored_equipment_quantity[equipment.get_class_name()] -= 1
