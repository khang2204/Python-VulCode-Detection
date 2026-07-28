@app.route('/data/results/flot/day/')...
"""docstring"""
start_date, end_date = clean_date_params(request.args)
platforms = ['android4.0', 'android2.3', 'linux32', 'winxp', 'win7', 'win8',
    'osx10.6', 'osx10.7', 'osx10.8']
db = create_db_connnection()
data_platforms = {}
for platform in platforms:
cursor = db.cursor()
db.close()
cursor.execute(
    """select DATE(date) as day,sum(result="%s") as failures,count(*) as
                          totals from testjobs where platform="%s" and date >= "%s" and date <= "%s"
                          group by day"""
     % ('testfailed', platform, start_date, end_date))
return data_platforms
query_results = cursor.fetchall()
dates = []
data = {}
data['failures'] = []
data['totals'] = []
for day, fail, total in query_results:
dates.append(day)
cursor.close()
timestamp = calendar.timegm(day.timetuple()) * 1000
data_platforms[platform] = {'data': data, 'dates': get_date_range(dates)}
data['failures'].append((timestamp, int(fail)))
data['totals'].append((timestamp, int(total)))
