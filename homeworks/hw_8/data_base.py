import sqlite3
from sqlite3 import Error
import UI as u
import datetime
now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
path1 = '.\homeworks\hw_7\phone_book.db'

def db_creating(path=path1):
        db = sqlite3.connect(path)
        c = db.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            last_name TEXT,
            first_name TEXT
            )""")
        c.execute("""CREATE TABLE IF NOT EXISTS phones(
            phone_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            phone TEXT,
            comment TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
            )""")
        db.commit()
        db.close()

def print_db(path=path1):
    db = sqlite3.connect(path)
    c = db.cursor()
    c.execute('''SELECT users.id, users.last_name, users.first_name,
    phones.phone, phones.comment FROM users, phones WHERE 
    users.id = phones.user_id''')
    rows = c.fetchall()
    u.print_array_of_tuples(rows)
    db.commit()
    db.close()

def db_fetch(value1, value2, path = path1):
    db = sqlite3.connect(path)
    c = db.cursor()
    try:
        c.execute('''SELECT users.id, users.last_name, users.first_name, phones.phone, phones.comment
        FROM users, phones WHERE phones.user_id=users.id AND last_name = ?
        AND first_name = ?''', (value1, value2))
        rows = c.fetchall()
        u.print_array_of_tuples(rows)
        if len(rows) > 1:
            rows = rows[0][0]
        answer = u.choice2_menu()
        if answer == '1':
            phone = input("Введите номер телефона: ")
            phone = u.check_phone(phone)
            comment = input("Введите комментарий: ")
            comment = u.check_comment(comment)
            c.execute('''INSERT INTO phones(user_id, phone, comment) 
            VALUES(?, ?, ?)''', (rows, phone, comment))
            db.commit()
        if answer == '2':
            print("Какой номер телефона удалить?")
            old_phone = input("Введите номер телефона: ")
            old_phone = u.check_phone(old_phone)
            try:
                c.execute('SELECT phone_id FROM phones WHERE phone = ?', (old_phone,))
                print("На какой номер телефона поменять?")
                new_phone = input("Введите номер телефона: ")
                new_phone = u.check_phone(new_phone)      
                c.execute('UPDATE phones SET phone = ? WHERE id = ?', (new_phone, c.fetchone()[0]))
                db.commit()
                print("Исполнено")    
            except Error:
                print("Упс, что-то пошло не так...")    
        if answer == '3':
            try: 
                phone = input("Введите номер телефона: ")
                phone = u.check_phone(phone)
                c.execute('''SELECT phone_id FRON phones WHERE 
                user_id = ? AND phone = ?''', (rows, phone))
                c.execute('''DELETE FROM phones
                WHERE user_id = ?''', c.fetchall())
                db.commit()
            except Error:
                print("Упс, что-то пошло не так...")
        if answer == '4':
            try:
                c.execute('''DELETE FROM phones 
                WHERE user_id = ?''', (rows,))
                db.commit()
                c.execute('''DELETE FROM users WHERE 
                id = ?''', (rows,))
                db.commit()
            except Error:
                print("Попытайтесь позже...")
        else:
            exit()
    except Error:
        c.execute('INSERT INTO users(last_name, first_name) VALUES(?, ?)', (value1, value2))
        db.commit()
        c.execute('''SELECT id from users
        WHERE last_name = ? AND first_name = ?''', (value1, value2))
        phone = input("Введите номер телефона: ")
        phone = u.check_phone(phone)
        comment = input("Введите комментарий: ")
        c.execute('''INSERT INTO phones(user_id, phone, comment) 
        VALUES(?, ?, ?)''', (c.fetchone()[0], phone, comment))
        db.commit()
        c.execute('''SELECT users.id, users.last_name, users.first_name, phones.phone, phones.comment
        FROM users, phones WHERE phones.user_id = users.id 
        AND last_name = ? AND first_name = ?''', (value1, value2))
        rows = c.fetchall()
        print("Вы ввели:\n")
        u.print_array_of_tuples(rows)
    finally:
        db.commit()
        db.close()

def db_fetch_all_tables(path= path1):
    db = sqlite3.connect(path)
    c = db.cursor()
    c.execute('SELECT name from sqlite_master where type= "table"')
    print(c.fetchall())

lst = [('Ширяев','Артём','98798798797','доброта'), ('Колкина','Милена','654654654','знающая'),('Бородатыый','Сергей','456987654','нужный')]

def import_list_of_tuples(data=lst, path=path1):
    db = sqlite3.connect(path)
    c = db.cursor()
    for i in range(len(data)):
        try:
            c.execute('''Select id FROM users 
            WHERE last_name = ? AND first_name = ?''', (data[i][0], data[i][1]))
            row = c.fetchone()
            c.execute('''INSERT INTO phones(user_id, phone, comment)
            VALUES(?, ?, ?)''', (row, data[i][2], data[i][3]))
            db.commit()
            c.execute('''SELECT users.id, users.last_name, users.first_name, phones.phone, phones.comment
            FROM users, phones WHERE phones.user_id = users.id 
            AND last_name = ? AND first_name = ?''', (data[i][0], data[i][1]))
            rows = c.fetchall()
            print("Вы ввели:\n")
            u.print_array_of_tuples(rows)
        except Error as e:
            print(e)
            print("И вот из-за этого всё и отвалилось...")
    db.close()


def print_table_db(path=path1):
    db = sqlite3.connect(path)
    c = db.cursor()
    c.execute('''SELECT * FROM users''')
    rows = c.fetchall()
    for row in rows:
        print(row)
    db.commit()
    db.close()
