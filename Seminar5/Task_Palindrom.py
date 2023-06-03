# Задача с полиндромом через рекурсию
# Один вариант

word = "топот"

def palindrom(word):
    if len(word) < 1: # Выходи из рекурсии, в конечном итоге функция будет возвращать True, поэтому на 12 строчке именно с ним и сравниваем
        return True
    if word[0] == word[-1]: # Сравниваем первую букву и полседнюю
        return palindrom(word[1: -1]) # Передаем срез без первой и последней буквы, чтобы рекурсия не топталась на месте
       
if palindrom(word) == True: # Сверяем палиндром с True, так как palindrom(word) и есть True 
    print("Да")
else:
    print("Нет")

# Второй вариант
# def pal(word):
#     if len(word) == 0:
#         return ''
#     c = word.pop(0) # Удаляем первую букву
#     print(word)
#     print(pal(word) + c, end = ", ")
#     return pal(word) + c # И добавляем ее в конец
    

# text = [item for item in word] # Создаем новый список, содержащий все буквы слова "word"
# if word == pal(text): # Сравниваем, равно ли слово "word" слову "word"(перевернутое)
#     print('Да')
# else:
#     print('Нет')
