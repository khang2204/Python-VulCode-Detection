"""Functions for interfacing with the SQL databases.
"""
import sqlite3 as sql
import traceback
def authenticate(username, password):...
"""docstring"""
con = sql.connect('./resources/users.db')
authenticated = False
cmd = """SELECT * FROM users
             WHERE username = ? AND password = ?;
    """
cur = con.cursor()
info = username, password
cur.execute(cmd, info)
user_info = cur.fetchone()
if user_info != None:
authenticated = True
authenticated = False
user_id = user_info[0]
user_id = None
firstname = user_info[2]
firstname = None
lastname = user_info[3]
lastname = None
con.close()
return authenticated, user_id, firstname, lastname
