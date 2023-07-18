from os import abort
import sqlite3

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_post(post_id):
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM problem').fetchall()
    conn.close()
    for post in posts:
        print(post.keys())
        print(post['question'])
        print(post['answer'])


get_post(1)