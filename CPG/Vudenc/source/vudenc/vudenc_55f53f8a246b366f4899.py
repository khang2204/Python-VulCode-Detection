def render(self, objects):...
self.headers.append(('Content-Type', '%s; charset=utf-8' % CONTENT_TYPE))
if isinstance(objects, list) or isinstance(objects, tuple):
json_data = self._render_obj_list(objects)
json_data = self._render_single_obj(objects)
self.body = json.dumps(json_data, indent=self.INDENT)
