def text_input(self, name, value):...
"""docstring"""
if isinstance(value, unicode):
if isinstance(value, str):
return u'<input name="%s" value="%s" size=%d>' % (html_escape(name),
    html_escape(value), self.input_size)
value = value.decode('utf-8')
if value is not None:
value = str(value)
value = ''
