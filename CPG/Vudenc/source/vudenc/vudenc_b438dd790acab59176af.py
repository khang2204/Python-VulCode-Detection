def __init__(self, *args, **kwargs):...
campaign = kwargs['campaign']
super(event_filter, self).__init__(*args, **kwargs)
event_type_choices = self.event_choices(campaign, 'event_type')
self.filters['event_type'].extra.update(choices=event_type_choices)
self.filters['event_type'].widget.attrs['size'] = min(len(
    event_type_choices), 10)
source_choices = self.event_choices(campaign, 'source')
self.filters['source'].extra.update(choices=source_choices)
self.filters['source'].widget.attrs['size'] = min(len(source_choices), 10)
