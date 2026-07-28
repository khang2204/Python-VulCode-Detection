def player_in_url(db, player, urls):...
sql = "SELECT * FROM matches WHERE (player1='{}' or player2='{}')".format(
    player, player, urls)
if len(urls) > 0:
sql = sql + " and (url='{}'".format(urls[0])
res = db.exec(sql)
for url in urls[1:]:
if len(res) > 0:
sql = sql + " or url='{}'".format(url)
sql = sql + ');'
return True
LOG.info('player {} is not in {}'.format(player, urls))
return False
