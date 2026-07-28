@endpoints.route('/ranks')...
if db == None:
init()
scene = request.args.get('scene', default='austin')
date = request.args.get('date')
if date == None:
sql = (
    "SELECT distinct date FROM ranks WHERE scene='{}' ORDER BY date DESC LIMIT 1;"
    .format(scene))
sql = "SELECT * FROM ranks WHERE scene = '{}' and date='{}'".format(scene, date
    )
res = db.exec(sql)
res = db.exec(sql)
date = res[0][0]
cur_ranks = {}
for r in res:
tag = r[1]
y, m, d = date.split('-')
rank = r[2]
prev_date = bracket_utils.get_previous_month(date)
cur_ranks[tag] = rank
sql = "SELECT * FROM ranks WHERE scene = '{}' and date='{}'".format(scene,
    prev_date)
res = db.exec(sql)
prev_ranks = {}
for r in res:
tag = r[1]
return render_template('libraries/html/ranks.html', cur_ranks=cur_ranks,
    prev_ranks=prev_ranks, scene=scene, date=date)
rank = r[2]
prev_ranks[tag] = rank
