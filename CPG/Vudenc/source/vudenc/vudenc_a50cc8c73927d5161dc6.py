@locations.route('/autocomplete', methods=['GET'])...
conn = mysql.get_db()
location_objects = []
city_cur = conn.cursor()
city_cur.execute(
    'SELECT cities.name, id AS city_id, region_id, country_id FROM cities WHERE cities.name REGEXP %s LIMIT 100'
    , (request.args['input_text'],))
location_objects.extend(convert_objects(city_cur.fetchall(), city_cur.
    description))
if len(location_objects) == 100:
return make_response(jsonify(location_objects), HTTPStatus.OK)
region_cur = conn.cursor()
region_cur.execute(
    "SELECT regions.name, 'null' AS city_id, id AS region_id, country_id FROM regions WHERE regions.name REGEXP %s LIMIT 100"
    , (request.args['input_text'],))
location_objects.extend(convert_objects(region_cur.fetchall(), region_cur.
    description))
if len(location_objects) == 100:
return make_response(jsonify(location_objects), HTTPStatus.OK)
country_cur = conn.cursor()
country_cur.execute(
    "SELECT countries.name, 'null' AS city_id, 'null' AS region_id, id AS country_id FROM countries WHERE countries.name REGEXP %s LIMIT 100"
    , (request.args['input_text'],))
location_objects.extend(convert_objects(country_cur.fetchall(), country_cur
    .description))
return make_response(jsonify(location_objects), HTTPStatus.OK)
