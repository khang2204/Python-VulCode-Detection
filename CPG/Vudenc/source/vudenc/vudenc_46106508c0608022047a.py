def extract_key_from_nested_dict(self, target_dict, key):...
"""docstring"""
assert isinstance(target_dict, dict)
assert isinstance(key, str) and key
for k, v in target_dict.items():
if k == key:
yield v
if isinstance(v, dict):
for item in self.extract_key_from_nested_dict(v):
yield item
