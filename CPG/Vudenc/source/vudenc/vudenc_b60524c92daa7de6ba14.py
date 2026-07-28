@property...
"""docstring"""
res = self.config.get(self.section, 'verify_request_signatures')
return bool(int(res))
