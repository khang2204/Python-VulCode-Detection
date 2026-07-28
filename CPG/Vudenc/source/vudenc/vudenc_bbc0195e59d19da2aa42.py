@app.route('/data/dailyjobs/')...
start_date, end_date = clean_date_params(request.args)
db = create_db_connnection()
cursor = db.cursor()
query = (
    "select date, platform, branch, numpushes, numjobs, sumduration from dailyjobs              where date>='%s' and date <='%s'             order by case platform                 when 'linux' then 1                 when 'osx' then 2                  when 'win' then 3                  when 'android' then 4                 end"
     % (start_date, end_date))
cursor.execute(query)
output = {}
for rows in cursor.fetchall():
date = str(rows[0])
return {'dailyjobs': output}
platform = rows[1]
branch = rows[2]
numpushes = int(rows[3])
numjobs = int(rows[4])
sumduration = int(rows[5])
if date not in output:
output[date] = {'mozilla-inbound': [], 'fx-team': [], 'try': [], 'autoland': []
    }
if 'mozilla-inbound' in branch:
output[date]['mozilla-inbound'].append([platform, numpushes, numjobs,
    sumduration])
if 'fx-team' in branch:
output[date]['fx-team'].append([platform, numpushes, numjobs, sumduration])
if 'try' in branch:
output[date]['try'].append([platform, numpushes, numjobs, sumduration])
if 'autoland' in branch:
output[date]['autoland'].append([platform, numpushes, numjobs, sumduration])
