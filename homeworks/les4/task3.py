'''
3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор.
'''

numbers = [elem for elem in range(20, 241) if not elem % 20 or not elem % 21]

print(numbers)
