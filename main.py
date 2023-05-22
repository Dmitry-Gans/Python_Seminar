"""
username = input('Введите имя:')
if username == 'Маша':
    print('Ура, это Маша!')
elif username == 'Марина':
    print('Я так ждал вас, Марина')
elif username == 'Ильнар':
    print('Ильнар - ТОП')
else:
    print('Привет,', username)
"""
line = ""
for i in range(5):
    line = ""
    for j in range(5):
        line += "*"
    print(line)