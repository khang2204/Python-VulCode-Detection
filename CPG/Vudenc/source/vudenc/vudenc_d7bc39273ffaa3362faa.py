@app.route('/queries', methods=['GET', 'POST'])...
if request.method == 'GET':
return render_template('queries-form.html', queries=get_queries(app, g))
query_key = request.form['query-selector']
query = get_queries(app, g)[query_key]
schema, data = execute_query(app, g, query)
return jsonify([('', schema, data)])
