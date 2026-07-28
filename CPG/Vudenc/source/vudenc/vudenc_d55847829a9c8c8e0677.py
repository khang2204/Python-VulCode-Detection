def create_event(subject='_Test Event', starts_on=None):...
"""docstring"""
from frappe.utils import get_datetime
event = frappe.get_doc({'doctype': 'Event', 'subject': subject,
    'event_type': 'Public', 'starts_on': get_datetime(starts_on)}).insert(
    ignore_permissions=True)
return event
