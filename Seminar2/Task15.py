# Задача №15.
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

min = 0
max = 0
size = 6

init = True

print("Введите 6-ть элементов")
for i in range(size):
    n = int(input())
    if init:
        min = max = n
        init = False
    elif min > n:
        min = n
    elif max < n:
        max = n
print(f"Арбуз теще {min}кг, арбуз себе {max}кг")