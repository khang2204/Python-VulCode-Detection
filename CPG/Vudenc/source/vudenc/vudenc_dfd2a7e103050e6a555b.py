@addObs.route('/search_taxon_name/<table>/<expr>', methods=['GET'])...
db = getConnexion()
sql = """ SELECT array_to_json(array_agg(row_to_json(r))) FROM(
                SELECT cd_ref, search_name, nom_valide from taxonomie.taxons_""" + table + """
                WHERE search_name ILIKE %s  
                ORDER BY search_name ASC 
                LIMIT 20) r"""
params = ['%' + expr + '%']
db.cur.execute(sql, params)
res = db.cur.fetchone()[0]
db.closeAll()
return Response(flask.json.dumps(res), mimetype='application/json')
