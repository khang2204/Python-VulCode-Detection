@endpoints.route('/losses')...
if db == None:
init()
player = request.args.get('tag', default='christmasmike')
sql = "SELECT * FROM matches WHERE (player1 = '" + str(player
    ) + "' OR " + "player2 = '" + str(player) + "') AND winner != '" + str(
    player) + "' ORDER BY date DESC;"
result = db.exec(sql)
result = [str(x) for x in result]
return json.dumps('\n'.join(result))
