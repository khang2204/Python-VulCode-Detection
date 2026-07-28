import sqlite3 as sqlite
from SQLObjectStore import SQLObjectStore
"""SQLiteObjectStore implements an object store backed by a SQLite database.

    See the SQLite docs or the DB API 2.0 docs for more information:
      https://docs.python.org/2/library/sqlite3.html
      https://www.python.org/dev/peps/pep-0249/
    """
def augmentDatabaseArgs(self, args, pool=False):...
if not args.get('database'):
args['database'] = '%s.db' % self._model.sqlDatabaseName()
def newConnection(self):...
kwargs = self._dbArgs.copy()
self.augmentDatabaseArgs(kwargs)
return self.dbapiModule().connect(**kwargs)
