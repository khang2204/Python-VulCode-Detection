@app.route('/saveAs', methods=['POST'])...
if not 'email' in session and not 'social' in session:
return '', 401
name = fname if fname else request.form['filename']
if name:
if name[-4:] != '.pml':
flash('Invalid File')
name += '.pml'
if allowed_file(name):
return redirect('/saveAs')
session['currentFile'] = name
if 'email' in session:
email = session['email']
if 'social' in session:
savepath = os.path.join(app.config['UPLOAD_FOLDER'], email)
email = session['social']
os.makedirs(savepath, exist_ok=True)
saveFilePath = os.path.join(savepath, name)
tempFilePath = session.pop('tempFile', None)
if tempFilePath:
shutil.copy(tempFilePath, saveFilePath)
if 'diagram' in request.referrer or 'diagram' in request.args or 'diagram' in request.form:
return redirect('/diagram?filename=%s' % name)
return redirect('/?filename=%s' % name)
