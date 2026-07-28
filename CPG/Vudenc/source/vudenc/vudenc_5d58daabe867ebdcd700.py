def _create_server(self, connector):...
cliq_args = {}
cliq_args['serverName'] = connector['host']
out = self._cliq_run_xml('getServerInfo', cliq_args, False)
response = out.find('response')
result = response.attrib.get('result')
if result != '0':
cliq_args = {}
cliq_args['serverName'] = connector['host']
cliq_args['initiator'] = connector['initiator']
self._cliq_run_xml('createServer', cliq_args)
