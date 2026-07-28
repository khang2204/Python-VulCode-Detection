def setLastReplied(messageType, itemId):...
QUERY = (
    "UPDATE twitter_bot_vac_last_replied_id SET item_id = '${0}' WHERE name = '${1}'"
    .format(itemId, messageType))
conn = psycopg2.connect(connectionString)
print('Error %s' % e)
if conn:
cur = conn.cursor()
conn.close()
cur.execute(QUERY)
conn.commit()
cur.close()
