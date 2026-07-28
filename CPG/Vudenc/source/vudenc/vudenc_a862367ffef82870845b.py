@staticmethod...
"""docstring"""
if isinstance(value, list):
return ','.join([(str(x) if x is not None else '') for x in value])
return str(value)
