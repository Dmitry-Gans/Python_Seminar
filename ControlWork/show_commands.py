import Note

def menu():
    print('\nЭто программа "Заметки", имеются следующие функции:\n\n1 - Показать весь список заметок\n2 - Создать заметку\n3 - Удаленить заметку\n4 - Редактировать заметку\n5 - Фильтрация заметок по дате\n6 - Показать заметку по id\n7 - Выход\n\nВведите номер функции: ')

def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите текст: ')
    else:
        return text
    
def create_note(number):
    title = check_len_text_input(input ('Введите название заметки: '), number)
    body = check_len_text_input(input('Введите описание заметки:'), number)
    return Note.Note(title = title, body = body)