def new_unique_file(self, content):...
"""docstring"""
n_uuid = get_new_uuid(None, self.st_uuid_idx)
n_size = len(content)
n_count = 1
n_hash = self.hash_algo(content).hexdigest()
u_fl = self.UniqueFile(n_uuid, n_size, n_count, n_hash, master=self)
content = binascii.hexlify(content).decode('ascii')
self.st_db.execute(
    "INSERT INTO file_storage (uuid, size, count, hash, content) VALUES ('%s', %d, %d, '%s', E'\\x%s');"
     % (n_uuid, n_size, n_count, n_hash, content))
self.st_uuid_idx[n_uuid] = u_fl
self.st_hash_idx[n_hash] = u_fl
return n_uuid
