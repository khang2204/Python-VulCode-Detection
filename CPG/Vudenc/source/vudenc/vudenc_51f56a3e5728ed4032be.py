@app.route('/delete_crawl', methods=['POST'])...
cid = request.form['cid']
cur = mysql.connection.cursor()
result = cur.execute('DELETE FROM Crawls WHERE cid = %s' % cid)
mysql.connection.commit()
cur.close()
flash('Crawl successfully removed', 'success')
return redirect(url_for('dashboard'))
