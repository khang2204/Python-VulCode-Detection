def get_user_profiles():...
"""docstring"""
user_con = sql.connect('./resources/users.db')
response = False
user_cur = user_con.cursor()
print(''.join(traceback.format_exception(etype=type(e), value=e, tb=e.
    __traceback__)))
user_con.close()
return response
user_cur.execute('SELECT * from user;')
user_con.rollback()
response = user_cur.fetchall()
