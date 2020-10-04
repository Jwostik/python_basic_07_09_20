'''
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода.
Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
'''


class Date:
    date_str = ''

    def __init__(self, date_str):
        self.date_str = date_str

    @classmethod
    def get_date(cls, date_str):
        cls.day, cls.month, cls.year = map(int, date_str.split('-'))
        print(f"День: {cls.day}, месяц: {cls.month}, год: {cls.year}.")

    @staticmethod
    def validate(day, month, year):
        if month not in range(1, 13):
            return False
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return True if day in range(1, 32) else False
        elif month == 2:
            if year % 4:
                return True if day in range(1, 29) else False
            else:
                return True if day in range(1, 30) else False
        else:
            return True if day in range(1, 31) else False


date = Date('1-2-2020')
date.get_date('1-2-2020')
print(date.validate(date.day, date.month, date.year))
