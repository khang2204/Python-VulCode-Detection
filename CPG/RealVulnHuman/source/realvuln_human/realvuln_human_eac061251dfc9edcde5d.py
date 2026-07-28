if params.keys() == {'username', 'password'}:
    username = re.sub(r"[^\w]", '', params.get('username')[0])
    password = params.get('password')[0]

    if username == 'dsvpwa' and password == 'dsvpwa':
        user = ['dsvpwa', 'Default', 'Default', 'dsvpwa']
    else:
        try:
            cursor.execute("SELECT * FROM users WHERE username='" +  username + "' AND password='" + password + "'")
        except sqlite3.OperationalError as e:
            return content.format(type=type, message=e)
        user = cursor.fetchone()

    if user:
        type = 'success'
        message = 'Welcome <strong>{} {}</strong>!'.format(user[2], user[3])
        cursor.execute("UPDATE users SET session = ? WHERE id = ?", (session, user[0]))
        connection.commit()
    else:
        type = 'danger'
        message = 'The username and/or password is incorrect!'
