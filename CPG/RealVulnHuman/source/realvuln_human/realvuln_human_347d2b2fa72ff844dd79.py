import sqlite3

SELECT_ALL = "SELECT * FROM Character"


def _db_reset():
    db_connection = sqlite3.connect(":memory:", check_same_thread=False)
    db_connection.executescript(
        """
        DROP TABLE IF EXISTS Character;
        CREATE TABLE Character(value, count);
        INSERT INTO Character VALUES
            ('a', '3'),('b', '5'),('c', '1')
        """
    )
    db_connection.commit()
    return db_connection
