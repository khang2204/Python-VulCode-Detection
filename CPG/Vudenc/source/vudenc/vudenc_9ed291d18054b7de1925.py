@app.route('/update_comment/<pic_name>', methods=['POST', 'GET'])...
if request.method == 'POST':
query = (
    "UPDATE commentsTable\t\t\t\t\tSET comment = '%s'\t\t\t\t\tWHERE comment_id = '%s' "
     % (request.form['new_comment'], request.form['edit_value']))
return redirect(url_for('view_comment', pic_name=pic_name))
cursor.execute(query)
db.commit()
