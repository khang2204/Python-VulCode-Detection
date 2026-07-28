@app.route('/diagram')...
if 'filename' in request.args:
filename = request.args['filename']
if 'tempFile' in session or 'currentFile' in session:
if 'email' in session or 'social' in session:
if 'tempFile' in session:
return render_template('diagramEditor.html')
if 'email' in session:
filepath = session['tempFile']
if 'currentFile' in session and 'email' in session or 'social' in session:
email = session['email']
if 'social' in session:
if 'email' in session:
data = f.read()
userpath = os.path.join(app.config['UPLOAD_FOLDER'], email)
email = session['social']
email = session['email']
if 'social' in session:
parsed = parser.parse(data)
filepath = os.path.join(userpath, filename)
filename = session['currentFile']
email = session['social']
return render_template('diagramEditor.html', data=json.dumps(parsed))
session['currentFile'] = filename
userpath = os.path.join(app.config['UPLOAD_FOLDER'], email)
data = f.read()
editor_content = ''
filepath = os.path.join(userpath, filename)
parsed = parser.parse(data)
return render_template('diagramEditor.html', data=json.dumps(parsed))
