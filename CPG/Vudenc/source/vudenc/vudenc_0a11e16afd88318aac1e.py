@addObs.route('/loadProtocoles', methods=['GET', 'POST'])...
db = getConnexion()
sql = (
    'SELECT array_to_json(array_agg(row_to_json(p))) FROM (SELECT * FROM synthese.bib_projet WHERE saisie_possible = TRUE) p'
    )
db.cur.execute(sql)
return Response(flask.json.dumps(db.cur.fetchone()[0]), mimetype=
    'application/json')
