'''
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
'''


def user_data(name, surname, birthyear, city, email, phone):
    return f"имя: {name}, фамилия: {surname}, год рождения: {birthyear}, город проживания: {city}, " \
           f"email: {email}, телефон: {phone}"


try:
    user = input('Введите параметры, описывающих данные пользователя: '
                 'имя, фамилия, год рождения, город проживания, email, телефон.\n').split()

    if len(user) != 6:
        raise ValueError
    print(user_data(name=user[0], surname=user[1], birthyear=user[2], city=user[3], email=user[4], phone=user[5]))
except ValueError:
    print("Неверный ввод")
