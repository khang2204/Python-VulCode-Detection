@app.route('/metric/api/v1.0/metric/current')...
res = getMetric(request.args.get('fromtime', None), request.args.get(
    'totime', None), request.args.get('origin', None), request.args.get(
    'key', None), 1, ('Time', True))
return jsonify({'results': res, 'resultcount': len(res)})
