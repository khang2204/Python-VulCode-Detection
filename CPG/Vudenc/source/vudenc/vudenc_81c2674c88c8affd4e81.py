def __init__(self, *args, **kwargs):...
self.dg_type = kwargs.pop('dg_type', 0)
self.user = kwargs.pop('user', None)
super(ExtractionScriptForm, self).__init__(*args, **kwargs)
self.fields['weight_fraction_type'].widget.attrs.update({'style':
    'height:2.75rem; !important'})
self.fields['script_selection'].widget.attrs.update({'style':
    'height:2.75rem; !important'})
self.fields['extract_file'].widget.attrs.update({'accept': '.csv'})
if self.dg_type in ['FU', 'CP']:
self.collapsed = True
