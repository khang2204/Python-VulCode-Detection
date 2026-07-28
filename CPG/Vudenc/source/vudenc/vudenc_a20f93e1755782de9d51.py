@app.route('/delete_comment/<pic_name>', methods=['POST', 'GET'])...
if request.method == 'POST':
query = ("DELETE FROM commentsTable\t\t\t\tWHERE comment_id = '%s'" %
    request.form['delete_comment'])
cursor.execute(query)
db.commit()
return redirect(url_for('view_comment', pic_name=pic_name))
