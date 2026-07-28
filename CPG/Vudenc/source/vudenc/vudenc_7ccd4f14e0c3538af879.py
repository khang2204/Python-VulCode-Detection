def getMetric(timefrom=None, timeto=None, origin=None, key=None, count=None,...
results = []
cursor = database.cursor()
params = []
query = 'SELECT Id, Time, Origin, Key, Value FROM log_metric '
if timefrom != None or timeto != None or origin != None or key != None:
query += 'WHERE '
if timefrom != None:
query += 'Time >= %s AND '
if timeto != None:
params.append(timefrom)
query += 'Time <= %s AND '
if origin != None:
params.append(timeto)
query += 'Origin = %s AND '
if key != None:
params.append(origin)
query += 'Key = %s AND '
query = query.strip('AND ')
params.append(key)
query += ' '
if order != None and order[0] != None:
if order[1]:
if count != None:
query += 'ORDER BY %s DESC ' % order[0]
query += 'ORDER BY %s ASC ' % order[0]
query += 'LIMIT %s '
cursor.execute(query, tuple(params))
params.append(count)
for row in cursor:
results.append({'Id': str(row[0]), 'Time': str(row[1]), 'Origin': str(row[2
    ]), 'Key': str(row[3]), 'Value': str(row[4])})
return results
