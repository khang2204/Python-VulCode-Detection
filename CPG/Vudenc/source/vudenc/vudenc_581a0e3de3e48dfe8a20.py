def wrap_list_response(self, data):...
"""docstring"""
response = OrderedDict(((self.objects_key, data[1]), ('total_entries', self
    .session.query(func.count(self.resource_type.id)).scalar()), (
    'filtered_entries', data[0])))
full_response = self._add_meta_props(response)
return full_response
