HERE = Path(__file__).parent


def login(username, password, **kwargs):

    conn = sqlite3.connect('db_users.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    user = c.execute("SELECT * FROM users WHERE username = ?", (username,)).fetchone()

    if not user:
        #print('The user doesnt exists')
        return False

    backend = default_backend()

    kdf = Scrypt(
        salt=unhexlify(user['salt']),
        length=32,
