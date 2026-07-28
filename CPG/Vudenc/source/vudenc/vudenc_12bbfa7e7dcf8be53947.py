def detail(self, model_id):...
"""docstring"""
model = self.session.query(self.resource_type).get(model_id)
if model is None:
return self._specific_fields(model)
