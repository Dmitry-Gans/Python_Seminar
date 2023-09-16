import commands as com
import show_commands

def run():
    input_from_user = ''
    while input_from_user != 7:
        show_commands.menu()
        input_from_user = input().strip()
        if input_from_user == '1':
            com.show('all')
        if input_from_user == '2':
            com.add()
        if input_from_user == '3':
            com.show('all')
            com.id_edit_del_show('del')
        if input_from_user == '4':
            com.show('all')
            com.id_edit_del_show('edit')
        if input_from_user == '5':
            com.show('date')
        if input_from_user == '6':
            com.show('id')
            com.id_edit_del_show('show')
        if input_from_user == '7':
            break