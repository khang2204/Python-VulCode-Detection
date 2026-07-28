@app.route('/metric/api/v1.0/metric', methods=['POST'])...
if not request.json or not 'Origin' in request.json or not 'Key' in request.json or not 'Value' in request.json:
abort(400)
cursor = database.cursor()
cursor.execute(
    'INSERT INTO log_metric (Time, Origin, Key, Value) VALUES (%s,%s,%s,%s);',
    (time.time(), request.json['Origin'], request.json['Key'], request.json
    ['Value']))
cursor.close()
database.commit()
return "{'message': 'OK'}"
