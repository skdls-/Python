import requests
import sqlite3
from Client import Client
import hashlib
import getpass
import datetime
import calendar

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()


def secured_pass(password):
    long_enough = len(password) > 8
    uppers = [l for l in password if l.isupper()]
    has_uppers = len(uppers) > 0
    specials = ["@", "!", "#", '^', "*"]
    specs = [s for s in password if s in specials]
    has_specs = len(specs) > 0
    if (long_enough and has_uppers and has_specs):
        return True
    return False



def create_clients_table():

    cursor.execute('''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                failed_logins INTEGER DEFAULT 0,
                last_login TEXT DEFAULT '')''')


def change_message(new_message, logged_user):

    cursor.execute('''UPDATE clients SET message = ? WHERE id = ?''', (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    if secured_pass(password.encode()):
        update_sql = "UPDATE clients SET password = '%s' WHERE id = '%s'" % (new_pass, logged_user.get_id())
        cursor.execute(update_sql)
        conn.commit()
    else:
        print("New pass not valid!")
        change_pass(new_pass, logged_user)


def register(username, password):
    while not secured_pass(password):
        print("Your password is not valid. Must have 8 symbols, a special sybol and a capital letter!")
        password = input("Try another pass: ")
        register(username, password)
        return False
    else:
        print('here')
        hashed_pass = hashlib.sha1(password.encode())
        hex_dig = hashed_pass.hexdigest()
        cursor.execute('''insert into clients (username, password) values (?, ?)''',  (username, hex_dig))
        conn.commit()
        return True


def login(username, password):
    hashed_pass = hashlib.sha1(password.encode()).hexdigest()
    user = cursor.execute('''SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ?''', (username, hashed_pass)).fetchone()

    login_attempts = cursor.execute('SELECT failed_logins, id FROM clients WHERE username = ?', (username,)).fetchone()
    if login_attempts is None:
        login_attempts = 0

    if user and login_attempts < 6:
        return Client(user[0], user[1], user[2], user[3])
    else:
        login_attempts += 1
        date_now = datetime.datetime.utcnow()
        timestamp_now = calendar.timegm(date_now.utctimetuple())
        print(timestamp_now)
        print(login_attempts)
        id = cursor.execute('SELECT id FROM clients WHERE username = ?', (username,)).fetchone()
        cursor.execute('UPDATE clients SET failed_logins = ?, last_login = ? WHERE id = ?', (login_attempts, timestamp_now, id))
        return False # Gr@b@na!!!