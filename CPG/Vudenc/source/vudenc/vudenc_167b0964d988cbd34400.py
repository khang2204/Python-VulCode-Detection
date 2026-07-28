@app.route('/api/indi_profiles/<id>', methods=['DELETE'])...
indi_profile = controller.indi_profiles.lookup(id)
indi_profile_json = indi_profile.to_map()
indi_profile_json.update({'status': 'deleted'})
controller.indi_profiles.remove(indi_profile)
return indi_profile_json
