def karma_ask(name):...
db = db_connect()
cursor = db.cursor()
cursor.execute(" SELECT karma FROM people WHERE name='{}' ".format(name))
logger.error('Execution failed with error: {}'.format(e))
karma = cursor.fetchone()
if karma is None:
logger.debug('No karma found for name {}'.format(name))
karma = karma[0]
db.close()
logger.debug('karma of {} found for name {}'.format(karma, name))
return karma
db.close()
return karma
