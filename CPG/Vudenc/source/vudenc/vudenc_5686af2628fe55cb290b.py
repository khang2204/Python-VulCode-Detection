def get_last_ranked_month(db, scene, player):...
sql = (
    "select date from ranks where scene='{}' and player='{}' order by date desc limit 1;"
    .format(scene, player))
res = db.exec(sql)
date = res[0][0]
return date
