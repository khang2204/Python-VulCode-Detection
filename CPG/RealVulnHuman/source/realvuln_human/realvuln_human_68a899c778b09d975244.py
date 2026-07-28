cursor = connection.cursor()
content = 'Please login, <strong>Anonymous</strong>!'

if 'SESSIONID' in handler.cookie:
    session = handler.cookie['SESSIONID'].value
    cursor.execute("SELECT * FROM users WHERE session = ?", [session])

    user = cursor.fetchone()
    if user:

        if 'delete' in params.keys():
            cursor.execute("DELETE FROM users WHERE id = ?", [user[0]])
            connection.commit()
            content = '''
            <div class="alert alert-success">
                Your account has been deleted!
            </div>
            '''
        else:
            content = '''
            <div class="alert alert-danger">
                Irreversible and destructive actions!
            </div>
