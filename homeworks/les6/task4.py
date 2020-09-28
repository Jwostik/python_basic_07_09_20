'''
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self, speed, color, name):
        try:
            self.speed = int(speed)
            self.color = color
            self.name = name
            self.is_police = False
        except ValueError:
            print("Неверный ввод")

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость равна {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Скорость превышена")
        else:
            print(f"Текущая скорость равна {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Скорость превышена")
        else:
            print(f"Текущая скорость равна {self.speed}")


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        try:
            self.speed = int(speed)
            self.color = color
            self.name = name
            self.is_police = True
        except ValueError:
            print("Неверный ввод")


print("Класс Car")
car = Car(20, 'красный', 'VW')
print(
    f"Элемент из класса: {type(car)}, cкорость: {car.speed}, цвет: {car.color}, имя: {car.name}, полицейская: {car.is_police}")
print("Метод go:")
car.go()
print("Метод stop:")
car.stop()
print("Метод turn с параметором \'назад\':")
car.turn('назад')
print("Метод show_speed:")
car.show_speed()

print("\nКласс TownCar")
car = TownCar(50, 'синий', 'Audi')
print(
    f"Элемент из класса: {type(car)}, cкорость: {car.speed}, цвет: {car.color}, имя: {car.name}, полицейская: {car.is_police}")
print("Метод go:")
car.go()
print("Метод stop:")
car.stop()
print("Метод turn с параметором \'направо\':")
car.turn('направо')
print("Метод show_speed:")
car.show_speed()
car = TownCar(70, 'синий', 'Audi')
print(f"Метод show_speed для машины со скоростью {car.speed}:")
car.show_speed()

print("\nКласс WorkCar")
car = WorkCar(30, 'зеленый', 'BMW')
print(
    f"Элемент из класса: {type(car)}, cкорость: {car.speed}, цвет: {car.color}, имя: {car.name}, полицейская: {car.is_police}")
print("Метод go:")
car.go()
print("Метод stop:")
car.stop()
print("Метод turn с параметором \'налево\':")
car.turn('налево')
print("Метод show_speed:")
car.show_speed()
car = WorkCar(50, 'зеленый', 'BMW')
print(f"Метод show_speed для машины со скоростью {car.speed}:")
car.show_speed()

print("\nКласс PoliceCar")
car = PoliceCar(10, 'белый', 'Bugatti')
print(
    f"Элемент из класса: {type(car)}, cкорость: {car.speed}, цвет: {car.color}, имя: {car.name}, полицейская: {car.is_police}")
print("Метод go:")
car.go()
print("Метод stop:")
car.stop()
print("Метод turn с параметором \'с полицейским разворотом\':")
car.turn('с полицейским разворотом')
print("Метод show_speed:")
car.show_speed()
car = PoliceCar(200, 'белый', 'Bugatti')
print(f"Метод show_speed для машины со скоростью {car.speed}:")
car.show_speed()
