@app.route('/crawling/end')...
p_id = session.get('crawl_process_id', None)
os.kill(p_id, signal.SIGTERM)
session['crawl_process_id'] = -1
crawl_start_time = session.get('crawl_start_time', None)
session['crawl_total_time'] = time.time() - crawl_start_time
flash('You successfully interrupted the crawler', 'success')
return render_template('end_crawling.html')
