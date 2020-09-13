'''
5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
'''
rating = [7, 5, 3, 3, 2]

while True:
    n = input("Введите новый элемент рейтинга\n")
    if n.isdigit():
        n = int(n)
        break
    else:
        print('Неверный ввод')

for i, elem in enumerate(rating):
    if n > elem:
        rating.insert(i, n)
        break
    elif i == len(rating) - 1:
        rating.append(n)
        break

print(rating)

# Второй способ решения
rating_second = [7, 5, 3, 3, 2]

rating_second.append(n)
rating_second.sort(reverse=True)
print(rating_second)
