import data_base as d
import UI as u
def BUTTON():
    d.db_creating()
    while True:
        family = u.main_menu()# пользователь в главном меню
        if family == 'q':
            break
        elif family == "1":
            format_export = u.export() # выгрузка справочника
            if format_export == 'r':
                print("Перехожу в другое меню...")
                continue
            elif format_export == "1":
                print("Печатаю телефонный справочник...")
                d.print_db()
                continue
            elif format_export == "2": 
                break
                #TODO
            else:
                print("Я вас не понимаю")
                continue
        elif family == '2':
            break
            #TODO
        else:
            family = u.check_name(family)
            name = input("Введите, пожалуйста, имя абонента: ")
            name = u.check_name(name)
            print(family)
            print(name)
            print("Ищу по базе...")
            d.db_fetch(family, name)
            break
            


            

