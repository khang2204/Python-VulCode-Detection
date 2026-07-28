def __new__(cls, name, bases, attrs):...
super_new = super(ResourceBase, cls).__new__
if name == 'NewBase' and attrs == {}:
return super_new(cls, name, bases, attrs)
parents = [b for b in bases if isinstance(b, ResourceBase) and not (b.
    __name__ == 'NewBase' and b.__mro__ == (b, object))]
if not parents:
return super_new(cls, name, bases, attrs)
module = attrs.pop('__module__')
new_class = super_new(cls, name, bases, {'__module__': module})
attr_meta = attrs.pop('Meta', None)
abstract = getattr(attr_meta, 'abstract', False)
if not attr_meta:
meta = getattr(new_class, 'Meta', None)
meta = attr_meta
base_meta = getattr(new_class, '_meta', None)
new_class.add_to_class('_meta', ResourceOptions(meta))
if new_class._meta.name_space is NOT_PROVIDED and base_meta:
if not new_class._meta.name_space or new_class._meta.name_space is NOT_PROVIDED:
if new_class._meta.name_space is NOT_PROVIDED:
new_class._meta.name_space = base_meta.name_space
new_class._meta.name_space = module
r = registration.get_resource(new_class._meta.resource_name)
if r is not None:
return r
for obj_name, obj in attrs.items():
new_class.add_to_class(obj_name, obj)
new_class._meta.fields = sorted(new_class._meta.fields, key=hash)
local_field_attnames = set([f.attname for f in new_class._meta.fields])
field_attnames = set(local_field_attnames)
for base in parents:
if not hasattr(base, '_meta'):
if new_class._meta.key_field is not None:
for field in base._meta.all_fields:
if new_class._meta.key_field not in field_attnames:
if abstract:
if field.attname in local_field_attnames:
for field in base._meta.fields:
return new_class
registration.register_resources(new_class)
if field.attname not in field_attnames:
for field in base._meta.virtual_fields:
return registration.get_resource(new_class._meta.resource_name)
field_attnames.add(field.attname)
new_class.add_to_class(field.attname, copy.deepcopy(field))
new_class._meta.parents += base._meta.parents
new_class.add_to_class(field.attname, copy.deepcopy(field))
new_class._meta.parents.append(base)
