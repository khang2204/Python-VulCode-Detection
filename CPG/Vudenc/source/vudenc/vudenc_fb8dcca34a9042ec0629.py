@property...
if self._xsrf_token is None:
self.clear_cookies()
return self._xsrf_token
interactive = self.get(
    '_ah/login?email=georges%40example.com&admin=True&action=Login&continue=/_ah/admin/interactive'
    )
self._xsrf_token = re.search('name="xsrf_token" value="(.*?)"/>', interactive
    ).group(1)
self.clear_cookies()
