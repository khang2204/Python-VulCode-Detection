@app.route('/api/uploads/<sid>/download')...
if not utils.sid_is_valid(sid):
abort(400)
path = os.path.join(app.config['UPLOAD_FOLDER'], sid)
if os.path.isfile(os.path.join(path, app.config['RESULTS_ZIP'])):
return send_from_directory(directory=path, filename=app.config['RESULTS_ZIP'])
abort(404)
