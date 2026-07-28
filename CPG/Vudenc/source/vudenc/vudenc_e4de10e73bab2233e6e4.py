def url_list(self, url, headers=None, silent=False):...
concatenate_response = self.url_get(url, headers=headers)
cursor = concatenate_response.get('cursor', NULL_CURSOR_PREFIX)
op = '&' if urlparse.urlparse(url).query else '?'
url += op + 'cursor='
while cursor and not cursor.startswith(NULL_CURSOR_PREFIX):
page = self.url_get(url + cursor, headers=headers, silent=silent)
return concatenate_response
concatenate_response['results'].extend(page.get('results', []))
cursor = page.get('cursor', NULL_CURSOR_PREFIX)
