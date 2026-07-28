@app.route('/data/platform/')...
platform = request.args.get('platform')
build_system_type = request.args.get('build_system_type')
start_date, end_date = clean_date_params(request.args)
log_message = 'platform: %s startDate: %s endDate: %s' % (platform,
    start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d'))
app.logger.debug(log_message)
db = create_db_connnection()
cursor = db.cursor()
query = (
    """select distinct revision from testjobs
                      where platform = '%s'
                      and branch = 'mozilla-central'
                      and date between '%s' and '%s'
                      and build_system_type='%s'
                      order by date desc;"""
     % (platform, start_date, end_date, build_system_type))
cursor.execute(query)
csets = cursor.fetchall()
cset_summaries = []
test_summaries = {}
dates = []
labels = 'green orange blue red'.split()
summary = {result: (0) for result in labels}
for cset in csets:
cset_id = cset[0]
cursor.close()
cset_summary = CSetSummary(cset_id)
db.close()
query = (
    """select result, testtype, date from testjobs
                   where platform='%s' and buildtype='opt' and revision='%s' and
                   build_system_type='%s' order by testtype"""
     % (platform, cset_id, build_system_type))
test_types = sorted(test_summaries.keys())
cursor.execute(query)
test_types += ['total', 'percentage']
test_results = cursor.fetchall()
total = Counter()
for res, testtype, date in test_results:
percentage = {}
test_summary = test_summaries.setdefault(testtype, summary.copy())
cset_summaries.append(cset_summary)
for test in test_summaries:
if res == 'success':
total.update(test_summaries[test])
test_count = sum(total.values())
cset_summary.green[testtype] += 1
if res == 'testfailed':
for key in total:
test_summary['green'] += 1
cset_summary.orange[testtype] += 1
if res == 'retry':
percentage[key] = round(100.0 * total[key] / test_count, 2)
fail_rates = calculate_fail_rate(passes=total['green'], retries=total[
    'blue'], totals=test_count)
dates.append(date)
test_summary['orange'] += 1
cset_summary.blue[testtype] += 1
if res == 'exception' or res == 'busted':
test_summaries['total'] = total
test_summary['blue'] += 1
cset_summary.red[testtype] += 1
if res == 'usercancel':
test_summaries['percentage'] = percentage
test_summary['red'] += 1
app.logger.debug('usercancel')
app.logger.debug('UNRECOGNIZED RESULT: %s' % res)
return {'testTypes': test_types, 'byRevision': cset_summaries, 'byTest':
    test_summaries, 'failRates': fail_rates, 'dates': get_date_range(dates)}
