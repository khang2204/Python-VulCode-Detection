)

    key = kdf.derive(password.encode())

    conn = sqlite3.connect('db_users.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    print('Changing password for', username)
    c.execute("UPDATE users SET password = ?, salt = ? WHERE username = ?", (hexlify(key).decode(), hexlify(salt).decode(), username))
    conn.commit()


def userlist():

    conn = sqlite3.connect('db_users.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
