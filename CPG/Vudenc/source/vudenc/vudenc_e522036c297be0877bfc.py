@app.route('/api/uploads/<sid>/logs')...
if '/' not in sid:
path = os.path.join(app.config['UPLOAD_FOLDER'], sid)
abort(403)
if os.path.isfile(os.path.join(path, app.config['LOG_FILE'])):
return send_from_directory(directory=path, filename=app.config['LOG_FILE'])
abort(404)
