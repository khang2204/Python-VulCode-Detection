def close(self):...
"""docstring"""
self.c.close()
logging.error(T('Failed to close database, see log'))
self.con.close()
logging.info('Traceback: ', exc_info=True)
