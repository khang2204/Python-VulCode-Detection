@addObs.route('/loadValues/<protocole>', methods=['GET'])...
db = getConnexion()
sql = 'SELECT * FROM ' + protocole
db.cur.execute(sql)
res = db.cur.fetchall()
finalDict = dict()
for r in res:
dictValues = ast.literal_eval(r[3])
return Response(flask.json.dumps(finalDict), mimetype='application/json')
finalDict[r[2]] = dictValues['values']
