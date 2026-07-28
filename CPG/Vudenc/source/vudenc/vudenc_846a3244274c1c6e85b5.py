def get_inputs_choices_by_model(name):...
models = load_json('models.json')
model = next(item for item in models if item['model_system_name'] == name)
return [(value['series_name_system'], value['series_name_system'] + ':' +
    value['series_name_user']) for key, value in model['inputs'].iteritems()]
