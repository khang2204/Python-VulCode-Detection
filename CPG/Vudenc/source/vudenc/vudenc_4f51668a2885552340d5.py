@app.route('/statistics')...
cur = mysql.connection.cursor()
cur.execute(
    'SELECT cid FROM Crawls WHERE crawl_date = (SELECT max(crawl_date) FROM Crawls)'
    )
result = cur.fetchone()
cur.close()
if result:
cid_last_crawl = result['cid']
flash(
    'There are no statistics to display, please start a new query and wait for it to complete.'
    , 'danger')
return redirect(url_for('cid_statistics', cid=cid_last_crawl))
return redirect(url_for('index'))
