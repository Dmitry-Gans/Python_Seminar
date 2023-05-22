# Задача №9.
# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# Рещение с помощью функции 
# def factorial(number):
#     factorial = 1
#     while number > 1:
#         factorial = factorial * number
#         number = number - 1
#     print(factorial)
# factorial(5)

# Обычное решение 
print('Введите число N: ')

n = int(input())
fact = 1
if n < 0:
    print('Вы ввели отрицательное число. Введите неотрицательное: ')
    n = input()
    while n > 1:
        fact = fact * n
        n = n - 1
else:
    while n > 1:
        fact = fact*n
        n = n - 1
print(f'Факториал заданного числа: {fact}')
