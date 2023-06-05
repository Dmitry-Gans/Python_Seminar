# Задача No35.
# Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes

num = 5
def easy(num, div = None):
    if div is None:
        div = num -1
    while div >= 2:
        if num % div == 0:
            print("Число не простое")
            return False
        else:
            return easy(num, div - 1)
    else:
        print("Число является простым")
        return True
easy(num)

# Второй вариант:

# def checkPrime(n, div=2):
#     # div- дополнительный параметр для проверки на делимость. При вызове должен быть равен 2 т.к. первое простое число 2
#     if n < 2:  # если меьше то не простое
#         return False
#     elif n == 2:  # если два то сразу простое
#         return True
#     elif n % div == 0:  # если делится на 2 без остатка сразу выходим - не простое
#         return False
#     elif (
#         div * div > n
#     ):  # Проверка что делитель на меньше половины от числа т.к. все что больше половины будет остаток поэтому смысла дальше проверять нет
#         return checkPrime(n, div + 1)
#     else:
#         return True


# n = int(input("Введите число: "))
# if checkPrime(n):
#     print("Простое")
# else:
#     print("Не простое")