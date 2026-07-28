@app.route('/')...
editor_content = ''
if session.get('tempFile') is not None:
if session['tempFile'] != '':
if 'filename' in request.args or filename != '' or 'currentFile' in session:
editor_content = open(session['tempFile']).read()
if not filename:
return render_template('editor.html', editor_content=editor_content)
if 'filename' in request.args:
if 'email' in session or 'social' in session:
filename = request.args['filename']
filename = session['currentFile']
if 'email' in session:
email = session['email']
if 'social' in session:
userpath = os.path.join(app.config['UPLOAD_FOLDER'], email)
email = session['social']
filepath = os.path.join(userpath, filename)
session['currentFile'] = filename
editor_content = f.read()
editor_content = ''
