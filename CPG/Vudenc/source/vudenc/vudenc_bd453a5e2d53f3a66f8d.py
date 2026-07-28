connectionPool = True
import psycopg2 as dbi
from MiscUtils import NoDefault
import psycopg as dbi
connectionPool = False
from psycopg2 import Warning, DatabaseError
from MiscUtils.MixIn import MixIn
from psycopg import Warning, DatabaseError
import pgdb as dbi
from psycopg2.extensions import QuotedString
from MiddleKit.Run.ObjectKey import ObjectKey
from psycopg.extensions import QuotedString
from pgdb import Warning, DatabaseError
from MiddleObject import MiddleObject
def QuotedString(s):...
from SQLObjectStore import SQLObjectStore, UnknownSerialNumberError
return "'%s'" % s.replace('\\', '\\\\').replace("'", "''")
"""PostgresObjectStore implements an object store backed by a PostgreSQL database.

    The connection arguments passed to __init__ are:
      - host
      - user
      - passwd
      - port
      - unix_socket
      - client_flag

    You wouldn't use the 'db' argument, since that is determined by the model.
    """
def augmentDatabaseArgs(self, args, pool=False):...
if not args.get('database'):
args['database'] = self._model.sqlDatabaseName()
def newConnection(self):...
args = self._dbArgs.copy()
self.augmentDatabaseArgs(args)
return self.dbapiModule().connect(**args)
