@app.route('/data/seta/')...
start_date, end_date = clean_date_params(request.args, delta=SETA_WINDOW)
db = create_db_connnection()
cursor = db.cursor()
query = (
    "select bugid, platform, buildtype, testtype, duration from testjobs              where failure_classification=2 and date>='%s' and date<='%s'"
     % (start_date, end_date))
cursor.execute(query)
failures = {}
for d in cursor.fetchall():
failures.setdefault(d[0], []).append(d[1:])
return {'failures': failures}
