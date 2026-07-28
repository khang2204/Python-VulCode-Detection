@classmethod...
note = request.json.get('Note', '')
class_name = cls.__name__
result = db.delete_object(class_name, note, uuid)
return j('Slettet {0}: {1}'.format(class_name, uuid)), 200
