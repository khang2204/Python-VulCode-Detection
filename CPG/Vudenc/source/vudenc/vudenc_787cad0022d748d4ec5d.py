def shame_add(name):...
shame = shame_ask(name)
db = db_connect()
cursor = db.cursor()
if shame is None:
shame = shame + 1
cursor.execute(
    """
                INSERT INTO people(name,karma,shame) VALUES('{}',0,1)
                """
    .format(name))
logger.error('Execution failed with error: {}'.format(e))
cursor.execute(
    """
                UPDATE people SET shame = {0} WHERE name = '{1}'
                """
    .format(shame, name))
logger.error('Execution failed with error: {}'.format(e))
db.commit()
db.commit()
logger.debug('Inserted into karmadb 1 shame for {}'.format(name))
logger.debug('Inserted into karmadb {} shame for {}'.format(shame, name))
db.close()
db.close()
return 1
return shame
