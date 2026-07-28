def _confirmation(self, win):...
"""docstring"""
if win['id'] in self.table_maps['confirmations']:
confirmation = self.table_maps['confirmations'][win['id']][0]
confirmation = None
values = [('customer response recieved', self._val_to_str(bool(confirmation)))]
for field_name in self.customerresponse_fields:
if field_name in ['win']:
return values
model_field = self._get_customerresponse_field(field_name)
if confirmation:
if model_field.choices:
value = ''
display_fn = getattr(confirmation, 'get_{0}_display'.format(field_name))
value = getattr(confirmation, field_name)
model_field_name = model_field.verbose_name or model_field.name
value = display_fn()
if model_field_name == 'created':
csv_field_name = 'date response received'
csv_field_name = model_field_name
if value:
values.append((csv_field_name, self._val_to_str(value)))
value = value.date()
