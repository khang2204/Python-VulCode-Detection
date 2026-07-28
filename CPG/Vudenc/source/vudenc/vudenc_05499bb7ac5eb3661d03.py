@app.route('/json/politicians/state/<state>')...
pols = Politician.all()
pols.filter('state =', state.lower())
pols.order('-search_count')
politicians = []
for pol in pols:
politician = {'name': pol.name, 'party': pol.party, 'state': pol.state,
    'constituency': pol.constituency, 'wiki': pol.wiki_link, 'search_count':
    pol.search_count}
return jsonify(politicians=politicians)
politicians.append(politician)
