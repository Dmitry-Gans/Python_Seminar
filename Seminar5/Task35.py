# Задача No35.
# Решение в группах
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes

num = 6
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