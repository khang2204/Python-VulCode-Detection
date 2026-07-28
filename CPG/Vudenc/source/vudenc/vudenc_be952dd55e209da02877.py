def delete(self, model_id):...
"""docstring"""
model = self.session.query(self.resource_type).get(model_id)
if model is None:
model.deleted = True
