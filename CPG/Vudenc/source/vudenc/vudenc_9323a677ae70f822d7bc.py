@app.route('/players/<int:player_id>/achievements')...
"""docstring"""
cursor = db.connection.cursor(db.pymysql.cursors.DictCursor)
cursor.execute(
    """SELECT
                            achievement_id,
                            current_steps,
                            state,
                            UNIX_TIMESTAMP(create_time) as create_time,
                            UNIX_TIMESTAMP(update_time) as update_time
                        FROM player_achievements
                        WHERE player_id = '%s'"""
     % player_id)
return flask.jsonify(items=cursor.fetchall())
