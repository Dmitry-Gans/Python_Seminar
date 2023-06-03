# Задача №31. Решение в группах
# Последовательностью Фибоначчи называется
# последовательность чисел
# a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

# n = 7
# def fibonaci(n):
#     if n in [0, 1]:
#         return 1
#     return fibonaci(n-1) + fibonaci(n -2) 

# print(fibonaci(n))

# Задача с полиндромом через рекурсию
# Один вариант

def pal(word):
    if len(word) == 0: return ''
    c = word.pop(0)
    return pal(word) + c


word = 'око'
text = [item for item in word]
if word == pal(text): print('Да')
else: print('Нет')
