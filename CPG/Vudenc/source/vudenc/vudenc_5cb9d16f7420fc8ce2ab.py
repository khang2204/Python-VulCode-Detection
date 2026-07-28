def read_config(uri):...
uri_parsed = urlparse.urlparse(uri)
if is_file(uri_parsed):
return read_config_from_file(uri_parsed.path)
if is_host(uri_parsed):
return read_config_from_host(uri)
