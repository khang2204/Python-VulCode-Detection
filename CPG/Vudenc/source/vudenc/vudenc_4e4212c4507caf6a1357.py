def __init__(self, scheme: dict, field: forms.Field, attrs=None):...
widgets = []
self.scheme = scheme
self.field = field
for fname, label, size in self.scheme['fields']:
a = copy.copy(attrs) or {}
super().__init__(widgets, attrs)
a['data-fname'] = fname
widgets.append(self.widget(attrs=a))
