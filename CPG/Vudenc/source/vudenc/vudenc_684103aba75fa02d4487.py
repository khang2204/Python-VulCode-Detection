def __init__(self, *args, **kwargs):...
super(CleanCompDataForm, self).__init__(*args, **kwargs)
self.fields['script_selection'].widget.attrs.update({'style':
    'height:2.75rem; !important'})
self.fields['clean_comp_data_file'].widget.attrs.update({'accept': '.csv'})
self.collapsed = True
