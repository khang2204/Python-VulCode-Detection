from flask import Blueprint, request, jsonify
from modules.ProfileManager.api.db_methods import db_delProfile, db_getProfileInfo, db_getProfilesInfo, db_updateProfileInfo
from modules.ProfileManager.api.db_methods import db_FullDelProfile, db_isProfileExists
from modules.ProfileManager.api.functions import isProfileDeleted, isProfileBlocked
import json
profile_module = Blueprint('profile', __name__)
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
@profile_module.route('/profiles')...
return jsonify({'status': 0, 'message':
    'Невозможно изменить данные удалённого аккаунта'})
if isProfileBlocked(ID):
return jsonify({'status': 0, 'message': 'Аккаунт уже удалён'})
return jsonify(db_FullDelProfile(ID))
return jsonify(db_getProfilesInfo())
return jsonify({'status': 0, 'message':
    'Невозможно изменить данные заблокированного'})
return jsonify(db_updateProfileInfo(ID, data))
