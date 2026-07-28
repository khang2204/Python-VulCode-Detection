def execute(self, command, args=(), save=False):...
"""docstring"""
for tries in xrange(5, 0, -1):
if args and isinstance(args, tuple):
error = str(sys.exc_value)
return False
self.c.execute(command, args)
self.c.execute(command)
if tries >= 0 and 'is locked' in error:
if save:
logging.debug('Database locked, wait and retry')
if 'readonly' in error:
self.save()
return True
time.sleep(0.5)
logging.error(T('Cannot write to History database, check access rights!'))
if 'not a database' in error or 'malformed' in error or 'duplicate column name' in error:
return True
logging.error(T('Damaged History database, created empty replacement'))
logging.error(T('SQL Command Failed, see log'))
logging.info('Traceback: ', exc_info=True)
logging.debug('SQL: %s', command)
self.close()
logging.info('Traceback: ', exc_info=True)
os.remove(HistoryDB.db_path)
self.connect()
self.con.rollback()
logging.debug('Rollback Failed:', exc_info=True)
return 'duplicate column name' not in error
