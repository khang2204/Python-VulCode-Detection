@app.route('/upload', methods=['POST'])...
if not 'email' in session and not 'social' in session:
return '', 401
if 'email' in session:
email = session['email']
if 'social' in session:
file = request.files['file']
email = session['social']
filename = ''
if file and allowed_file(file.filename):
filename = secure_filename(file.filename)
flash('Invalid file')
userpath = os.path.join(app.config['UPLOAD_FOLDER'], email)
return redirect('/openFile')
os.makedirs(userpath, exist_ok=True)
file.save(os.path.join(userpath, filename))
session['currentFile'] = filename
if 'diagram' in request.referrer:
return redirect('/diagram?filename=%s' % filename)
return redirect('/?filename=%s' % filename)
