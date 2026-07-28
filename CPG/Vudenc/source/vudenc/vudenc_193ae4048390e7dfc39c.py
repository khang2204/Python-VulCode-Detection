def save(self):...
"""docstring"""
self.con.commit()
logging.error(T('SQL Commit Failed, see log'))
logging.info('Traceback: ', exc_info=True)
