import sqlite3
from sqlite3 import Error
import UI as u

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
            phone = u.enter_phone()
            comment = u.enter_comment()
            c.execute('''INSERT INTO phones(user_id, phone, comment) 
            VALUES(?, ?, ?)''', (rows, phone, comment))
            db.commit()
        elif answer == '2':
            print("Какой номер телефона удалить?")
            old_value = u.enter_phone()
            try:
                c.execute('SELECT phone_id FROM phones WHERE phone = ?', (old_value,))
                print("На какой номер телефона поменять?")
                id = c.fetchone()
                new_value = u.enter_phone()           
                c.execute('UPDATE phones SET phone = ? WHERE id = ?', (new_value, id))
                db.commit()
                print("Исполненио")    
            except Error:
                print("Упс, что-то пошло не так...")    
        elif answer == '3':
            phone = u.enter_phone()
            try: 
                c.execute('''SELECT phone_id FRON phones WHERE 
                user_id = ? AND phone = ?''', (rows, phone))
                id = c.fetchall()
                c.execute('''DELETE FROM phones
                WHERE user_id = ?''', (id,))
                db.commit()
            except Error:
                print("Упс, что-то пошло не так...")
        elif answer == '4':
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
        temp = c.fetchone()
        phone = u.enter_phone()
        comment = u.enter_comment()
        c.execute('''INSERT INTO phones(user_id, phone, comment) 
        VALUES(?, ?, ?)''', (temp[0], phone, comment))
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


def import_list_of_tuples(data: list, path=path1):
    db = sqlite3.connect(path)
    c = db.cursor()
    c.execute('''Select id FROM users 
    WHERE last_name = ? AND first_name = ?''', data[0], data[1])
    row = c.fetchone()
    c.execute('''INSERT INTO phones(user_id, phone, comment)
    VALUES(?, ?, ?)''', (row[0], data[2], data[3]))
    rows = c.fetchone()
    print("Фамилия:", row[0][0])
    print("Имя:", row[0][1])
    print("Телефон:", row[0][2])
    print("Комментарий:", row[0][3])
    db.commit()
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
