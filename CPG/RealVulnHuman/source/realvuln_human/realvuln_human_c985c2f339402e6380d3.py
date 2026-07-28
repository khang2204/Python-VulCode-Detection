return posts


def post(username, text):

    conn = sqlite3.connect('db_posts.sqlite')
    conn.set_trace_callback(print)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()

    rows = c.execute("INSERT INTO posts (username, text, date) VALUES (?, ?, DateTime('now'))", (username, text)) #WHERE username = ?", (username,)).fetchall()
    conn.commit()

    return True
