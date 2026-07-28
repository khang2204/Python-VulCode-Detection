def get_updates(timeout, offset=None):...
url = '{}/getUpdates?timeout={}'.format(base_url, timeout)
if offset:
url += '&offset={}'.format(offset)
return get_json_from_url(url)
