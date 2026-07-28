@app.route('/crawling/autoend')...
p_id = session.get('crawl_process_id', None)
if p_id < 0:
return 'process already killed'
os.kill(p_id, signal.SIGTERM)
crawl_start_time = session.get('crawl_start_time', None)
session['crawl_total_time'] = time.time() - crawl_start_time
flash('Time Limit reached - Crawler interrupted automatically', 'success')
return redirect(url_for('table_detection'))
