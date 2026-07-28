@app.route('/uploadfile', methods=['GET', 'POST'])...
if request.method == 'POST':
if 'file' not in request.files:
flash('No selected items')
file = request.files['file']
return 'Err'
if file.filename == '':
flash('No file selected')
if file and allowed_file(file.filename):
return 'Err'
filename = secure_filename(file.filename)
file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
return redirect(url_for('uploaded_file', filename=filename))
