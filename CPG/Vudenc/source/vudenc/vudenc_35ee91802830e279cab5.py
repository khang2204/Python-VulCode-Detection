@app.route('/save')...
if not 'email' in session and not 'social' in session:
return redirect('/login?return_url=saveAs')
if 'currentFile' in session:
return saveFile(session['currentFile'])
if 'diagram' in request.referrer:
return saveAs(True)
return saveAs()
