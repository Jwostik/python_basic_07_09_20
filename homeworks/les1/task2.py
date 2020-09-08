'''
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
'''
time = input("Введите время в секундах\n")

if time.isdigit():
    time = int(time)
    seconds = time % 60
    time //= 60
    minutes = time % 60
    hours = time // 60
    print('{:02}:{:02}:{:02}'.format(hours, minutes, seconds))
else:
    print("Неверный ввод")