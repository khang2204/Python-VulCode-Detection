@app.route('/openFile')...
if not 'email' in session and not 'social' in session:
if 'diagram' in request.args:
files = []
return redirect('/login?return_url=openFile&diagram=true')
return redirect('/login?return_url=openFile')
if 'email' in session:
email = session['email']
if 'social' in session:
userpath = os.path.join(app.config['UPLOAD_FOLDER'], email)
email = session['social']
files = os.listdir(userpath)
os.makedirs(userpath, exist_ok=True)
return render_template('openFile.html', files=files)
