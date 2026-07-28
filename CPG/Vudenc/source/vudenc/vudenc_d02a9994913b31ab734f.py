def assert_call(verb, client_or_resource, url, verify=nsxlib_testcase....
nsx_client = client_or_resource
if getattr(nsx_client, 'client', None) is not None:
nsx_client = nsx_client.client
cluster = nsx_client._conn
if single_call:
cluster.assert_called_once(verb, **{'url': url, 'verify': verify, 'body':
    data, 'headers': headers, 'cert': None, 'timeout': timeout})
cluster.assert_any_call(verb, **{'url': url, 'verify': verify, 'body': data,
    'headers': headers, 'cert': None, 'timeout': timeout})
