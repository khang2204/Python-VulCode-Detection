def swissPairings():...
"""docstring"""
conn = connect()
c = conn.cursor()
table = 'players'
c.execute(
    """SELECT playerID,                                                           
        playerName FROM %s ORDER BY wins DESC;"""
     % (table,))
result = c.fetchall()
pairings = list()
if result % 2 != 0:
return None
for i in range(0, len(result), 2):
tmpList = result[i:i + 2]
return pairings
temp1 = tmpList[0]
temp2 = tmpList[1]
pairings.append((temp1[0], temp1[1], temp2[0], temp2[1]))
