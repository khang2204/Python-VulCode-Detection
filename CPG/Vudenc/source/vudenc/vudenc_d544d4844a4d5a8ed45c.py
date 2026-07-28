def deletePlayers():...
"""docstring"""
conn = connect()
table = 'players'
c = conn.cursor()
c.execute('DELETE FROM %s;' % (table,))
conn.commit()
conn.close()
