def start_automatic_event_creation(self):...
repeating_event_ids = self.env['event.event'].search([(
    'fit_repetition_enabled', '=', True)])
for repeating_event in repeating_event_ids:
_logger.info('Found repeating event: ' + repeating_event.name)
if repeating_event.fit_repetition == 'daily':
self._handle_daily_event_repetition(repeating_event)
if repeating_event.fit_repetition == 'weekly':
self._handle_weekly_event_repetition(repeating_event)
if repeating_event.fit_repetition == 'monthly':
self._handle_montly_event_repetition(repeating_event)
