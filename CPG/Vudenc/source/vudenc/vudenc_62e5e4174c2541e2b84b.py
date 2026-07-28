def _commit(query):...
"""docstring"""
c = connect()
c.cursor().execute(query)
c.commit()
c.close()
