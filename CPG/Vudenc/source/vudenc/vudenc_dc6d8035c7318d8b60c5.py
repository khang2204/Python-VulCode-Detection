@app.route('/achievements/<achievement_id>/unlock', methods=['POST'])...
"""docstring"""
player_id = int(request.form.get('player_id'))
return flask.jsonify(unlock_achievement(achievement_id, player_id))
