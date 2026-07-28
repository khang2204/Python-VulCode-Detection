def _handle_monthly_event_repetition(self, old_repeating_event):...
_logger.info('Handling monthly repeating event')
end_date = datetime.strptime(old_repeating_event.date_end, '%Y-%m-%d %H:%M:00')
present = datetime.now()
if present >= end_date:
new_start_date = datetime.strptime(old_repeating_event.date_begin,
    '%Y-%m-%d %H:%M:00') + relativedelta(months=+1)
new_end_date = end_date + relativedelta(months=+1)
if self._event_does_not_exist(old_repeating_event, new_end_date):
self._create_new_event(old_repeating_event, new_start_date, new_end_date)
