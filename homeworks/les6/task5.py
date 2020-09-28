'''
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
'''


class Stationery:
    def __init__(self):
        self.title = "Канцелярия"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def __init__(self):
        self.title = "Ручка"

    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def __init__(self):
        self.title = "Карандаш"

    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def __init__(self):
        self.title = "Маркер"

    def draw(self):
        print("Запуск отрисовки маркером")


print("Класс Stationery")
stationery = Stationery()
print(f"Элемент из класса: {type(stationery)}, название: {stationery.title}")
print("Метод draw:")
stationery.draw()

print("\nКласс Pen")
pen = Pen()
print(f"Элемент из класса: {type(pen)}, название: {pen.title}")
print("Метод draw:")
pen.draw()

print("\nКласс Pencil")
pencil = Pencil()
print(f"Элемент из класса: {type(pencil)}, название: {pencil.title}")
print("Метод draw:")
pencil.draw()

print("\nКласс Handle")
handle = Handle()
print(f"Элемент из класса: {type(handle)}, название: {handle.title}")
print("Метод draw:")
handle.draw()
