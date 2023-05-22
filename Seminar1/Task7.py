# Задача №7.
# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.
# Input: 2016
# Output: YES

a = int(input("Введите год: "))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f"{a} год является високосным") 
else:
    print(f"{a} год не является високосным") 