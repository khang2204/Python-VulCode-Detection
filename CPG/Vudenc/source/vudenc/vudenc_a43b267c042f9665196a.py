def render(self, name: str, value, attrs=None, renderer=None) ->str:...
if not isinstance(value, list):
value = self.decompress(value)
output = []
final_attrs = self.build_attrs(attrs or dict())
if 'required' in final_attrs:
id_ = final_attrs.get('id', None)
for i, widget in enumerate(self.widgets):
return mark_safe(self.format_output(output))
widget_value = value[i]
widget_value = None
if id_:
final_attrs = dict(final_attrs, id='%s_%s' % (id_, i), title=self.scheme[
    'fields'][i][1], placeholder=self.scheme['fields'][i][1])
output.append(widget.render(name + '_%s' % i, widget_value, final_attrs,
    renderer=renderer))
final_attrs['data-size'] = self.scheme['fields'][i][2]
