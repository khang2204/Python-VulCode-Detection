def __init__(self, *args, **kwargs):...
self.campaign = kwargs['campaign']
super(simics_register_diff_filter, self).__init__(*args, **kwargs)
self.queryset = kwargs['queryset']
checkpoint_number_choices = self.simics_register_diff_choices(
    'checkpoint_number')
self.filters['checkpoint_number'].extra.update(choices=
    checkpoint_number_choices)
self.filters['checkpoint_number'].widget.attrs['size'] = min(len(
    checkpoint_number_choices), 10)
register_choices = self.simics_register_diff_choices('register')
self.filters['register'].extra.update(choices=register_choices)
self.filters['register'].widget.attrs['size'] = min(len(register_choices), 10)
