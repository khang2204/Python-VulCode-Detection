@app.route('/json/politicians/all')...
pols = Politician.all()
politicians = []
for pol in pols:
tokens = pol.name.title().split(' ')
resp = Response(response=json.dumps(politicians), status=200, mimetype=
    'application/json')
politician = {'value': pol.name.title(), 'tokens': tokens, 'search_count':
    pol.search_count}
return resp
politicians.append(politician)
