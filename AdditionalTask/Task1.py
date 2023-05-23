# Доп задание

# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]


number = [2, 3, 4, 5, 6]
i = 0
sum = 0
result = 0

for i in number:
    sum = number[0] * number[len(number) - 1]
    number[len(number) - 1] = number[len(number) - 1] - 1
    i = i + 1
    result = str(result) + str(sum)
print(result)
