@endpoints.route('/matches_at_date')...
if db == None:
init()
tag = request.args.get('tag', default=None)
date = request.args.get('date', default=None)
if tag and date:
y, m, d = date.split('-')
return ''
previous_m = '12' if m == '01' else str(int(m) - 1)
previous_m = previous_m.zfill(2)
previous_y = str(int(y) - 1) if m == '01' else y
previous_date = '{}-{}-{}'.format(previous_y, previous_m, d)
sql = (
    "select * from matches where (player1='{}' or player2='{}') and date<='{}' and date>='{}'"
    .format(tag, tag, date, previous_date))
data = db.exec(sql)
return json.dumps(data)
