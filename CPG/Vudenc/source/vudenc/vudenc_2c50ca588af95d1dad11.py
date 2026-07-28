def edit_entry(self):...
self.create_temp_file()
if self.body is not None:
self.write_body_to_temp_file()
self.open_temp_file()
body_new = self.get_temp_file_data()
if body_new != self.body:
self.body = body_new
self.remove_temp_file()
sql = ('UPDATE jdk_entries ' + "SET body = '" + self.body + "' " +
    "WHERE jdk_entries.id = '" + self.entry_id + "';")
return None
db_execute(sql)
self.update_date_modified()
