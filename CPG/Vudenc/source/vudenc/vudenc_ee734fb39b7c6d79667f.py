import psycopg2
import secretConstants
connectionString = ('dbname=' + secretConstants.DATABASE_NAME + ' user=' +
    secretConstants.DATABASE_USER + ' host=' + secretConstants.
    DATABASE_HOST + ' password=' + secretConstants.DATABASE_PASSWORD +
    ' port=' + secretConstants.DATABASE_PORT)
conn = None
result = None
def getLastReplied(messageType):...
QUERY = (
    "SELECT item_id from twitter_bot_vac_last_replied_id where name = '{0}'"
    .format(messageType))
conn = psycopg2.connect(connectionString)
print('Error %s' % e)
if conn:
return result[0]
cur = conn.cursor()
conn.close()
cur.execute(QUERY)
result = cur.fetchone()
