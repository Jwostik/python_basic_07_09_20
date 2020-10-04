'''
7. Реализовать проект «Операции с комплексными числами».
Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
'''


class Complex:
    def __init__(self, re=0, im=0):
        if not isinstance(re, int) or not isinstance(im, int):
            raise ValueError("Неверный ввод")
        self.re = re
        self.im = im

    def __add__(self, other):
        if not isinstance(other, Complex):
            raise ValueError("Складываться должны комплексные числа")
        return Complex(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        if not isinstance(other, Complex):
            raise ValueError("Умножаться должны комплексные числа")
        return Complex(self.re * other.re - self.im * other.im, self.re * other.im + other.re * self.im)

    def __str__(self):
        if self.im < 0:
            return f"{self.re}-{abs(self.im)}i"
        return f"{self.re}+{abs(self.im)}i"


a = Complex(1, 2)
b = Complex(-2, -1)

print(a + b)
print(a * b)
print((1 + 2j) * (-2 - 1j))
