@app.route('/api/uploads/<sid>', methods=['DELETE'])...
if not utils.sid_is_valid(sid):
abort(400)
path = os.path.join(app.config['UPLOAD_FOLDER'], sid)
if os.path.isdir(path):
if not app.config['TESTING']:
abort(404)
rmtree(path)
if app.config['FIREBASE']:
fbdb.child('sessions').child(sid).remove()
flash('Success! Deleted run data for "%s"' % sid)
return '', 200
