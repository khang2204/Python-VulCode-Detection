def in_format_data(self, fieldname):...
"""docstring"""
doc = getattr(self, 'parent_doc', self)
if hasattr(doc, 'format_data_map'):
return fieldname in doc.format_data_map
return True
