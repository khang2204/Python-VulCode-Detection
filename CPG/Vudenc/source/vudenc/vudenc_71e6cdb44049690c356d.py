def get(self):...
user = database.users.get_current_user()
if user:
item = db.get(db.Key.from_path('Item', int(self.request.get('item_id'))))
self.redirect(self.request.referer)
if item.created_by_id == user.user_id(
database.logging.info('Deleting item with id %s', item.key().id())
database.db.delete(item)
