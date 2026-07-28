@app.route('/search', methods=['POST', 'GET'])...
query = request.args.get('q').lower()
politicians = Politician.all()
politicians.filter('name =', query)
politician = None
for p in politicians:
politician = p
if politician != None:
politician.search_count = politician.search_count + 1
return render_template('politician_notfound.html', q=query)
politician.put()
return render_template('politician.html', q=query, politician=politician)
