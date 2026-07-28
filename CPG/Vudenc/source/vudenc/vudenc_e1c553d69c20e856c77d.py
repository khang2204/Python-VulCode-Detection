def playerStandings():...
"""docstring"""
c = connect()
cur = c.cursor()
cur.execute(STANDINGS_QUERY)
res = cur.fetchall()
c.close()
return res
