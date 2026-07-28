@app.route('/statistics/<int:cid>')...
cur = mysql.connection.cursor()
result = cur.execute('SELECT * FROM Crawls WHERE cid = %s' % cid)
crawl = cur.fetchall()[0]
cur.close()
print(session.get('stats', None))
print(crawl['stats'])
json_stats = json.loads(crawl['stats'])
json_hierarchy = json.loads(crawl['hierarchy'])
stats_items = json_stats.items()
n_tables = sum([subdict['n_tables_pages'] for filename, subdict in stats_items]
    )
n_rows = sum([subdict['n_table_rows'] for filename, subdict in stats_items])
medium_tables = sum([subdict['table_sizes']['medium'] for filename, subdict in
    stats_items])
small_tables = sum([subdict['table_sizes']['small'] for filename, subdict in
    stats_items])
large_tables = sum([subdict['table_sizes']['large'] for filename, subdict in
    stats_items])
creation_dates_pdf = [subdict['creation_date'] for filename, subdict in
    stats_items]
creation_dates = list(map(lambda str: pdf_date_format_to_datetime(str),
    creation_dates_pdf))
if len(creation_dates) > 0:
oldest_pdf = min(creation_dates)
oldest_pdf = 'None'
most_recent_pdf = max(creation_dates)
most_recent_pdf = 'None'
return render_template('statistics.html', n_files=crawl['pdf_crawled'],
    n_success=crawl['pdf_processed'], n_tables=n_tables, n_rows=n_rows,
    n_errors=crawl['process_errors'], domain=crawl['domain'], small_tables=
    small_tables, medium_tables=medium_tables, large_tables=large_tables,
    stats=json_stats, hierarchy=json_hierarchy, end_time=crawl['crawl_date'
    ], crawl_total_time=round(crawl['crawl_total_time'] / 60.0, 1),
    proc_total_time=round(crawl['proc_total_time'] / 60.0, 1), oldest_pdf=
    oldest_pdf, most_recent_pdf=most_recent_pdf)
