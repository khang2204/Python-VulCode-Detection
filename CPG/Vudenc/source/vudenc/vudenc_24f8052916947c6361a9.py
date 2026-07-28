@app.route('/data/setadetails/')...
date = request.args.get('date', '')
active = request.args.get('active', 0)
buildbot = request.args.get('buildbot', 0)
branch = request.args.get('branch', '')
taskcluster = request.args.get('taskcluster', 0)
priority = request.args.get('priority', 'low')
jobnames = JOBSDATA.jobnames_query()
if date == '' or date == 'latest':
today = datetime.now()
db = create_db_connnection()
date = today.strftime('%Y-%m-%d')
cursor = db.cursor()
query = "select jobtype from seta where date='%s 00:00:00'" % date
cursor.execute(query)
retVal = {}
retVal[date] = []
jobtype = []
if (str(branch) in ['fx-team', 'mozilla-inbound', 'autoland']
abort(404)
for d in cursor.fetchall():
parts = d[0].split("'")
alljobs = JOBSDATA.jobtype_query()
jobtype.append([parts[1], parts[3], parts[5]])
if priority == 'low':
low_value_jobs = [low_value_job for low_value_job in alljobs if 
    low_value_job not in jobtype]
if active:
jobtype = low_value_jobs
active_jobs = []
if buildbot:
for job in alljobs:
active_jobs = []
if taskcluster:
found = False
jobtype = active_jobs
buildbot_jobs = [job for job in jobnames if job['buildplatform'] == 'buildbot']
active_jobs = []
retVal[date] = jobtype
for j in jobtype:
for job in jobtype:
taskcluster_jobs = [job for job in jobnames if job['buildplatform'] ==
    'taskcluster']
return {'jobtypes': retVal}
if j[0] == job[0] and j[1] == job[1] and j[2] == job[2]:
if not found:
for j in buildbot_jobs:
jobtype = active_jobs
for job in jobtype:
found = True
active_jobs.append(job)
if j['name'] == job[2] and j['platform'] == job[0] and j['buildtype'] == job[1
for j in taskcluster_jobs:
jobtype = active_jobs
active_jobs.append(j['ref_data_name'] if branch is 'mozilla-inbound' else j
    ['ref_data_name'].replace('mozilla-inbound', branch))
if j['name'] == job[2] and j['platform'] == job[0] and j['buildtype'] == job[1
active_jobs.append(j['ref_data_name'])
