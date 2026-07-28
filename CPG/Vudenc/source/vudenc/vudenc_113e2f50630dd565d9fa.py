@app.route('/api/script_update', methods=['POST'])...
if not app.config['FIREBASE']:
abort(400)
if request.json is None:
abort(400)
if request.json['auth_token'] != app.config['API_KEY']:
abort(403)
sid = request.json['session_id']
abort(400)
data = {'progress': progress, 'text': text}
progress = int(request.json['progress'])
fbdb.child('sessions').child(sid).set(data)
text = request.json['text']
return '', 200
