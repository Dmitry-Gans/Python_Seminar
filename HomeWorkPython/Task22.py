# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

# Мое решение:

# n = int(input("Введите размер первого множества: "))
# m = int(input("Введите размер второго множества: "))
# list_1 = []
# list_2 = []
# list_result = []

# for i in range(n):
#     # i = int(input("Заполните первое множество: "))
#     # Чтобы упростить себе проверку и вам, сделал через рандом)))))
#     import random
#     i = random.randint(0, 15)
#     list_1.append(i)

# for i in range(m):
#     i = random.randint(0, 15)
#     list_2.append(i)

# for i in list_1:
#     for j in list_2:
#         if i == j:
#             list_result.append(i)
#             for k in range(len(list_result) - 1): # Запускаем сортировку пузырьком
#                 for l in range(len(list_result) - k - 1):
#                     if list_result[l] > list_result[l + 1]:
#                         tmp = list_result[l]
#                         list_result[l] = list_result[l + 1]
#                         list_result[l + 1] = tmp
#                         # Или так: list_result[l], list_result[l + 1] = list_result[l + 1], list_result[l]
# print(list_1)
# print(list_2)
# print(set(list_result))

# Пример преподавателя:

n = int(input("Введите количество элементов первого множества: "))
m = int(input("Введите количество элементов второго множества: "))
set1 = set()
set2 = set()

# Ввод элементов первого множества
print("Введите элементы первого множества:")
for i in range(n):
    num = int(input())
    set1.add(num)

# Ввод элементов второго множества
print("Введите элементы второго множества:")
for i in range(m):
    num = int(input())
    set2.add(num)

# Находим пересечение множеств
intersection = sorted(set1.intersection(set2))

# Выводим результат
print("Числа, встречающиеся в обоих множествах без повторений и в порядке возрастания:")
for num in intersection:
    print(num, end = ', ')