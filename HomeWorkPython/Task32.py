# Задача 32: 
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
list_result = []
step = 0
min_number = int(input("Введите минимальное число: "))
max_number = int(input("Введите максимальное число: "))
for i in range(len(list)):
    if min_number <= list[i] <= max_number:
        list_result.insert(step, i)
        step += 1

print(list_result)

# Решение через рекурсию, не доделано 

# list=[-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# list_result = []
# step = 0
# min_number = 1
# max_number = 10
# def index(list, list_result, step, min_number, max_number):
#     for i in range(len(list)):
#         if min_number <= list[i] <= max_number:
#             list_result.insert(step, i)
#             step +=1
#             if step != len(list_result):
#                 return index(list, list_result, step +1, min_number, max_number)
#             else:
#                 print(list_result)
# index(list, list_result, step, min_number, max_number)
