@app.route('/<pic_name>')...
query = 'SELECT comment, comment_id, img_name\t\t\tFROM commentsTable'
cursor.execute(query)
return render_template('static_page.html', names=cursor, pic_name=pic_name)
