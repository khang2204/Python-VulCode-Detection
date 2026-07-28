def get_event(events, matches):...
for e in events['events']:
if all([(match in e) for match in matches]):
return None
return e
