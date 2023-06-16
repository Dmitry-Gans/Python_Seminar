# Задача №51.
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.

# Ввод: Вывод:
# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# Вывод:
# same

values = [0, 2, 10, 6] 

# def same_by(function, objects):
#     if len(objects) == 0:
#         print ('Список пустой')
#     else:
#         list_1 = list(map(function, objects))
#         return max(list_1) == min(list_1)

def same_by(function, objects):
    return len(list(filter(function, objects))) == 0

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')