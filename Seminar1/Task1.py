# Вводится два числа, определить какое из них больше

a = int(input("Введите число a "))
b = int(input("Введите число b "))

if a > b:
    print(f"{a} > {b}")
elif a < b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")
    