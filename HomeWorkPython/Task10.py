# Задача 10: На столе лежат n монеток.
# Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# 5 -> 10110
# 2

all_coins = int(input("Введите общее количество монет: "))
j = 0
for i in range(all_coins):
    v = int(input("Скажите какая сторона медали вам выпала: "))
    if v == 1:
        j += 1
    if j < all_coins/ 2:
        print(j)
    else:
        print(all_coins - j)

# Эталонный пример:

# n = int(input())
# count_zero = 0
# count_one = 0
# for i in range(n):
# x = int(input())
# if x == 0:
# count_zero += 1
# else:
# count_one += 1
# if count_one > count_zero:
# print(count_zero)
# else:
# print(count_one)

