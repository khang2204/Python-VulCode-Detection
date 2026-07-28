def can_unsubscribe(self, event):...
event_start = datetime.strptime(event.date_begin_located, '%Y-%m-%d %H:%M:%S')
if event_start < datetime.now():
return False
return True
