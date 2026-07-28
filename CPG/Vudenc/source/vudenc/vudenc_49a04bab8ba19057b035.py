def _get_item(self, klass, key, object_name):...
assert self.dbsession is not None, 'Missing dbsession'
dbsession = self.dbsession()
obj = dbsession.query(klass).options(undefer_group('edit')).filter(getattr(
    klass, self.id_key) == key).scalar()
if obj is None:
obj.__name__ = object_name
return obj
