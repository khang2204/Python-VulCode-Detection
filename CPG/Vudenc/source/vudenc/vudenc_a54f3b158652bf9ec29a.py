@addObs.route('/loadMailles', methods=['GET'])...
db = getConnexion()
sql = """ SELECT row_to_json(fc)
              FROM ( SELECT 
                'FeatureCollection' AS type, 
                array_to_json(array_agg(f)) AS features
                FROM(
                    SELECT 'Feature' AS type,
                   ST_ASGeoJSON(ST_TRANSFORM(m.geom,4326))::json As geometry,
                   row_to_json((SELECT l FROM(SELECT id_maille) AS l)) AS properties
                   FROM layers.maille_1_2 AS m WHERE m.taille_maille='1') AS f)
                AS fc; """
db.cur.execute(sql)
res = db.cur.fetchone()
db.closeAll()
return Response(flask.json.dumps(res), mimetype='application/json')
