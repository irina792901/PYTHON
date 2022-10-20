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

def update_db_table(db, position, new_value, user_iden):
    c = db.cursor()
    c.execute(f'UPDATE users SET {position} = "{new_value}" where user_id = {user_iden}')
    db.commit()
    db.close()

def print_db(path=path1):
    db = sqlite3.connect(path)
    c = db.cursor()
    c.execute('''SELECT users.id, users.last_name, users.first_name,
    phones.phone, phones.comment FROM users, phones WHERE 
    users.id = phones.user_id''')
    rows = c.fetchall()
    for row in rows:
        print("id: ", row[0])
        print("Фамилия:", row[1])
        print("Имя:", row[2])
        print("Телефон:", row[3])
        print("Комментарий:", row[4], end = "\n\n")
    db.commit()
    db.close()

def db_fetch(value, path = path1):
    db = sqlite3.connect(path)
    c = db.cursor()
    try:
        c.execute('''SELECT users.id, users.last_name, users.first_name, phones.phone, phones.comment
        FROM users, phones WHERE phones.user_id=users.id AND last_name = ?''', (value,))
        rows = c.fetchall()
        counter = len(rows)
        if counter == 1:
            u.print_array_of_tuples(rows)
        name = input("Введите имя абонента: ")
        name = u.check_name(name)
        try:
            c.execute('''SELECT users.id, users.last_name, users.first_name, phones.phone, phones.comment
            FROM users, phones WHERE phones.user_id=users.id AND last_name = ?
            AND first_name = ?''', (value, name))
            rows = c.fetchall()
            u.print_array_of_tuples(rows)
        except Error:
            name = u.check_name(name)
            print(name)
            c.execute('INSERT INTO users(last_name, first_name) VALUES(?, ?)', (value, name))
            db.commit()
            exit()
        answer = u.choice2_menu()
        if answer == '1':
            phone = u.enter_phone()
            comment = u.enter_comment()
            c.execute('''INSERT INTO phones(user_id, phone, comment) 
            VALUES(?, ?, ?)''', (rows[0], phone, comment))
            db.commit()
        elif answer == '2':
            c.execute('''DELETE FROM users AND phones  
            WHERE users.id = phones.user_id = ?''', (rows[0]))
            db.commit()
        else:
            exit()
    except Error:
        name = u.choice_menu()
        if name == 'q':
            exit()
        else:
            name = u.check_name(name)
            print(name)
            c.execute('INSERT INTO users(last_name, first_name) VALUES(?, ?)', (value, name))
            db.commit()
            c.execute('''SELECT id from users
            WHERE last_name = ? AND first_name = ?''', (value, name))
            temp = c.fetchone()
            phone = u.enter_phone()
            comment = u.enter_comment()
            c.execute('''INSERT INTO phones(user_id, phone, comment) 
            VALUES(?, ?, ?)''', (temp[0], phone, comment))
            db.commit()
            c.execute('''SELECT users.last_name, users.first_name, phones.phone, phones.comment
            FROM users, phones WHERE phones.user_id = users.id 
            AND last_name = ? AND first_name = ?''', (value, name))
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
