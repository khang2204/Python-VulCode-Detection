def log_event(self, level, source, event_type, description=None, campaign=...
if description == self.log_trace:
description = ''.join(format_stack()[:-2])
if description == self.log_exception:
event = {'description': description, 'event_type': event_type, 'level':
    level, 'source': source, 'success': success, 'timestamp': None}
description = ''.join(format_exc())
if self.result and not campaign:
event['result_id'] = self.result['id']
event['campaign_id'] = self.campaign['id']
self.insert('event', event)
return event
