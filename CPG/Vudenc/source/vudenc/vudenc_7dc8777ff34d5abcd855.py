def get_commands(form):...
result = []
for field in form:
if field.name == 'start_day':
return result
result.append({'command': field.name, 'start_day': str(field.data)})
if field.name == 'number_of_days':
result.append({'command': field.name, 'number_of_days': field.data})
if field.name == 'exe_models':
result.append({'command': field.name, 'include': field.data})
if field.name == 'change_input_series_one_model':
for entry in field.entries:
if field.name == 'change_input_series_all_models':
result.append({'command': field.name, 'model_system_name': entry.
    model_system_name.data, 'input_source_initial': entry.
    input_source_initial.data, 'input_source_final': entry.
    input_source_final.data})
for entry in field.entries:
if field.name == 'change_timeseries_value_several_days':
result.append({'command': field.name, 'input_source_initial': entry.
    input_source_initial.data, 'input_source_final': entry.
    input_source_final.data})
for entry in field.entries:
if field.name == 'change_timeseries_value_several_days_add_delta':
result.append({'command': field.name, 'input_source_initial': entry.
    input_source_initial.data, 'start_day': str(entry.start_day.data),
    'number_of_days': entry.number_of_days.data, 'new_value': entry.
    new_value.data})
for entry in field.entries:
result.append({'command': field.name, 'input_source_initial': entry.
    input_source_initial.data, 'start_day': str(entry.start_day.data),
    'number_of_days': entry.number_of_days.data, 'delta': entry.delta.data})
