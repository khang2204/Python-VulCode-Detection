def create_resource_from_dict(d, resource=None, full_clean=True, copy_dict=True...
"""docstring"""
assert isinstance(d, dict)
if copy_dict:
d = d.copy()
if resource:
resource_type = None
document_resource_name = d.pop(DEFAULT_TYPE_FIELD, None)
if isinstance(resource, (tuple, list)):
if not document_resource_name:
resources = (resolve_resource_type(r) for r in resource)
resources = [resolve_resource_type(resource)]
resource_type = registration.get_resource(document_resource_name)
for resource_name, type_field in resources:
if not resource_type:
document_resource_name = d.get(type_field, None)
if not resource_type:
attrs = []
if document_resource_name:
errors = {}
resource_type = registration.get_resource(document_resource_name)
resource_type = registration.get_resource(resource_name)
for f in resource_type._meta.fields:
if not resource_type:
value = d.pop(f.name, NOT_PROVIDED)
if errors:
if document_resource_name:
if value is NOT_PROVIDED:
new_resource = resource_type(*attrs)
if resource_name == document_resource_name or resource_name in resource_type._meta.parent_resource_names:
value = f.get_default() if f.use_default_if_not_provided else None
value = f.to_python(value)
errors[f.name] = ve.error_messages
attrs.append(value)
if d:
new_resource.extra_attrs(d)
if full_clean:
new_resource.full_clean()
return new_resource
