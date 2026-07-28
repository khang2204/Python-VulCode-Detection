def _render_single_obj(self, obj):...
"""docstring"""
if 'category_discovery' not in obj.render_flags:
category_headers = HeaderRenderer.category_headers(obj)
return self._json_obj(obj)
[self.headers.append(('Category', h)) for h in category_headers.headers()]
