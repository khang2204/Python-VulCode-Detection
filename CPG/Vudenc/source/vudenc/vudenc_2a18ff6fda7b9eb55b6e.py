def __init__(self, entry_id=None, title=None, writeable=True):...
if entry_id:
self.entry_id = entry_id
self.create_entry()
self.populate_entry_data()
self.set_entry_id()
self.writeable = writeable
if title:
self.title = title
self.update_title()
