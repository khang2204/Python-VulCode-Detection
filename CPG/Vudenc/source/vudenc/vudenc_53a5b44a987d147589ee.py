def get_bracket_placings_in_scene(db, scene, tag):...
sql = (
    "select distinct matches.date, placings.place from placings join matches on             matches.url=placings.url where scene='{}' and ((player1='{}' and placings.player=player1) or             (player2='{}' and placings.player=player2));"
    .format(scene, tag, tag))
print(sql)
res = db.exec(sql)
res = [[r[0], int(r[1])] for r in res]
return res
