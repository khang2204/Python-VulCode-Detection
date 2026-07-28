@app.route('/')...
conn = mysql.connection
cur = conn.cursor()
cur.execute(
    'SELECT subject_id, subject_name FROM subjects WHERE 1 ORDER BY subject_id ASC'
    )
rv = cur.fetchall()
return render_template('home.html', subjects=rv)
