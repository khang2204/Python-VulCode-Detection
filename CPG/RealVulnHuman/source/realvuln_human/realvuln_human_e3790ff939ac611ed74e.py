import sqlite3
from time import sleep

def mfa_is_enabled(username):

    conn = sqlite3.connect('db_users.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    user = c.execute("SELECT * FROM users WHERE username = ? and mfa_enabled = 1", (username, )).fetchone()

    if user:
        return True
    else:
        return False


def mfa_disable(username):

    conn = sqlite3.connect('db_users.sqlite')
