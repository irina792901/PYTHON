import data_base as d
import UI as u
def BUTTON():
    d.db_creating()
    while True:
        family = u.main_menu()# пользователь в главном меню
        if family == 'q':
            break
        elif family == "2":
            format_export = u.export() # выгрузка справочника
            if format_export == 'q':
                print("Перехожу в другое меню...")
                continue
            if format_export == "1":
                print("Печатаю телефонный справочник...")
                d.print_db()
            else:
                break
                #TODO
        elif family == '3':
            break
            #TODO
        else:
            family = u.check_name(family)
            print(family)
            d.db_fetch(family)


            

