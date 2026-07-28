import new
import MySQLdb
from MySQLdb import Warning
from SQLObjectStore import SQLObjectStore
"""MySQLObjectStore implements an object store backed by a MySQL database.

    MySQL notes:
      * MySQL home page: http://www.mysql.com.
      * MySQL version this was developed and tested with: 3.22.34 & 3.23.27
      * The platforms developed and tested with include Linux (Mandrake 7.1)
        and Windows ME.
      * The MySQL-Python DB API 2.0 module used under the hood is MySQLdb
        by Andy Dustman: http://dustman.net/andy/python/MySQLdb/.
      * Newer versions of MySQLdb have autocommit switched off by default.

    The connection arguments passed to __init__ are:
      - host
      - user
      - passwd
      - port
      - unix_socket
      - client_flag
      - autocommit

    You wouldn't use the 'db' argument, since that is determined by the model.

    See the MySQLdb docs or the DB API 2.0 docs for more information.
      http://www.python.org/topics/database/DatabaseAPI-2.0.html
    """
def __init__(self, **kwargs):...
self._autocommit = kwargs.pop('autocommit', False)
SQLObjectStore.__init__(self, **kwargs)
def augmentDatabaseArgs(self, args, pool=False):...
if not args.get('db'):
args['db'] = self._model.sqlDatabaseName()
def newConnection(self):...
kwargs = self._dbArgs.copy()
self.augmentDatabaseArgs(kwargs)
conn = self.dbapiModule().connect(**kwargs)
if self._autocommit:
return conn
conn.autocommit(True)
