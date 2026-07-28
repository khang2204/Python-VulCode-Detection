@app.route('/achievements/<achievement_id>/increment', methods=['POST'])...
"""docstring"""
player_id = int(request.form.get('player_id'))
steps = int(request.form.get('steps', 1))
return flask.jsonify(increment_achievement(achievement_id, player_id, steps))
