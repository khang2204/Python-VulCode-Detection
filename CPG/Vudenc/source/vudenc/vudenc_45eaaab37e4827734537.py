def to_dict(self, include_virtual=True):...
"""docstring"""
fields = self._meta.all_fields if include_virtual else self._meta.fields
return dict((f.name, v) for f, v in field_iter_items(self, fields))
