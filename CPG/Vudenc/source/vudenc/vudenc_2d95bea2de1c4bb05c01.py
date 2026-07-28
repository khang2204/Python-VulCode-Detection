@app.route('/achievements/<achievement_id>/reveal', methods=['POST'])...
"""docstring"""
player_id = int(request.form.get('player_id'))
return flask.jsonify(reveal_achievement(achievement_id, player_id))
