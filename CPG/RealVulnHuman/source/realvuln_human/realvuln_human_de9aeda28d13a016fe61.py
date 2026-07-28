if 'SESSIONID' in handler.cookie:
    session = handler.cookie['SESSIONID'].value
    cursor.execute("SELECT * FROM users WHERE session = ?", [session])

    user = cursor.fetchone()
    if user:

        if 'email' in params.keys():
            email = params.get('email')[0]
            cursor.execute("UPDATE users SET email = ? WHERE id = ?", (email, user[0]))
            connection.commit()
            content = 'Your settings have been updated!'
        else:
            content = '''
            <p>Change your profile settings here:</p>
            <form method="GET" action="/settings">
                <div class="form-group">
                    <label for="firstname">First name:</label>
                    <input type="text" id="firstname" name="firstname" class="form-control" value="{}">
                </div>
