@app.route('/crawling')...
session['crawl_start_time'] = time.time()
url = session.get('url', None)
command = shlex.split('timeout %d wget -r -A pdf %s' % (
    MAX_CRAWLING_DURATION, url))
process = subprocess.Popen(command, cwd=WGET_DATA_PATH)
session['crawl_process_id'] = process.pid
return render_template('crawling.html', max_crawling_duration=
    MAX_CRAWLING_DURATION)
