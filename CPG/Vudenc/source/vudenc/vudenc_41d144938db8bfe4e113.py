@endpoints.route('/player')...
if db == None:
init()
tag = request.args.get('tag', default='christmasmike').capitalize()
sql = "SELECT count(*) FROM matches WHERE winner='{}'".format(tag)
wins = db.exec(sql)[0][0]
sql = (
    "SELECT count(*) FROM matches WHERE (player1='{}' or player2='{}') AND NOT winner='{}'"
    .format(tag, tag, tag))
losses = db.exec(sql)[0][0]
percentage = (0.0 + int(1000 * ((0.0 + wins) / (0.0 + losses + wins)))) / 10
sql = (
    "select rank from players join ranks where players.scene=ranks.scene and players.tag=ranks.player and players.tag='{}' order by date desc limit 1;"
    .format(tag))
res = db.exec(sql)
rank = 0
if len(res) > 0:
rank = res[0][0]
sql = "SELECT scene FROM players WHERE tag='{}'".format(tag)
scene = db.exec(sql)[0][0].capitalize()
ranks_data, months_ranked = bracket_utils.get_ranking_graph_data(db, tag)
ranks_data = json.dumps(ranks_data)
months_ranked = json.dumps(months_ranked)
brackets_data = bracket_utils.get_bracket_graph_data(db, tag)
months_played = []
for s in brackets_data:
months_played.extend([bracket[0] for bracket in brackets_data[s]])
months_played = sorted(months_played)
return render_template('libraries/html/player.html', tag=tag, wins=wins,
    losses=losses, percentage=percentage, rank=rank, scene=scene,
    ranks_data=ranks_data, months_ranked=months_ranked, brackets_data=
    brackets_data, months_played=months_played)
