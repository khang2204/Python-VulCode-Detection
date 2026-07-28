cursor.execute(sql)

    return _execute(execute)


EXECUTEMANY_QUERY_FMT = "INSERT INTO Character VALUES ('{}', ?)"


def do_sqlite3_executemany(user_input):
    def executemany(cursor):
        sql = EXECUTEMANY_QUERY_FMT.format(user_input)
        cursor.executemany(sql, [("1")])

    return _execute(executemany)


EXECUTESCRIPT_QUERY_FMT = "INSERT INTO Character VALUES ('{}', '1'); SELECT 0"


def do_sqlite3_executescript(user_input):
    def executescript(cursor):
        sql = EXECUTESCRIPT_QUERY_FMT.format(user_input)
