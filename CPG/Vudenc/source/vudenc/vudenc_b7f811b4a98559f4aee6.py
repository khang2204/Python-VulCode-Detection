def karma_add(name):...
karma = karma_ask(name)
db = db_connect()
cursor = db.cursor()
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
db.commit()
logger.debug('Inserted into karmadb 1 karma for {}'.format(name))
logger.debug('Inserted into karmadb {} karma for {}'.format(karma, name))
return 1
return karma
