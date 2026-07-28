def make_input(self, version, name, value, attribute):...
options = []
if value == True:
value = 'TRUE'
if value == False:
for choice, title in [('', _('(unspecified)')), ('TRUE', _('yes')), (
value = 'FALSE'
value = ''
selected = value == choice and 'selected' or ''
return '<select name="%s">%s</select>' % (html_escape(name), ''.join(options))
options.append('<option value="%s" %s>%s</option>' % (choice, selected, title))
