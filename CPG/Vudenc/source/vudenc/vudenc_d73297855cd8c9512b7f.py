@app.route('/achievements/<achievement_id>')...
"""docstring"""
language = request.args.get('language', 'en')
region = request.args.get('region', 'US')
cursor = db.connection.cursor(db.pymysql.cursors.DictCursor)
cursor.execute(SELECT_ACHIEVEMENTS_QUERY +
    'WHERE ach.id = %(achievement_id)s', {'language': language, 'region':
    region, 'achievement_id': achievement_id})
return cursor.fetchone()
