def __init__(self, *args, **kwargs):...
fields = []
defaults = {'widget': self.widget, 'max_length': kwargs.pop('max_length', None)
    }
self.scheme_name = kwargs.pop('scheme')
self.scheme = PERSON_NAME_SCHEMES.get(self.scheme_name)
self.one_required = kwargs.get('required', True)
require_all_fields = kwargs.pop('require_all_fields', False)
kwargs['required'] = False
kwargs['widget'] = (kwargs.get('widget') or self.widget)(scheme=self.scheme,
    field=self, **kwargs.pop('widget_kwargs', {}))
defaults.update(**kwargs)
for fname, label, size in self.scheme['fields']:
defaults['label'] = label
super().__init__(*args, fields=fields, require_all_fields=False, **kwargs)
field = forms.CharField(**defaults)
self.require_all_fields = require_all_fields
field.part_name = fname
self.required = self.one_required
fields.append(field)
