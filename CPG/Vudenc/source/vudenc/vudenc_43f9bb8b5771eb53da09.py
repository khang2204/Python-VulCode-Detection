@property...
"""docstring"""
if self._parsed_status_test_usernames:
return self._parsed_status_test_usernames
value = self.config.get(self.section, 'status_test_usernames')
res = [x.strip() for x in value.split(',')]
self._parsed_status_test_usernames = res
return res
