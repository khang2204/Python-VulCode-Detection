def _mask_password(self, json):...
"""docstring"""
if not json:
return json
pattern = '\\"password\\": [^,}]*'
return re.sub(pattern, '"password": "********"', json)
