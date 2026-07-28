def __init__(self, *args, **kwargs):...
campaign = kwargs['campaign']
super(injection_filter, self).__init__(*args, **kwargs)
bit_choices = self.injection_choices(campaign, 'bit')
self.filters['bit'].extra.update(choices=bit_choices)
self.filters['bit'].widget.attrs['size'] = min(len(bit_choices), 10)
checkpoint_number_choices = self.injection_choices(campaign,
    'checkpoint_number')
self.filters['checkpoint_number'].extra.update(choices=
    checkpoint_number_choices)
self.filters['checkpoint_number'].widget.attrs['size'] = min(len(
    checkpoint_number_choices), 10)
field_choices = self.injection_choices(campaign, 'field')
self.filters['field'].extra.update(choices=field_choices)
self.filters['field'].widget.attrs['size'] = min(len(field_choices), 10)
register_choices = self.injection_choices(campaign, 'register')
self.filters['register'].extra.update(choices=register_choices)
self.filters['register'].widget.attrs['size'] = min(len(register_choices), 10)
register_index_choices = self.injection_choices(campaign, 'register_index')
self.filters['register_index'].extra.update(choices=register_index_choices)
self.filters['register_index'].widget.attrs['size'] = min(len(
    register_index_choices), 10)
num_injections_choices = result_choices(campaign, 'num_injections')
self.filters['result__num_injections'].extra.update(choices=
    num_injections_choices)
self.filters['result__num_injections'].widget.attrs['size'] = min(len(
    num_injections_choices), 10)
outcome_choices = result_choices(campaign, 'outcome')
self.filters['result__outcome'].extra.update(choices=outcome_choices)
self.filters['result__outcome'].widget.attrs['size'] = min(len(
    outcome_choices), 10)
outcome_category_choices = result_choices(campaign, 'outcome_category')
self.filters['result__outcome_category'].extra.update(choices=
    outcome_category_choices)
self.filters['result__outcome_category'].widget.attrs['size'] = min(len(
    outcome_category_choices), 10)
self.filters['success'].extra.update(help_text='')
target_choices = self.injection_choices(campaign, 'target')
self.filters['target'].extra.update(choices=target_choices)
self.filters['target'].widget.attrs['size'] = min(len(target_choices), 10)
target_index_choices = self.injection_choices(campaign, 'target_index')
self.filters['target_index'].extra.update(choices=target_index_choices)
self.filters['target_index'].widget.attrs['size'] = min(len(
    target_index_choices), 10)
