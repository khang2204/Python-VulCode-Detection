def _specific_fields(self, model_or_models, is_detail=True):...
"""docstring"""
fields = self._query_arg('fields', list)
if fields is None:
return model_or_models
if is_detail:
the_model = model_or_models
models = model_or_models
return get_fields_subset(the_model, fields)
return [get_fields_subset(model, fields) for model in models]
