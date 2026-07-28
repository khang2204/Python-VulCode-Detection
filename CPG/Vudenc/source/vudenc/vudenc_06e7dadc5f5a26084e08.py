def _event_does_not_exist(self, old_repeating_event, new_end_date):...
_logger.info('Checking new event existence: ' + old_repeating_event.name +
    ', date: ' + str(new_end_date))
old_event_cat = old_repeating_event.event_type_id.id
existing_event = self.env['event.event'].search([('event_type_id', '=',
    old_event_cat), ('date_end', '=', str(new_end_date))])
if existing_event:
return False
return True
