def _render_obj_list(self, objects):...
"""docstring"""
json_data = []
for obj in objects:
json_data.append(self._json_obj(obj))
return json_data
