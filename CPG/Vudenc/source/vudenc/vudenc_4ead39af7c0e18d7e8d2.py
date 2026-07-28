def get(self):...
params = {'message': '', 'title': 'Config: Chrome Infra Monitoring Proxy'}
data = common.MonAcqData.get_by_id(common.CONFIG_DATA_KEY)
if data:
self.setParams(params, data)
self.render_response('set_credentials.html', **params)
