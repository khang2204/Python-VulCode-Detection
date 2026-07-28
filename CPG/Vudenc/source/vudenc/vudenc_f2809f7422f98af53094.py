@app.route('/api/settings', methods=['PUT'])...
controller.settings.update(json)
updated_settings = controller.settings.to_map()
return dict([setting for setting in updated_settings.items() if setting[0] in
    json])
