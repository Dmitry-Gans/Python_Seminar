# Задача №39. 
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива

# Ввод:
# 7
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 
# (каждое число вводится с новой строки)

# Вывод: 3 3 2 12

n = 7
m = 6
list_1 = []
list_2 = []
k = 0
list_result = []
for i in range(n):
    list_1 = int(input("Заполните первый массив: "))
for i in range(m):
    list_2 = int(input("Заполните второй массив: "))
for i in list_1:
    for j in list_2:
        if i != j:
            list_result.inser(k, i)
            k += 1
print(list_result)

print(list_result)



