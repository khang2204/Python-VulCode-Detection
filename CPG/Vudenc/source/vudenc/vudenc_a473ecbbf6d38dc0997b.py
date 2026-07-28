def _get_relatee(self, attribute):...
"""docstring"""
rel = self._relationships[attribute.entity_attr]
return rel.relatee
