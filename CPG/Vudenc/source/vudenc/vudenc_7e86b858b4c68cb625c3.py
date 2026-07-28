@app.route('/')...
query = 'SELECT img_path, img_name\t\t\tFROM imageTable'
cursor.execute(query)
return render_template('index.html', images=cursor)
