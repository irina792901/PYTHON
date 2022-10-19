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
    c.execute('''SELECT uers.last_name, users.first_name, phones.phone
    FROM users, phones WHERE phones.user_id=users.id''')
    print([row for row in c.fetchall()])
    db.commit()
    db.close()
 
def db_fetch(value, path = path1):
    db = sqlite3.connect(path)
    c = db.cursor()
    try:
        c.execute(f'SELECT id FROM users WHERE last_name = {value}')
    except Error:
        name = u.choice_menu()
        if name == 'q':
            exit()
        else:
            name = u.check_name(name)
        c.execute('INSERT INTO users(last_name, first_name) VALUES(?, ?)', (value, name))
        db.commit()
        phone = u.enter_phone()
        comment = u.enter_comment()
        c.execute('''INSERT INTO phones(user_id, phone, comment) 
        VALUES(?, ?, ?)''', ("Select users.id FROM users WHERE last_name = {value} AND first_name = {name}", phone, comment))
        db.commit()
        c.execute('''SELECT users.last_name, users.first_name, phones.phone
        FROM users, phones WHERE phones.user_id = users.id''')
        print(list(c.fetchone()))
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
    c.executemany("INSERT INTO users VALUES(?, ?)", (data[0], data[1]))
    db.commit()
    db.close()

