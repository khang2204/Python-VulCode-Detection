"""todo_server_db.py

A class for communicating with MySQL to add, update, and remove tags and tasks.
"""
import sys
import datetime
import MySQLdb
"""Interface to the MySQL database.

    A class for communicating with MySQL to add, update, and remove tags and
    tasks. Changing database methods will effect network/network.py since
    the method calls are only defined there and in the actual client script
    todo.py. The global attributes here are used as responses from the Todo
    server in todo_server_thread.py.

    Attributes:
        DEFAULT_TAG: tag to default to if no default tag is specified
        CANT_CONNECT: returned when Database can't connect to MySQL
        SUCCESS: returned for successful database calls
        DUPLICATE: returned when a method attempts to insert a duplicate entry
        DOES_NOT_EXIST: returned when a delete or update method can not find the
            row to delete or update
        INVALID_DATE: returned when a date passed to a method is not valid
        DATA: returned when data is passed across the network rather than an
            enumerated reponse
    """
DEFAULT_TAG = 'misc'
CANT_CONNECT = 0
SUCCESS = 1
DUPLICATE = 2
DOES_NOT_EXIST = 3
INVALID_ID = 4
INVALID_DATE = 5
DATA = 6
def __init__(self, default_tag):...
"""docstring"""
self.default_tag = default_tag
def connect(self, hostname='localhost', username='todo', password='todo',...
"""docstring"""
self.__con = MySQLdb.connect(hostname, username, password, database)
return Database.CANT_CONNECT
def close(self):...
self.__con.autocommit(True)
"""docstring"""
return Database.SUCCESS
self.__con.close()
@staticmethod...
"""docstring"""
pieces = map(lambda x: int(x), date.split('-'))
return Database.INVALID_DATE
return valid_date.isoformat()
valid_date = datetime.date(pieces[2], pieces[0], pieces[1])
