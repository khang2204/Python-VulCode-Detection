def test_between_filters(self):...
"""docstring"""
frappe.db.sql('delete from tabEvent')
todays_event = create_event()
event1 = create_event(starts_on='2016-07-05 23:59:59')
event2 = create_event(starts_on='2016-07-06 00:00:00')
event3 = create_event(starts_on='2016-07-07 23:59:59')
event4 = create_event(starts_on='2016-07-08 00:00:01')
data = DatabaseQuery('Event').execute(filters={'starts_on': ['between',
    None]}, fields=['name'])
self.assertTrue({'name': event1.name} not in data)
data = DatabaseQuery('Event').execute(filters={'starts_on': ['between', [
    '2016-07-06', '2016-07-07']]}, fields=['name'])
self.assertTrue({'name': event2.name} in data)
self.assertTrue({'name': event3.name} in data)
self.assertTrue({'name': event1.name} not in data)
self.assertTrue({'name': event4.name} not in data)
data = DatabaseQuery('Event').execute(filters={'starts_on': ['between', [
    '2016-07-07']]}, fields=['name'])
self.assertTrue({'name': event3.name} in data)
self.assertTrue({'name': event4.name} in data)
self.assertTrue({'name': todays_event.name} in data)
self.assertTrue({'name': event1.name} not in data)
self.assertTrue({'name': event2.name} not in data)
