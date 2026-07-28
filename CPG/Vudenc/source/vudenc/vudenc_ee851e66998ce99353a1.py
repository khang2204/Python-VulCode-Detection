def swissPairings():...
"""docstring"""
records = fetchall('select * from player_static_view order by wins desc')
count = 0
length = len(records)
pairs = []
while count < length:
pairs.append((records[count][0], records[count][1], records[count + 1][0],
    records[count + 1][1]))
return pairs
count += 2
