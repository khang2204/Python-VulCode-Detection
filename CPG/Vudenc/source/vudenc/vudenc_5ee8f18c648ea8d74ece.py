@app.route('/api/server/disconnect', methods=['PUT'])...
controller.indi_server.disconnect()
is_error = not timeout(5)(lambda : not controller.indi_server.is_connected())()
return notify('indi_server', 'indi_server_disconnect', controller.
    indi_server.to_map(), is_error)
