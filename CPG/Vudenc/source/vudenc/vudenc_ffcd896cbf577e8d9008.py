def update(self, model_id):...
"""docstring"""
model = self.session.query(self.resource_type).get(model_id)
if model is None:
for attribute, value in self.data.items():
setattr(model, attribute, value)
self.session.add(model)
return model
