def get_models_choices():...
models = load_json('models.json')
return [(model['model_system_name'], model['model_name_user'] + ':' + model
    ['author']) for model in models]
