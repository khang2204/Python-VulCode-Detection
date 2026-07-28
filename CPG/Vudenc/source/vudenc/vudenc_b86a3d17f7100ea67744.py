def get_last_month(db, scene):...
sql = ("select date from matches where scene='{}' order by date desc limit 1;"
    .format(scene))
res = db.exec(sql)
date = res[0][0]
today = datetime.datetime.today().strftime('%Y-%m-%d')
y, m, d = today.split('-')
cy, cm, cd = date.split('-')
if y > cy or m > cm:
date = get_next_month(date)
return date
