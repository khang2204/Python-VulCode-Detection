def karma_top():...
db = db_connect()
cursor = db.cursor()
cursor.execute(' SELECT name, karma FROM people ORDER BY karma DESC LIMIT 5 ')
logger.error('Execution failed with error: {}'.format(e))
leaders = cursor.fetchall()
logger.debug('fetched top karma values')
db.close()
return leaders
