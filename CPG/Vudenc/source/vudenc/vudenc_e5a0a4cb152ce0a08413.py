def getRankingsFromDatabase(submission):...
database = sqlite3.connect('database.db')
cursor = database.cursor()
nameSet = set()
for row in cursor.execute(
for val in row:
nameList = [name for name in nameSet]
if val is not '':
table = [[name, 0, 0, 0] for name in nameList]
for author in val.split('|'):
for i in range(1, 4):
nameSet.add(author)
for row in cursor.execute('SELECT Place' + str(i) +
table.sort(reverse=True, key=operator.itemgetter(1, 2, 3))
for val in row:
database.close()
if val is not '':
return table
for author in val.split('|'):
table[nameList.index(author)][i] += 1
