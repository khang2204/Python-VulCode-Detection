def assert_json_call(self, method, client, url, headers=nsx_client....
cluster = client._conn
if data:
data = jsonutils.dumps(data, sort_keys=True)
cluster.assert_called_once(method, **{'url': url, 'verify': NSX_CERT,
    'body': data, 'headers': headers, 'cert': None, 'timeout': timeout})
