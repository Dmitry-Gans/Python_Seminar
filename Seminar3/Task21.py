# Задача 21.
# Напигите программу для печати всех уникальных значений в словаре.

# Дано:
#  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}] 


# Итог:
# {'S005', 'S002', 'S007', 'S001', 'S009'}

list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] 
count = 0 # Счетчик перебора
new_list = [] # Пустой список
for i in list:
    dictionary = i # Передаем словарь по индексу в новую переменную
    for j in dictionary: # Перебираем полученный словарь
        dictionary[j] = dictionary[j].strip() # Удаляем лишние пробелы
        new_list.insert(count, dictionary[j]) # Заполняем пустой список
        count += 1
print(set(new_list))
