def resolve_resource_type(resource):...
if isinstance(resource, type) and issubclass(resource, Resource):
return resource._meta.resource_name, resource._meta.type_field
return resource, DEFAULT_TYPE_FIELD
