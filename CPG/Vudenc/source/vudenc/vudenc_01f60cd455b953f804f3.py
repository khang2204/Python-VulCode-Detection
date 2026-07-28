def _get_win_data(self, win):...
"""docstring"""
win_data = collections.OrderedDict()
for field_name in self.win_fields:
if field_name in self.IGNORE_FIELDS:
win_data['contributing advisors/team'] = ', '.join(map(str, self.table_maps
    ['advisors'][win['id']]))
model_field = self._get_win_field(field_name)
notifications = self.table_maps['notifications'][win['id']]
if field_name == 'user':
email_sent = bool(notifications or win['complete'])
value = str(self.users_map[win['user_id']])
if field_name == 'created':
win_data['customer email sent'] = self._val_to_str(email_sent)
if model_field.choices and value:
value = win[field_name].date()
if field_name == 'cdms_reference':
if notifications:
comma_fields = ['total_expected_export_value',
    'total_expected_non_export_value', 'total_expected_odi_value']
value = self._choices_dict(model_field.choices)[value]
if model_field.attname == 'hvc':
model_field_name = model_field.verbose_name or model_field.name
value = win[field_name]
value = win[field_name]
win_data['customer email date'] = str(notifications[0].created.date())
if win['complete']:
if field_name in comma_fields:
value = value
win_data[model_field_name] = self._val_to_str(value)
int(value)
if value.startswith('0'):
win_data.update(self._extract_breakdowns(win))
win_data['customer email date'] = '[manual]'
win_data['customer email date'] = ''
value = '£{:,}'.format(value)
value = "'" + value
win_data.update(self._confirmation(win))
return win_data
