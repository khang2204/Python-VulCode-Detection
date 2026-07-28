def shame_ask(name):...
db = db_connect()
cursor = db.cursor()
cursor.execute(
    """
            SELECT shame FROM people WHERE name='{}'
            """
    .format(name))
logger.error('Execution failed with error: {}'.format(e))
shame = cursor.fetchone()
db.close()
if shame is None:
logger.debug('No shame found for name {}'.format(name))
shame = shame[0]
return shame
logger.debug('shame of {} found for name {}'.format(shame, name))
return shame
