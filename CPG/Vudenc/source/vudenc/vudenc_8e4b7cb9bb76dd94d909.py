import time
import math
from flask import request
from pyMetricServer import app
from pyMetricServer.system.database import database, getMetric
from werkzeug.exceptions import abort
from pyMetricServer.system.decorators import crossdomain
from flask.json import jsonify
@app.route('/metric/api/v1.0/metric/get')...
"""docstring"""
res = getMetric(request.args.get('fromtime', None), request.args.get(
    'totime', None), request.args.get('origin', None), request.args.get(
    'key', None), request.args.get('count', None), (request.args.get(
    'order', 'Time'), bool(request.args.get('desc', True))))
return jsonify({'results': res, 'resultcount': len(res)})
