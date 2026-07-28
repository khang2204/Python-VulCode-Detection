def new_file(self, telegram_id, name, mime, size, directory_id=None):...
if not directory_id:
directory_id = self.path[-1:][0]
return db.insert('file', {'name': name, 'mime': mime, 'size': size,
    'telegram_id': telegram_id, 'directory_id': directory_id, 'user_id':
    self.user_id})
