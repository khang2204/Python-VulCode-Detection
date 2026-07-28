def can_subscribe(self, event):...
can_subscribe = False
event_type = str(event.event_type_id.name).lower()
event_start = datetime.strptime(event.date_begin, '%Y-%m-%d %H:%M:%S')
if event_type == 'open' and len(self.fit_subscriptions) > 0:
_logger.info('Can subscribe for open event id: %s, name: %s', event.
    event_type_id.name, event.name)
if event_start < datetime.now():
return True
return False
if event_start + relativedelta(hours=-24) > datetime.now(
return False
for subscription in self.fit_subscriptions:
if subscription._can_subscribe(event.event_type_id):
return can_subscribe
_logger.info('Can subscribe for event id: %s, name: %s', event.
    event_type_id.name, event.name)
can_subscribe = True
