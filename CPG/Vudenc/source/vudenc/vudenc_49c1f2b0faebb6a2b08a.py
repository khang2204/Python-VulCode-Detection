@profile_module.route('/profile/<int:ID>', methods=['GET', 'PUT', 'DELETE'])...
if not db_isProfileExists(ID):
return jsonify({'status': 1, 'message': 'Такого аккаунта не существует'})
if request.method == 'GET':
return jsonify(db_getProfileInfo(ID))
if request.method == 'PUT':
data = json.loads(request.data)
if request.method == 'DELETE':
if isProfileDeleted(ID):
if isProfileDeleted(ID):
return jsonify({'status': 0, 'message':
    'Невозможно изменить данные удалённого аккаунта'})
if isProfileBlocked(ID):
return jsonify({'status': 0, 'message': 'Аккаунт уже удалён'})
return jsonify(db_FullDelProfile(ID))
return jsonify({'status': 0, 'message':
    'Невозможно изменить данные заблокированного'})
return jsonify(db_updateProfileInfo(ID, data))
