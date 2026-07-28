def __init__(self, connection, url_prefix=None, default_headers=None,...
super(JSONRESTClient, self).__init__(connection, url_prefix=url_prefix,
    default_headers=RESTClient.merge_headers(JSONRESTClient.
    _DEFAULT_HEADERS, default_headers), client_obj=None)
