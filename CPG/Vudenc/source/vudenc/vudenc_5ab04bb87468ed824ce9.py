def registerPlayer(name):...
"""docstring"""
c = connect()
c.cursor().execute('INSERT INTO players(name) VALUES (%s)', (name,))
c.commit()
c.close()
