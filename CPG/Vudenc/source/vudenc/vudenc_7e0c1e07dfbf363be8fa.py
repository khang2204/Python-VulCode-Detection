def get_n_tournaments_before_date(db, scene, date, limit):...
sql = (
    "select url, date from matches where scene='{}' and date<='{}' group by url, date order by date desc limit {};"
    .format(scene, date, limit))
res = db.exec(sql)
urls = [r[0] for r in res]
return urls, date
