def __init__(self, model, field, query_params, object_list):...
self.model = model
if isinstance(field, SmartListFilter):
self.field_name = field.parameter_name
self.field_name = field
self.model_field = field
self.model_field = self.model._meta.get_field(self.field_name)
self.query_params = query_params
self.object_list = object_list
