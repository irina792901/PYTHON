import data_base as d
import UI as u
import export as e
def BUTTON():
    d.db_creating()
    while True:
        family = u.main_menu()# пользователь в главном меню
        if family == 'q':
            break
        elif family == "1":
            format_export = u.export() # меню выгрузки справочника
            if format_export == 'r':
                print("Перехожу в другое меню...")
                continue
            elif format_export == "1":
                print("Печатаю телефонный справочник...")
                d.print_db()
                continue
            elif format_export == "2":
                file = u.format()
                if file == "1":# в txt
                    e.creating(file = 'Phonebook.txt')
                elif file == '2':# csv
                    e.creating()
                elif file == '3':# json
                    break # TODO
                elif file == '4':# xml
                    break # TODO
                elif file == '5':# html
                    break # TODO
                else:
                    break
            else:
                print("Я вас не понимаю")
                continue
        elif family == '2':
            d.import_list_of_tuples()
        else:
            family = u.check_name(family)
            name = input("Введите, пожалуйста, имя абонента: ")
            name = u.check_name(name)
            print(family)
            print(name)
            print("Ищу по базе...")
            d.db_fetch(family, name)
            continue
            
            


            

