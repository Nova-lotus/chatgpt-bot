import sqlite3
from sqlite3 import Error

def create_connection():
    conn = None;
    try:
        conn = sqlite3.connect(':memory:') # change this to 'database.db' to persist data
        print(sqlite3.version)
    except Error as e:
        print(e)

    if conn:
        create_table(conn)

def create_table(conn):
    try:
        sql = '''CREATE TABLE userdata (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    mood TEXT,
                    reminder TEXT,
                    conversation_history TEXT
                ); '''
        conn.execute(sql)
    except Error as e:
        print(e)

def insert_user_data(conn, data):
    try:
        sql = '''INSERT INTO userdata(username, mood, reminder, conversation_history) 
                VALUES(?,?,?,?) '''
        conn.execute(sql, data)
        conn.commit()
    except Error as e:
        print(e)

def get_user_data(conn, username):
    try:
        sql = '''SELECT * FROM userdata WHERE username=?'''
        cur = conn.cursor()
        cur.execute(sql, (username,))
        return cur.fetchone()
    except Error as e:
        print(e)

def update_user_data(conn, data):
    try:
        sql = '''UPDATE userdata SET mood = ?, reminder = ?, conversation_history = ? WHERE username = ?'''
        conn.execute(sql, data)
        conn.commit()
    except Error as e:
        print(e)

create_connection()