@classmethod...
"""docstring"""
virkning_fra = request.args.get('virkningFra', None)
virkning_til = request.args.get('virkningTil', None)
registreret_fra = request.args.get('registreretFra', None)
registreret_til = request.args.get('registreretTil', None)
uuid = request.args.get('uuid', None)
if uuid is None:
uuid = []
uuid = uuid.split(',')
results = db.list_objects(cls.__name__, uuid, virkning_fra, virkning_til,
    registreret_fra, registreret_til)
if results is None:
results = []
return jsonify({'results': results})
