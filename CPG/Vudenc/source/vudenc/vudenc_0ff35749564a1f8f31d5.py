@app.route('/api/server/devices/<device>/properties/<property_name>',...
app.logger.debug('update property: {}/{} ({})'.format(device, property_name,
    json))
indi_property = controller.indi_server.property(device=device, name=
    property_name)
return {'action': 'set_property', 'device': device, 'property':
    property_name, 'values': json, 'result': indi_property.set_values(json)}
