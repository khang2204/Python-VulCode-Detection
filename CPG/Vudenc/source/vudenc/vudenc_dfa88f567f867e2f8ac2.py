@app.route('/processing')...
proc_start_time = time.time()
domain = session.get('domain', None)
if domain == None:
path = 'data/%s' % (domain,)
hierarchy_dict = path_dict(path)
hierarchy_json = json.dumps(hierarchy_dict, sort_keys=True, indent=4)
n_files = path_number_of_files(path)
session['n_files'] = n_files
stats, n_error, n_success = pdf_stats(path, PDF_TO_PROCESS)
session['n_error'] = n_error
session['n_success'] = n_success
stats_json = json.dumps(stats, sort_keys=True, indent=4)
session['stats'] = stats_json
proc_over_time = time.time()
proc_total_time = proc_over_time - proc_start_time
cur = mysql.connection.cursor()
cur.execute(
    'INSERT INTO Crawls(cid, crawl_date, pdf_crawled, pdf_processed, process_errors, domain, url, hierarchy, stats, crawl_total_time, proc_total_time) VALUES(NULL, NULL, %s ,%s, %s, %s, %s, %s, %s, %s, %s)'
    , (n_files, n_success, n_error, domain, session.get('url', None),
    hierarchy_json, stats_json, session.get('crawl_total_time', None),
    proc_total_time))
mysql.connection.commit()
cur.close()
return render_template('processing.html', n_files=n_success, domain=domain,
    cid=0)
