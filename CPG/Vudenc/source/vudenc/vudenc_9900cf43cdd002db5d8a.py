def run(self, name):...
if name:
cleaned = _force_ascii(name)
if cleaned == name:
abort(404, 'page not found')
return Tag._by_name(cleaned)
