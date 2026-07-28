def get_prep_value(self, value):...
if not value:
return None if self.null else b''
if isinstance(value, bytes):
return value
return pickle.dumps(value)
