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
    c.execute('''SELECT * FROM users, phones WHERE 
    users.id = phones.user_id''')
    rows = c.fetchall()
    for row in rows:
        print("id: ", row[0])
        print("Фамилия:", row[1])
        print("Имя:", row[2])
        print("id: ", row[3])
        print("id: ", row[4])
        print("Телефон:", row[5])
        print("Комментарий:", row[6], end = "\n\n")
    db.commit()
    db.close()

def db_fetch(value, path = path1):
    db = sqlite3.connect(path)
    c = db.cursor()
    try:
        temp = c.execute('SELECE * FROM users WHERE lasr_name = "{value}"').rowcount
        if temp == 1:
            c.execute('''SELECT users.last_name, users.first_name, phones.phone, phones.comment
            FROM users, phones WHERE phones.user_id=users.id AND last_name = "{value}"''')
            row = c.fetchone()
            print("Фамилия:", row[0][0])
            print("Имя:", row[0][1])
            print("Телефон:", row[0][2])
            print("Комментарий:", row[0][3])
            exit()
        else:
            name = u.choice_menu()
            if name == 'q':
                exit()
            else:
                name = u.check_name(name)
                print(name)
                c.execute('''SELECT users.last_name, users.first_name, phones.phone, phones.comment
                FROM users, phones WHERE phones.user_id = users.id AND last_name = "{value}" AND first_name = "{name}"''')
                rows = c.fetchall()
                for row in rows:
                    print("Фамилия:", row[0])
                    print("Имя:", row[1])
                    print("Телефон:", row[2])
                    print("Комментарий:", row[3], end = "\n\n")
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
        phone = u.enter_phone()
        comment = u.enter_comment()
        c.execute('''INSERT INTO phones(user_id, phone, comment) 
        VALUES(?, ?, ?)''', ('''Select id FROM users WHERE last_name = "{value}"
        AND first_name = "{name}"''', phone, comment))
        db.commit()
        c.execute('''SELECT users.last_name, users.first_name, phones.phone, phones.comment
        FROM users, phones WHERE phones.user_id = users.id AND last_name = "{value}" AND first_name = "{name}"''')
        rows = c.fetchall()
        for row in rows:
            print("Фамилия:", row[0])
            print("Имя:", row[1])
            print("Телефон:", row[2])
            print("Комментарий:", row[3], end = "\n\n")
    finally:
        db.commit()
        db.close()

def db_fetch_all_tables(path):
    db = sqlite3.connect(path)
    c = db.cursor()
    c.execute('SELECT name from sqlite_master where type= "table"')
    print(c.fetchall())

def import_list_of_tuples(data: list, path=path1):
    db = sqlite3.connect(path)
    c = db.cursor()
    c.execute('''INSERT INTO phones(user_id, phone, comment)
    VALUES(?, ?, ?)''', ('''Select id FROM users WHERE last_name = "{value}"
    AND first_name = "{name}"''', data[2], data[3]))
    row = c.fetchone()
    print("Фамилия:", row[0][0])
    print("Имя:", row[0][1])
    print("Телефон:", row[0][2])
    print("Комментарий:", row[0][3])
    db.commit()
    db.close()

