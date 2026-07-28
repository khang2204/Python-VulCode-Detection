def filter(self, table, mappings, filter_string):...
"""docstring"""
q = filter_string.lower()
return [mapping for mapping in mappings if q in mapping.ud.lower()]
