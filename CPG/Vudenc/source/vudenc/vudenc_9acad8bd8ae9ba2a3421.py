def get_db_prep_value(self, value, connection, prepared=False):...
"""docstring"""
if value is None and self.null:
return None
while isinstance(value, str):
return json_encode(value, cls=self.encoder, sort_keys=True)
value = json_decode(value)
