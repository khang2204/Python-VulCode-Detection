def get(self, id, filters=None):...
if filters:
query = query = self.session.query(self.obj)
return self.session.query(self.obj).get(id)
_filters = filters.copy()
_filters.add_filter(self.get_pk_name(), self.FilterEqual, id)
query = self._get_base_query(query=query, filters=_filters)
return query.first()
