from base import Field
from primaryKeyField import PrimaryKeyField
from referenceField import ReferenceField
def __init__(self, rel_model, reference=None, related_name=None, on_delete=...
super(ForeignKeyField, self).__init__(*args, **kwargs)
self.rel_model = rel_model
self.reference = reference or rel_model._meta.fields['id']
self.related_name = related_name
self.on_delete = on_delete
self.on_update = on_update
def add_to_model(self, model_class, name):...
self.name = name
self.model_class = model_class
self.related_name = self.related_name or '%ss' % model_class._meta.name
model_class._meta.add_field(self)
if self.related_name in self.rel_model._meta.fields:
print('ERROR: Foreign key conflict')
if self.related_name in self.rel_model._meta.reverse_rel:
print('ERROR: Foreign key %s already exists on model %s' % (self.
    related_name, model_class._meta.name))
self.model_class._meta.rel[self.name] = self
self.model_class._meta.rel_class[self.rel_model] = self
reference = ReferenceField(self.model_class)
reference.add_to_model(self.rel_model, self.related_name, self.name)
def create_field(self, name):...
_type = self.reference.get_db_field()
field_string = '%s %s REFERENCES %s(%s)' % (self.name, _type, self.
    rel_model._meta.table_name, self.reference.name)
if self.on_delete:
field_string += ' ON DELETE CASCADE'
if self.on_update:
field_string += ' ON UPDATE CASCADE'
if self.unique:
field_string += ' UNIQUE'
return field_string
