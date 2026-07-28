@app.route('/submit_comment/<pic_name>', methods=['POST', 'GET'])...
if request.method == 'POST':
query = (
    "INSERT INTO commentsTable(comment, img_name)\t\t\t\tVALUES('%s', '%s')" %
    (request.form['comment'], request.form['image-name']))
cursor.execute(query)
db.commit()
return redirect(url_for('view_comment', pic_name=pic_name))
