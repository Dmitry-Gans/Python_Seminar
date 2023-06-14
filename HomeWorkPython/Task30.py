# Задача 30:
# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии:

# an = a1 + (n-1) * d

# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

def progress(a1, d, n, i, list):
    c = a1 + i * d
    list.insert(i, c) # Добавляем каждое значение на свое место
    # Увеличиваем счетчик отвечаеющий за местоположение элемента
    if i < n - 1: # Если счетчик не равен размеру массива, то функция вызывает 
    # саму себя и увеличивает счетчик отвечаеющий за местоположение 
    # элемента в списке
        return progress(a1, d, n, i + 1, list)
    return list

a1 = 7
d = 2
n = 5
i = 0 # Счетчик местонахождения в списке
list = []
progress(a1, d, n, i, list)
print(list)

