def load_sql(self, db=Database):...
"""docstring"""
self.st_db = db
for item in self.st_db.execute(
s_uuid, s_size, s_count, s_hash = item
return
s_fl = self.UniqueFile(s_uuid, s_size, s_count, s_hash, self)
self.st_uuid_idx[s_uuid] = s_fl
self.st_hash_idx[s_hash] = s_fl
