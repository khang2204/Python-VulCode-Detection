return content


class SessionHijacking(Attack):
    def run(self, handler):
        cursor = handler.server.connection.cursor()
        content = 'Please login, <strong>Anonymous</strong>!'

        if 'SESSIONID' in handler.cookie:
            session = handler.cookie['SESSIONID'].value
            cursor.execute("SELECT * FROM users WHERE session = ?", [session])

            user = cursor.fetchone()
            if user:
                content = '''
                <h2>Welcome <strong>{}</strong>!</h2>
                Your first name: <pre>{}</pre>
                Your last name: <pre>{}</pre>
                Your email address: <pre>{}</pre>
                '''.format(user[1], user[2], user[3], user[4])
