@app.route('/upload_file', methods=['POST', 'GET'])...
if request.method == 'POST':
f = request.files['image_upload']
f.save('/home/pr0phet/MyProjects/Web/static/' + f.filename)
query = (
    "INSERT INTO imageTable(img_path, img_name)\t\t\t\tVALUES('%s', '%s')" %
    ('/static/' + f.filename, f.filename))
cursor.execute(query)
db.commit()
return redirect(url_for('index'))
