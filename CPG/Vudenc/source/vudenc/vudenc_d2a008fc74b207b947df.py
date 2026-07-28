def page_render(self, page_json, template='app.html', **kw):...
if self.is_api:
self.write(page_json)
self.render(template, page_json=page_json, **kw)
