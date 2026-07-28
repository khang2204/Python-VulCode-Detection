session TEXT
    )''')

connection.execute('''
    CREATE TABLE comments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        comment TEXT,
        time TEXT
    )''')

connection.executemany('''
    INSERT INTO users(id, username, firstname, lastname, email, password, session) VALUES(NULL, ?, ?, ?, ?, ?, ?)''',
    users)
