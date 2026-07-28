@app.route('/api/server/connect', methods=['PUT'])...
controller.indi_server.connect()
is_error = not timeout(5)(controller.indi_server.is_connected)()
return notify('indi_server', 'indi_server_connect', controller.indi_server.
    to_map(), is_error)
