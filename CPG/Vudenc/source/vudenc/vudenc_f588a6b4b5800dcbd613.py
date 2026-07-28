@app.route('/search', methods=['GET', 'POST'])...
if request.method == 'GET':
return render_template('search-form.html')
keywords = request.form['keywords']
tables = list(request.form.keys())
tables.remove('keywords')
data = generic_search(keywords, tables, app, g)
return jsonify(data)
