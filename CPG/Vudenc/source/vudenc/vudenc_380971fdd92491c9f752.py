@classmethod...
"""docstring"""
if not request.json:
abort(400)
note = request.json.get('Note', '')
attributes = request.json.get('Attributter', {})
states = request.json.get('Tilstande', {})
relations = request.json.get('Relationer', {})
uuid = db.create_or_import_object(cls.__name__, note, attributes, states,
    relations)
return jsonify({'uuid': uuid}), 201
