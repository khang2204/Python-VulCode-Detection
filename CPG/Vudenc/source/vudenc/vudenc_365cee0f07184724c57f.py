def make_input(self, version, name, value, attribute):...
options = []
if value is None:
value = ''
for choice in ([''] + attribute.values):
message = get_message(version, 'attribute_value', choice)
return '<select name="%s">%s</select>' % (html_escape(name), ''.join(options))
title = html_escape(message or _('(unspecified)'))
selected = value == choice and 'selected' or ''
options.append('<option value="%s" %s>%s</option>' % (choice, selected, title))
