def get(self):...
user = database.users.get_current_user()
if user:
item = db.get(db.Key.from_path('Item', int(self.request.get('item_id'))))
self.redirect('/')
database.render_template(self, 'items/edit_item.html', {'item': item})
