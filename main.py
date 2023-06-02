"""
username = input('Введите имя:')
if username == 'Маша':
    print('Ура, это Маша!')
elif username == 'Марина':
    print('Я так ждал вас, Марина')
elif username == 'Ильнар':
    print('Ильнар - ТОП')
else:
    print('Привет,', username)
"""
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# Пробуем импортировать модуль

import modul1
modul1.max1(5, 9)
print(modul1.max1(5, 9))

# Вызываем сразу функцию

from modul1 import max1 # Можно вместо max1 написать * - это значит, что импортируются все функции из файла
print(max1(5, 9))

# Можно так же переименовать файл в самой программе, но не сам файл,
# тем самым упростить ввод в будущем:

import modul1 as m1 # С помощью as задаем новое имя 
print(m1.max1(5, 9))