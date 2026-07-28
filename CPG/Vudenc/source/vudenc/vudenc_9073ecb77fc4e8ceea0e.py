@app.route('/')...
q = Politician.all()
q.order('-search_count')
politicians = []
count = 0
for politician in q:
politicians.append(politician)
return render_template('home.html', politicians=politicians)
count = count + 1
if count == 8:
