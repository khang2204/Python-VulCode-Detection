def post(self):...
user = database.users.get_current_user()
if user:
item = database.Item()
self.redirect('/')
item.title = cgi.escape(self.request.get('title'))
item.description = cgi.escape(self.request.get('description'))
item.price = '%.2f' % float(cgi.escape(self.request.get('price')))
item.created_by_id = user.user_id()
item.put()
database.logging.info(
    """Created a new item.
Title: %s
Description: %s
Price: %s
CreatedBy: %s"""
    , item.title, item.description, item.price, item.created_by_id)
self.redirect('/items/')
