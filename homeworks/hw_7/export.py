import sqlite3
path1 = '.\homeworks\hw_7\phone_book.db'
def creating(file='Phonebook.csv', path=path1):# file='Phonebook.txt'
    db = sqlite3.connect(path)
    c = db.cursor()
    c.execute('''SELECT users.id, users.last_name, users.first_name,
    phones.phone, phones.comment FROM users, phones WHERE 
    users.id = phones.user_id''')
    rows = c.fetchall()
    file = file
    with open (file, 'a', encoding = 'utf-8') as data:
        for row in rows:
            data.write(convert_tuple(row))
    db.close()

def convert_tuple(c_tuple):
    str=''
    for i in c_tuple: 
        str=str+i 
    return str

 
