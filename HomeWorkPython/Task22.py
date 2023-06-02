# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n — кол-во элементов первого множества.
# m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input("Введите размер первого множества: "))
m = int(input("Введите размер второго множества: "))
list_1 = []
list_2 = []
list_result = []

for i in range(n):
    # i = int(input("Заполните первое множество: "))
    # Чтобы упростить себе проверку и вам, сделал через рандом)))))
    import random
    i = random.randint(0, 15)
    list_1.append(i)

for i in range(m):
    i = random.randint(0, 15)
    list_2.append(i)

for i in list_1:
    for j in list_2:
        if i == j:
            list_result.append(i)
            for k in range(len(list_result) - 1):
                for l in range(len(list_result) - k - 1):
                    if list_result[l] > list_result[l + 1]:
                        tmp = list_result[l]
                        list_result[l] = list_result[l + 1]
                        list_result[l + 1] = tmp
                        # Или так: list_result[l], list_result[l + 1] = list_result[l + 1], list_result[l]
print(list_1)
print(list_2)
print(set(list_result))