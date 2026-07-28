def _create_new_event(self, old_repeating_event, new_start_date, new_end_date):...
_logger.info('Start creation new repeating event')
new_repeating_event = old_repeating_event.copy(default={'website_published':
    True})
new_repeating_event.date_end = new_end_date
new_repeating_event.date_begin = new_start_date
old_repeating_event.fit_repetition_enabled = False
old_repeating_event.fit_repetition = ''
