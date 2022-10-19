def creating ():
    file = 'Phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'Фамилия;Имя;Номер телефона;Описание\n')

def writing_scv (info):
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')

def writing_txt(info):
    file = 'Phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')

def write_contact(b):
    with open ('directory.txt', 'a', encoding='utf-8') as f:
        f.write(b)

def read_contact():
    with open ('directory.txt', 'r', encoding='utf-8') as f:
        return f.read()

