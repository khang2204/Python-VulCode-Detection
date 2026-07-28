@app.route('/politicians/id/<name>')...
name = name.lower()
politicians = Politician.all()
politicians.filter('name =', name)
politician = None
for p in politicians:
politician = p
if politician != None:
politician.search_count = politician.search_count + 1
return render_template('politician_notfound.html', q=name)
politician.put()
return render_template('politician.html', q=name, politician=politician)
