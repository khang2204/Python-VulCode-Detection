def shame_top():...
db = db_connect()
cursor = db.cursor()
cursor.execute(' SELECT name, shame FROM people ORDER BY shame DESC LIMIT 5 ')
logger.error('Execution failed with error: {}'.format(e))
leaders = cursor.fetchall()
logger.debug('fetched top shame values')
return leaders
