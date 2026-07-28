def __init__(self, obj, session=None):...
_include_filters(self)
self.list_columns = dict()
self.list_properties = dict()
self.session = session
for prop in sa.orm.class_mapper(obj).iterate_properties:
if type(prop) != SynonymProperty:
for col_name in obj.__mapper__.columns.keys():
self.list_properties[prop.key] = prop
if col_name in self.list_properties:
super(SQLAInterface, self).__init__(obj)
self.list_columns[col_name] = obj.__mapper__.columns[col_name]
