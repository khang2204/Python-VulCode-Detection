@addObs.route('/submit/', methods=['POST'])...
db = getConnexion()
if flask.request.method == 'POST':
observateur = flask.request.json['general']['observateur']
return Response(flask.json.dumps('success'), mimetype='application/json')
cd_nom = flask.request.json['general']['taxon']['cd_ref']
loc_exact = flask.request.json['general']['loc_exact']
code_maille = str()
loc = flask.request.json['general']['coord']
x = str(loc['lng'])
y = str(loc['lat'])
point = 'POINT(' + x + ' ' + y + ')'
code_maille = flask.request.json['general']['code_maille']
date = flask.request.json['general']['date']
commentaire = flask.request.json['general']['commentaire']
comm_loc = flask.request.json['general']['comm_loc']
protocoleObject = flask.request.json['protocole']
fullTableName = protocoleObject['nom_schema'] + '.' + protocoleObject[
    'nom_table']
protocoleName = protocoleObject['nom_table']
id_projet = protocoleObject['id_projet']
centroid = None
if not loc_exact:
point = None
sql_foret = (
    ' SELECT ccod_frt FROM layers.perimetre_forets WHERE ST_INTERSECTS(geom,(ST_Transform(ST_GeomFromText(%s, 4326),%s)))'
    )
sql = (
    'SELECT ST_AsText(ST_Centroid(ST_TRANSFORM(geom, 4326))) FROM layers.maille_1_2 WHERE id_maille = %s '
    )
if loc_exact:
params = [code_maille]
params = [point, config['MAP']['PROJECTION']]
params = [centroid, config['MAP']['PROJECTION']]
db.cur.execute(sql, params)
db.cur.execute(sql_foret, params)
res = db.cur.fetchone()
res = db.cur.fetchone()
if res != None:
ccod_frt = None
centroid = res[0]
if res != None:
ccod_frt = res[0]
sql_insee = (
    ' SELECT code_insee FROM layers.commune WHERE ST_INTERSECTS(geom,(ST_Transform(ST_GeomFromText(%s, 4326),%s)))'
    )
if loc_exact:
params = [point, config['MAP']['PROJECTION']]
params = [centroid, config['MAP']['PROJECTION']]
db.cur.execute(sql_insee, params)
res = db.cur.fetchone()
insee = None
if res != None:
insee = res[0]
id_structure = session['id_structure']
valide = False
generalValues = [id_projet, observateur, date, cd_nom, point, insee,
    commentaire, valide, ccod_frt, loc_exact, code_maille, id_structure,
    comm_loc]
stringInsert = ('INSERT INTO ' + fullTableName +
    '(id_projet, observateur, date, cd_nom, geom_point, insee, commentaire, valide, ccod_frt, loc_exact, code_maille, id_structure, comm_loc'
    )
stringValues = ''
if loc_exact:
stringValues = (
    'VALUES (%s, %s, %s, %s,  ST_Transform(ST_PointFromText(%s, 4326),' +
    str(config['MAP']['PROJECTION']) + '), %s, %s, %s, %s, %s, %s, %s, %s')
stringValues = 'VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s'
keys = getParmeters()['keys']
values = getParmeters()['values']
for k in keys:
stringInsert += ', ' + k
stringInsert += ')'
stringValues += ', %s'
stringValues += ')'
for v in values:
generalValues.append(v)
params = generalValues
sql = stringInsert + stringValues
db.cur.execute(sql, params)
db.conn.commit()
db.closeAll()
