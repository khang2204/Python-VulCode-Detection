import logging
from datetime import datetime
from queue import Queue
import MySQLdb
from htmlscraper.listing import Listing
logger = logging.getLogger(__name__)
FIELDS_DICT = {'id': 'id', 'title': 'title', 'pubdate': 'publish_date',
    'loc_id': 'location_id', 'addr': 'address', 'bedrooms': 'bedroom_qty',
    'bathrooms': 'bathroom_qty', 'price': 'price', 'pet_friendly':
    'pet_friendly_flag', 'furnished': 'furnished_flag', 'urgent':
    'urgent_flag', 'url': 'url', 'size': 'size', 'desc': 'description'}
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
def get_connection(self):...
logger.debug('Retrieving connection from the pool')
db = self._pool.get()
logger.debug('Type checking connection')
if not isinstance(db, MySQLdb.connections.Connection):
return -1
logger.info('Successful MySQL connection get request')
return db
