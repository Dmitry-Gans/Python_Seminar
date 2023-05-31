# Задача 17:
# Дан список чисел. Определите, сколько в нем встречается разных чисел.

# [1, 1, 2, 0, -1, 3, 4, 4]

# Ответ: 6 

# Решение с помощью множества:
# a = [1, 1, 2, 0, -1, 3, 4, 4]
# a = set(a)
# print(len(a))

# Обычное решение через цикл

list = [1, 1, 2, 0, -1, 3, 4, 4]
list_result = []
for i in list:
    if i not in list_result: # not in - своеобразное не равно, если числа нет в списке, то добавлляем
        list_result.append(i)
print(len(list_result))


# Решение не пойми чего из чата 
# from random import randint # Иначе randint на 14 строчке будет не работать
# n = int(input("Введите размер массива: "))
# list = [randint(1, n) for i in range(n)]
# print(list)
# x = int(input("Введите число Х: "))

# diff = 0
# oldDiff = max(list)
# resultNum = 0
# for num in list:
#     diff  = x - num
#     if abs(diff) < abs(oldDiff):
#         resultNum = num
#     oldDiff = diff
# print(resultNum)