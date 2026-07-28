"""
All DB operations, including connection to the appropriate DB, are handled here.

Released under MIT license, copyright 2018 Tyler Ramer
"""
import sqlite3
import os
import logging
from cfenv import AppEnv
import psycopg2
DB_NAME = 'karmadb'
env = AppEnv()
logger = logging.getLogger(__name__)
SERVICE_LABLE = 'elephantsql'
"""
Check what env we have - if on PCF, use mysql connector. Otherwise, we can
use sqlite to build our database. Fortunately, command execution libraries
are identical once we have a cursor.
"""
if env.name == None:
DB_PATH = os.path.expanduser('~/.KarmaBoi/databases/')
db_env = env.get_service(label=SERVICE_LABLE)
logger.critical(
    'not able to generate db_env - ensure db is bound and lable is correct')
PEOPLE_TABLE = """
    CREATE TABLE IF NOT EXISTS people(id SERIAL PRIMARY KEY,
    name TEXT, karma INTEGER, shame INTEGER)
    """
DB_NAME = 'karmadb'
db_creds = db_env.credentials
ALSO_TABLE = """
    CREATE TABLE IF NOT EXISTS isalso(id SERIAL PRIMARY KEY,
    name TEXT, also TEXT)
    """
PEOPLE_TABLE = """
    CREATE TABLE IF NOT EXISTS people(id SERIAL PRIMARY KEY,
    name TEXT, karma INTEGER, shame INTEGER)"""
db_config = {'user': db_creds.get('username'), 'password': db_creds.get(
    'password'), 'host': db_creds.get('hostname'), 'port': db_creds.get(
    'port'), 'database': db_creds.get('name')}
"""
Possible db connect class
class db_connect:
    def __init__(self):
        try:
            logger.debug('Connecting to db service')
            self.cnx = psycopg2.connect(db_uri)
            return self.cnx
        except Exception as e:
            if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logger.error('Username or password is incorrect')
                raise Exception('Could not connect, bad user or pwd')
            else:
                logger.error(
                    'Could not connect to DB for some other reason: {}'.format(
                        err))

    def __exit__(self):
        cnx.close()


"""
ALSO_TABLE = """
    CREATE TABLE IF NOT EXISTS isalso(id SERIAL PRIMARY KEY,
    name TEXT, also TEXT)
    """
db_uri = db_creds.get('uri')
def db_connect():...
if env.name == None:
logger.debug('Local install, attempting to connect to sqlite DB')
logger.debug('Detected Cloud Foundry, connecting to db service')
if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
def check_tables():...
if not os.path.exists(DB_PATH + 'karmadb'):
logger.debug('db_config: {}'.format(db_config))
logger.error('Username or password is incorrect')
logger.error('Could not connect to DB for some other reason: {}'.format(err))
db = db_connect()
logger.info('No database exists. Creating databases for the first time')
db = sqlite3.connect(DB_PATH + DB_NAME)
logger.error('db connection to sqlite was not successful')
logger.debug('db_uri: {}'.format(db_uri))
cursor = db.cursor()
if not os.path.exists(DB_PATH):
return db
logger.Exception
cnx = psycopg2.connect(db_uri)
cursor.execute("""
            SELECT 1 FROM people LIMIT 1;
            """)
cursor.execute("""
            SELECT 1 FROM people LIMIT 1;
            """)
def create_karma_table():...
os.makedirs(DB_PATH)
db = sqlite3.connect(DB_PATH + DB_NAME)
return cnx
cursor.fetchone()
cursor.fetchone()
db = db_connect()
create_karma_table()
logger.debug('people table exists')
logger.debug('people table exists')
cursor = db.cursor()
create_also_table()
cursor.execute(PEOPLE_TABLE)
return db
db.commit()
logger.info('successfully created karma db for the first time')
def create_also_table():...
db = db_connect()
cursor = db.cursor()
cursor.execute(ALSO_TABLE)
db.commit()
logger.info('successfully created also table for the first time')
def karma_ask(name):...
db = db_connect()
cursor = db.cursor()
cursor.execute(" SELECT karma FROM people WHERE name='{}' ".format(name))
logger.error('Execution failed with error: {}'.format(e))
def karma_rank(name):...
karma = cursor.fetchone()
db = db_connect()
if karma is None:
cursor = db.cursor()
logger.debug('No karma found for name {}'.format(name))
karma = karma[0]
cursor.execute(
    """
            SELECT (SELECT COUNT(*) FROM people AS t2 WHERE t2.karma > t1.karma)
            AS row_Num FROM people AS t1 WHERE name='{}'
        """
    .format(name))
logger.error('Execution failed with error: {}'.format(e))
def karma_add(name):...
db.close()
logger.debug('karma of {} found for name {}'.format(karma, name))
rank = cursor.fetchone()[0] + 1
karma = karma_ask(name)
return karma
db.close()
logger.debug('Rank of {} found for name {}'.format(rank, name))
db = db_connect()
return karma
db.close()
cursor = db.cursor()
return rank
if karma is None:
karma = karma + 1
cursor.execute(
    """
                INSERT INTO people(name,karma,shame) VALUES('{}',1,0)
                """
    .format(name))
logger.error('Execution failed with error: {}'.format(e))
db.close()
cursor.execute(
    """
                UPDATE people SET karma = {0} WHERE name = '{1}'
                """
    .format(karma, name))
logger.error('Execution failed with error: {}'.format(e))
db.commit()
def karma_sub(name):...
db.commit()
logger.debug('Inserted into karmadb 1 karma for {}'.format(name))
karma = karma_ask(name)
logger.debug('Inserted into karmadb {} karma for {}'.format(karma, name))
return 1
db = db_connect()
return karma
cursor = db.cursor()
if karma is None:
karma = karma - 1
cursor.execute(
    """
                INSERT INTO people(name,karma,shame) VALUES('{}',-1,0)
                """
    .format(name))
logger.error('Execution failed with error: {}'.format(e))
def karma_top():...
cursor.execute(
    """
                UPDATE people SET karma = {0} WHERE name = '{1}'
                """
    .format(karma, name))
logger.error('Execution failed with error: {}'.format(e))
db.commit()
db = db_connect()
db.commit()
logger.debug('Inserted into karmadb -1 karma for {}'.format(name))
cursor = db.cursor()
logger.debug('Inserted into karmadb -1 karma for {}'.format(name))
db.close()
cursor.execute(' SELECT name, karma FROM people ORDER BY karma DESC LIMIT 5 ')
logger.error('Execution failed with error: {}'.format(e))
def karma_bottom():...
db.close()
return -1
leaders = cursor.fetchall()
db = db_connect()
return karma
logger.debug('fetched top karma values')
cursor = db.cursor()
db.close()
cursor.execute(' SELECT name, karma FROM people ORDER BY karma ASC LIMIT 5 ')
logger.error('Execution failed with error: {}'.format(e))
def shame_ask(name):...
return leaders
leaders = cursor.fetchall()
db = db_connect()
logger.debug('fetched bottom karma values')
cursor = db.cursor()
db.close()
cursor.execute(
    """
            SELECT shame FROM people WHERE name='{}'
            """
    .format(name))
logger.error('Execution failed with error: {}'.format(e))
def shame_add(name):...
return leaders
shame = cursor.fetchone()
shame = shame_ask(name)
db.close()
db = db_connect()
if shame is None:
cursor = db.cursor()
logger.debug('No shame found for name {}'.format(name))
shame = shame[0]
if shame is None:
return shame
logger.debug('shame of {} found for name {}'.format(shame, name))
shame = shame + 1
cursor.execute(
    """
                INSERT INTO people(name,karma,shame) VALUES('{}',0,1)
                """
    .format(name))
logger.error('Execution failed with error: {}'.format(e))
def shame_top():...
return shame
cursor.execute(
    """
                UPDATE people SET shame = {0} WHERE name = '{1}'
                """
    .format(shame, name))
logger.error('Execution failed with error: {}'.format(e))
db.commit()
db = db_connect()
db.commit()
logger.debug('Inserted into karmadb 1 shame for {}'.format(name))
cursor = db.cursor()
logger.debug('Inserted into karmadb {} shame for {}'.format(shame, name))
db.close()
cursor.execute(' SELECT name, shame FROM people ORDER BY shame DESC LIMIT 5 ')
logger.error('Execution failed with error: {}'.format(e))
def also_add(name, also):...
db.close()
return 1
leaders = cursor.fetchall()
db = db_connect()
return shame
logger.debug('fetched top shame values')
cursor = db.cursor()
return leaders
cursor.execute(
    """
            INSERT INTO isalso(name,also) VALUES('{}','{}')
            """
    .format(name, also))
logger.error('Execution failed with error: {}'.format(e))
def also_ask(name):...
db.commit()
db = db_connect()
logger.debug('added to isalso name {} with value {}'.format(name, also))
cursor = db.cursor()
db.close()
if env.name == None:
r = 'RANDOM()'
r = 'RANDOM()'
cursor.execute(
    """
            SELECT also FROM isalso WHERE name='{0}' ORDER BY {1} LIMIT 1
            """
    .format(name, r))
logger.error('Execution failed with error: {}'.format(e))
also = cursor.fetchone()
db.close()
if also is None:
logger.debug('could not find is_also for name {}'.format(name))
also = also[0]
return also
logger.debug('found is_also {} for name {}'.format(also, name))
return also
