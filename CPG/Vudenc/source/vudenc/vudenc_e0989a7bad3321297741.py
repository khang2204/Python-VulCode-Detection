def update_title(self, title=None):...
if not self.title:
self.title = title
sql = ("UPDATE jdk_entries SET title = '" + self.title + "'" +
    "WHERE jdk_entries.id = '" + self.entry_id + "';")
db_execute(sql)
self.update_date_modified()
return None
