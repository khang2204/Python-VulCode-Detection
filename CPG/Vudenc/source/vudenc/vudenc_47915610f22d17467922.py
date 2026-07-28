@endpoints.route('/entrants')...
if db == None:
init()
sql = 'SELECT base_url FROM analyzed;'
urls = db.exec(sql, debug=False)
if players == None:
players = []
for p in players:
for p in request.args:
or_clause = "url = '{}' ".format(urls[0][0]) + ' '.join(["OR url = '{}'".
    format(url[0]) for url in urls[1:]])
return json.dumps(urls)
players.append(request.args[p])
sql = (
    "SELECT url, min(scene) scene, min(display_name) display_name, min(date) date FROM matches                 WHERE (player1='{}' or player2='{}') AND ({}) GROUP BY url ORDER BY date DESC;"
    .format(p, p, or_clause))
urls = db.exec(sql)
if len(urls) == 0:
return json.dumps([])
