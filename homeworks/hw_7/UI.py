from cmath import phase
import re

def main_menu():
    print('-'*40)
    menu = '''Введите
    для поиска:           фамилию абонента 
    для просмотра справочника:           1
    для загрузки из другого справочника: 2'''
    print(menu)
    return input("Ввод: ")

def choice_menu():
    print('-'*60)
    menu = """Абонент не найден\n
    Введите 
    для добавления нового абонента:   введите его имя
    для выхода:                                     q"""
    print(menu)
    return input("Ввод: ")

def choice2_menu():
    print('-'*40)
    menu = """Введите
    для добавления номера телефона:     1
    для удаления номера телефона:       2
    для удаление абонента из базы:      3
    для возврата в предыдущее меню :    r
    для выхода:                         q"""
    print(menu)
    return input("Ввод: ")

def export():
    print('-'*40)
    menu = '''Введите
    для выгрузки справочника на экран:   1
    для выгрузки данных в файл:          2
    для выхода:                          q'''
    print(menu)
    return input("Ввод: ")

def format():
    print('-'*40)
    menu = """Введите
    для TXT:                        1
    для CVS:                        2
    для JSON:                       3
    для XML:                        4
    для HTML:                       5
    для выхода:                     q"""
    print(menu)
    return input("Ввод: ")

def check_name(name):
    while not name.isalpha:
        print("""      Error! 
        Можно вводить русские 
        или латинские буквы!""")
        name = input("Попоробуйте снова: ").lower().capitalize()
    return name

def enter_phone():
    phone = input("Введите номер телефона: ")
    while not phone.isdigit:
        print("""      Error! 
        Можно вводить только цифры.""")
    return phone

def enter_comment():
    comment = input ("Введите комментарий: ")
    return comment

def add_contact():
    name = input('Введите имя: ')
    firstname = input('Введите фамилию: ')
    phone = input('Введите номер телефона: ')
    directory = name + ' ' + firstname + '||' + phone + '\n'
    return directory


def find_contact(f):
        a = input('Введите данные для поиска: ')
        fnd = list(filter(lambda x: a in x, f.split('\n')))
        return fnd
