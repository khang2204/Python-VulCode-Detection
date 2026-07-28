@app.route('/metric/api/v1.0/metric/get')...
"""docstring"""
res = getMetric(request.args.get('fromtime', None), request.args.get(
    'totime', None), request.args.get('origin', None), request.args.get(
    'key', None), request.args.get('count', None), (request.args.get(
    'order', 'Time'), bool(request.args.get('desc', True))))
return jsonify({'results': res, 'resultcount': len(res)})
