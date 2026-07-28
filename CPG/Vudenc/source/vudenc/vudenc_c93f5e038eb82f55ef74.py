def __init__(self, hostaddr, usr, pwd, dbname, size):...
logger.info('Initializing an instance of MySQLConnectionPool')
logger.debug(
    'Type checking for host address, username, password, database name and pool size'
    )
if type(hostaddr) != str:
if type(usr) != str:
if type(pwd) != str:
if type(dbname) != str:
logger.debug('All type checks passed')
logger.info('Initializing class variables')
self._hostaddr = hostaddr
self._usr = usr
self._pwd = pwd
self._dbname = dbname
logger.info('Initializing MySQL connection pool')
self._pool = Queue(size)
for i in range(size):
self._pool.put(MySQLdb.connect(hostaddr, usr, pwd, dbname), block=False)
logger.info('Initialized MySQL connection pool')
