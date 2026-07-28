class XSRequestForgery(Attack):
    def run(self, handler):
        params = handler.params
        connection = handler.server.connection
        cursor = connection.cursor()
        content = 'Please login, <strong>Anonymous</strong>!'

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
