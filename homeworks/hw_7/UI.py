from cmath import phase
import re

def main_menu():
    print('-'*40)
    menu = '''Введите
    для поиска:           фамилию абонента
    для просмотра справочника:           1
    для загрузки из другого справочника: 2
    для выхода:                          q'''
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
    для изменения номера телефона:      2
    для удаления номерoв телефона:      3
    для удаление абонента из базы:      4
    для выхода:        любую другую цифру"""
    print(menu)
    return input("Ввод: ")

def export():
    print('-'*40)
    menu = '''Введите
    для выгрузки справочника на экран:   1
    для выгрузки данных в файл:          2
    для перехода в предыдущее менюf:     r'''
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
        name = input("Попоробуйте снова: ")
    name = name.lower()
    name = name.capitalize()
    return name

def enter_phone():
    phone = input("Введите номер телефона: ")
    while not phone.isdigit:
        print("""      Error! 
        Можно вводить только цифры.""")
        phone = input("Введите номер телефона: ")
    return phone

def enter_comment():
    comment = input ("Введите комментарий: ")
    return comment

def print_array_of_tuples(array):
    for tuple in array:
        print("id: ", tuple[0])
        print("Фамилия:", tuple[1])
        print("Имя:", tuple[2])
        print("Телефон:", tuple[3])
        print("Комментарий:", tuple[4], end = "\n\n")