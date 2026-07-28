def post(self):...
params = {'message': '', 'title': 'Config: Chrome Infra Monitoring Proxy'}
data = common.MonAcqData.get_or_insert(common.CONFIG_DATA_KEY)
self.setParams(params, data)
updated_fields = False
failed_fields = []
for field, parser in self._parsers.iteritems():
if not self.request.get(field):
if failed_fields:
setattr(data, field, parser(self.request.get(field)))
failed_fields.append(field)
params[field] = self.request.get(field)
params['message'] = 'Failed to update %s. Please try again.' % ', '.join(
    failed_fields)
if updated_fields:
updated_fields = True
self.render_response('set_credentials.html', **params)
data.put()
self.setParams(params, data)
params['message'] = 'Updated configuration.'
logging.info('Updated configuration: %r', data)
