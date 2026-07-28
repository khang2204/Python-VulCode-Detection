def get_inputs_choices():...
models = load_json('models.json')
inputs_by_models = [get_inputs_choices_by_model(model['model_system_name']) for
    model in models]
return [item for inputs in inputs_by_models for item in inputs]
