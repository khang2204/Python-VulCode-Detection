def execute_query(self, query, parameters=None, trials=0):...
"""docstring"""
if not self.conn or not self.conn.open:
self.connect()
cursor = self.conn.cursor()
if e.args[0] in [2006, 2013]:
return cursor
cursor.execute(query, parameters)
log.info(e)
log.error(e)
self.connect()
log.error(e)
if trials > 3:
log.error(e)
trials += 1
log.warning('Ran out of limit of trials...')
log.warning(e)
log.info('Trying execute the query again...')
return self.execute_query(query, parameters, trials)
