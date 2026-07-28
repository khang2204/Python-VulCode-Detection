def post(self):...
user = database.users.get_current_user()
if user:
item = db.get(db.Key.from_path('Item', int(cgi.escape(self.request.get(
    'item_id')))))
self.redirect('/')
item.title = cgi.escape(self.request.get('title'))
item.description = cgi.escape(self.request.get('description'))
item.price = cgi.escape(self.request.get('price'))
database.logging.info(
    """Item #%s changed to:
Title: %s
Description: %s
Price: %s""", item.
    key().id(), item.title, item.description, item.price)
item.put()
self.redirect('/items/my_items')
