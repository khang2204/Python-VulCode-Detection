@app.route('/achievements')...
"""docstring"""
language = request.args.get('language', 'en')
region = request.args.get('region', 'US')
cursor = db.connection.cursor(db.pymysql.cursors.DictCursor)
cursor.execute(SELECT_ACHIEVEMENTS_QUERY + ' ORDER BY `order` ASC', {
    'language': language, 'region': region})
return flask.jsonify(items=cursor.fetchall())
