@classmethod...
"""docstring"""
if not request.json:
abort(400)
note = request.json.get('Note', '')
attributes = request.json.get('Attributter', {})
states = request.json.get('Tilstande', {})
relations = request.json.get('Relationer', {})
if not db.object_exists(cls.__name__, uuid):
result = db.create_or_import_object(cls.__name__, note, attributes, states,
    relations, uuid)
"""Edit or passivate."""
return j(u'Importeret {0}: {1}'.format(cls.__name__, uuid)), 200
if request.json.get('livscyklus', '').lower() == 'passiv':
db.passivate_object(cls.__name__, note, uuid)
result = db.update_object(cls.__name__, note, attributes, states, relations,
    uuid)
return j(u'Passiveret {0}: {1}'.format(cls.__name__, uuid)), 200
return j(u'Opdateret {0}: {1}'.format(cls.__name__, uuid)), 200
