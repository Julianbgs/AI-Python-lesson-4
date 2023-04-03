"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
def print_question(description):
    result = input(description)
    return result
year_poet = 'Ввведите год рождения А.С.Пушкина:'
year = print_question(year_poet)
while year != '1799':
    print("Не верно")
    year = print_question(year_poet)
birthday_poet = 'Ввведите день рождения Пушкина?'
day = print_question(birthday_poet)
while day != '6':
    print("Не верно")
    day = print_question(birthday_poet + ' Это в июне.')
print('Верно')
