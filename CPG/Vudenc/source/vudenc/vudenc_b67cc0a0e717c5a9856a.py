@endpoints.route('/placings')...
if db == None:
init()
tag = request.args.get('tag', default='christmas mike')
sql = "SELECT * FROM placings WHERE player = '{}'".format(tag)
results = list(db.exec(sql))
results.sort(key=lambda x: int(x[2]))
return json.dumps(results)
