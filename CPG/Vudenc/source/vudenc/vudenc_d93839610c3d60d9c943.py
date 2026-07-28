@app.route('/dashboard')...
cur = mysql.connection.cursor()
result = cur.execute(
    'SELECT cid, crawl_date, pdf_crawled, pdf_processed, domain, url FROM Crawls'
    )
crawls = cur.fetchall()
if result > 0:
return render_template('dashboard.html', crawls=crawls)
msg = 'No Crawls Found'
return render_template('dashboard.html', msg=msg)
