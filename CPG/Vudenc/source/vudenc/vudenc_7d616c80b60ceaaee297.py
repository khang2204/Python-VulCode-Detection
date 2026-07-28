def __init__(self, connection, url_prefix=None, default_headers=None,...
if client_obj:
self.nsx_api_managers = client_obj.nsx_api_managers or []
self.nsx_api_managers = nsx_api_managers or []
self.max_attempts = client_obj.max_attempts
self.max_attempts = max_attempts
url_prefix = url_prefix or url_path_base
if url_prefix and url_path_base not in url_prefix:
if url_prefix.startswith('http'):
self.max_attempts = max_attempts
url_prefix += '/' + url_path_base
url_prefix = '%s/%s' % (url_path_base, url_prefix or '')
super(NSX3Client, self).__init__(connection, url_prefix=url_prefix,
    default_headers=default_headers, client_obj=client_obj)
