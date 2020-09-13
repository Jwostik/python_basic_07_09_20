'''
3. Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
'''
while True:
    n = input("Введите номер месяца\n")
    if n.isdigit():
        n = int(n)
        break
    else:
        print('Неверный ввод')

season_name_list = ['зима', 'весна', 'лето', 'осень']
season_value_list = [[1, 2, 12], [3, 4, 5], [6, 7, 8], [9, 10, 11]]

for i, elem in enumerate(season_value_list):
    if n in elem:
        print(season_name_list[i])

season_dict = {'зима': [1, 2, 12], 'весна': [3, 4, 5], 'лето': [6, 7, 8], 'осень': [9, 10, 11]}

for elem in season_dict.items():
    if n in elem[1]:
        print(elem[0])
