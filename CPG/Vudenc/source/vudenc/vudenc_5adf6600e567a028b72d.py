@app.route('/api/indi_profiles/<id>', methods=['PUT'])...
updated_profile = None
profile.update(json)
updated_profile = profile.to_map()
return updated_profile
