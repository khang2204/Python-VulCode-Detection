return ";".join([",".join(row) for row in all_rows])
    except Exception:
        return "error"


EXECUTE_QUERY_FMT = "INSERT INTO Character VALUES ('{}', '1')"


def do_sqlite3_execute(user_input):
    def execute(cursor):
        sql = EXECUTE_QUERY_FMT.format(user_input)
        cursor.execute(sql)

    return _execute(execute)


EXECUTEMANY_QUERY_FMT = "INSERT INTO Character VALUES ('{}', ?)"


def do_sqlite3_executemany(user_input):
    def executemany(cursor):
        sql = EXECUTEMANY_QUERY_FMT.format(user_input)
