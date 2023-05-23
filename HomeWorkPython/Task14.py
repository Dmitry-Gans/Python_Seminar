# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input("Введите степень для 2: "))
result = " "

for i in range(number):
    if 2** i < number:
        tmp = 2**i
        result = result + str(tmp) + ", "
        i += 1
print(f"{number} -> {result}")

# Эталонное решение:

# n = int(input())
# i = 0
# while 2 ** i <= n:
#     print(2 ** i)
#     i += 1