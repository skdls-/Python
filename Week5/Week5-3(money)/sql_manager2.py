import requests
import sqlite3
import datetime

from Client import Client

conn = sqlite3.connect("bank.db")
conn.row_factory = sqlite3.Row
cursor = conn.cursor()


def create_clients_table():
    cursor.execute('''create table if not exists
        clients(id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT,
                password TEXT,
                balance REAL DEFAULT 0,
                message TEXT,
                email TEXT,
                last_login TEXT, 
                failed_logins INTEGER DEFAULT 0)''')
    conn.commit()


def change_message(new_message, logged_user):

    cursor.execute('''UPDATE clients SET message = ? WHERE id = ?''',  (
        new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = '%s' WHERE id = '%s'" % (
        new_pass, logged_user.get_id())
    cursor.execute(update_sql)
    conn.commit()


def register(username, password):
    cursor.execute(
        '''INSERT INTO clients (username, password) values (?, ?)''', (username, password))

    conn.commit()


def login(username, password):
    import calendar

    result = cursor.execute(
        'SELECT failed_logins, last_login FROM clients WHERE username = ? LIMIT 1', (username,)).fetchone()
    failed_attempts = int(result[0])
    last_login = int(result[1])
    date = datetime.datetime.now() + datetime.timedelta(minutes=5)
    timestamp = calendar.timegm(date.utctimetuple())

    if failed_attempts > 5 and last_login - timestamp > 300:
        cursor.execute(
            'UPDATE clients SET failed_logins = 0 WHERE username = ?', (username,))
        conn.commit()

    if failed_attempts > 5:
        print('Login attempts exceeded')
        return False

    cursor.execute(
        '''SELECT id, username, balance, message FROM clients WHERE username = ? AND password = ? LIMIT 1''', (username, password))
    user = cursor.fetchone()

    if user and failed_attempts < 6:
        return Client(user[0], user[1], user[2], user[3])
    else:
        date = datetime.datetime.now()
        timestamp = calendar.timegm(date.utctimetuple())
        cursor.execute(
            '''UPDATE clients SET last_login = ?, failed_logins = failed_logins + 1 WHERE username = ? ''', (timestamp, username))
        conn.commit()
        return False


def deposit_money(money, logged_user):
    result = cursor.execute(
        '''SELECT id,balance FROM clients WHERE id= ? ''', (logged_user.get_id(),))
    current_balance = 0
    for client in result:
        current_balance = int(client['balance'])
    current_balance += int(money)
    cursor.execute('''UPDATE clients SET balance = ? WHERE id = ?''',  (
        current_balance, logged_user.get_id()))
    conn.commit()


def display_money(logged_user):
    result = cursor.execute(
        '''SELECT id,balance FROM clients WHERE id= ? ''', (logged_user.get_id(),))
    for client in result:
        print("Your balance is: ", client['balance'])


def withdraw_money(logged_user, money):
    result = cursor.execute(
        '''SELECT id,balance FROM clients WHERE id= ? ''', (logged_user.get_id(),))
    balance = 0
    for client in result:
        balance = int(client['balance'])

    if balance - int(money) < 0:
        print("You have no enough money to withdraw !!!")
    else:
        balance -= int(money)
        cursor.execute('''UPDATE clients SET balance = ? WHERE id = ?''',  (
            balance, logged_user.get_id()))
        print("You withdraw successful !!!")
        conn.commit()
