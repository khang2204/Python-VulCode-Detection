@app.route('/data/slaves/')...
start_date, end_date = clean_date_params(request.args)
days_to_show = (end_date - start_date).days
if days_to_show <= 8:
jobs = 5
jobs = int(round(days_to_show * 0.4))
info = 'Only slaves with more than %d jobs are displayed.' % jobs
db = create_db_connnection()
cursor = db.cursor()
cursor.execute(
    """select slave, result, date from testjobs
                      where result in
                      ("retry", "testfailed", "success", "busted", "exception")
                      and date between "{0}" and "{1}"
                      order by date;"""
    .format(start_date, end_date))
query_results = cursor.fetchall()
cursor.close()
db.close()
if not query_results:
return
data = {}
labels = 'fail retry infra success total'.split()
summary = {result: (0) for result in labels}
summary['jobs_since_last_success'] = 0
dates = []
for name, result, date in query_results:
data.setdefault(name, summary.copy())
slave_list = [slave for slave in data if data[slave]['total'] > jobs]
data[name]['jobs_since_last_success'] += 1
for slave in slave_list:
if result == 'testfailed':
results = data[slave]
platforms = {}
data[name]['fail'] += 1
if result == 'retry':
fail_rates = calculate_fail_rate(results['success'], results['retry'],
    results['total'])
slaves = sorted(data.keys())
data[name]['total'] += 1
data[name]['retry'] += 1
if result == 'success':
data[slave]['sfr'] = fail_rates
for platform, slave_group in groupby(slaves, lambda x: x.rsplit('-', 1)[0]):
dates.append(date)
data[name]['success'] += 1
if result == 'busted' or result == 'exception':
slaves = list(slave_group)
for slave in data.keys():
data[name]['jobs_since_last_success'] = 0
data[name]['infra'] += 1
if not any(slave in slaves for slave in slave_list):
if slave not in slave_list:
return {'slaves': data, 'platforms': platforms, 'dates': get_date_range(
    dates), 'disclaimer': info}
platforms[platform] = {}
results = {}
for label in ['success', 'retry', 'total']:
r = reduce(lambda x, y: x + y, [data[slave][label] for slave in slaves])
fail_rates = calculate_fail_rate(results['success'], results['retry'],
    results['total'])
results[label] = r
platforms[platform].update(fail_rates)
