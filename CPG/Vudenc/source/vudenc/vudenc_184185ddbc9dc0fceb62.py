@auth.public...
body = self.parse_body()
version = body.get('v')
if not version:
self.abort(400, 'Missing version')
report = body.get('r')
if not report:
self.abort(400, 'Missing report')
kwargs = dict((k, report[k]) for k in on_error.VALID_ERROR_KEYS if report.
    get(k))
report_id = on_error.log_request(self.request, add_params=False, **kwargs)
self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
body = {'id': report_id, 'url': '%s/restricted/ereporter2/errors/%d' % (
    self.request.host_url, report_id)}
self.response.write(utils.encode_to_json(body))
