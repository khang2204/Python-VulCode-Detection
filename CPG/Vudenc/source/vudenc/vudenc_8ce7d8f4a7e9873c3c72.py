def db_connect():...
if env.name == None:
logger.debug('Local install, attempting to connect to sqlite DB')
logger.debug('Detected Cloud Foundry, connecting to db service')
if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
if not os.path.exists(DB_PATH + 'karmadb'):
logger.debug('db_config: {}'.format(db_config))
logger.error('Username or password is incorrect')
logger.error('Could not connect to DB for some other reason: {}'.format(err))
logger.info('No database exists. Creating databases for the first time')
db = sqlite3.connect(DB_PATH + DB_NAME)
logger.error('db connection to sqlite was not successful')
logger.debug('db_uri: {}'.format(db_uri))
if not os.path.exists(DB_PATH):
return db
logger.Exception
cnx = psycopg2.connect(db_uri)
os.makedirs(DB_PATH)
db = sqlite3.connect(DB_PATH + DB_NAME)
return cnx
create_karma_table()
create_also_table()
return db
