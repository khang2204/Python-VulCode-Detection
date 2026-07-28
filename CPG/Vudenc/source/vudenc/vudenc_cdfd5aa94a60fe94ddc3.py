def __init__(self, model, field, column_id, query_params,...
self.model = model
self.field_name = field
self.label = label
self.render_function = render_function
self.order_field = None
self.order = None
if not self.field_name:
return
if self.field_name.startswith('_') and self.field_name != '__str__':
self.model_field = self.model._meta.get_field(self.field_name)
self.model_field = None
if self.order_field:
self.order_field = self.field_name
field = getattr(self.model, self.field_name)
self.order_field = self.field_name
self.order = SmartOrder(query_params=query_params, column_id=column_id,
    ordering_query_param=ordering_query_param)
if callable(field) and getattr(field, 'admin_order_field', False):
self.order_field = getattr(field, 'admin_order_field')
if callable(field) and getattr(field, 'alters_data', False):
