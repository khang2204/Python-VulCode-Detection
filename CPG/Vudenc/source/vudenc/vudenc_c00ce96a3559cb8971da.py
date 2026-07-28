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
