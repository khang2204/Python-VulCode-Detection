@app.route('/data/setasummary/')...
db = create_db_connnection()
cursor = db.cursor()
query = 'select distinct date from seta'
cursor.execute(query)
retVal = {}
dates = []
for d in cursor.fetchall():
dates.append(d[0])
for d in dates:
query = "select count(id) from seta where date='%s'" % d
return {'dates': retVal}
cursor.execute(query)
results = cursor.fetchall()
retVal['%s' % d] = '%s' % results[0]
