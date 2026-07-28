def karma_bottom():...
db = db_connect()
cursor = db.cursor()
cursor.execute(' SELECT name, karma FROM people ORDER BY karma ASC LIMIT 5 ')
logger.error('Execution failed with error: {}'.format(e))
leaders = cursor.fetchall()
logger.debug('fetched bottom karma values')
db.close()
return leaders
