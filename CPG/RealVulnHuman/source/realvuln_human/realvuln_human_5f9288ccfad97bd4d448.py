)
    db_connection.commit()
    return db_connection


def _execute(db_func):
    try:
        db_connection = _db_reset()
        cursor = db_connection.cursor()
        db_func(cursor)
        all_rows = cursor.execute(SELECT_ALL)
        return ";".join([",".join(row) for row in all_rows])
    except Exception:
        return "error"


EXECUTE_QUERY_FMT = "INSERT INTO Character VALUES ('{}', '1')"


def do_sqlite3_execute(user_input):
    def execute(cursor):
