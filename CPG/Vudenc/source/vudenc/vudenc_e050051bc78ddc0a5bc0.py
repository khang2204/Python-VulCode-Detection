def also_ask(name):...
db = db_connect()
cursor = db.cursor()
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
