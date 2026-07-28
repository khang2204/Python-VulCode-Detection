import database
from database import cgi
from database import db
def get(self):...
items = db.GqlQuery('SELECT * FROM Item ORDER BY created_at DESC')
is_admin = database.users.is_current_user_admin()
database.render_template(self, 'items/index.html', {'items': items})
def get(self):...
if database.users.get_current_user():
database.render_template(self, 'items/new_item.html', {})
self.redirect('/')
def get(self):...
item = db.get(db.Key.from_path('Item', int(self.request.get('item_id'))))
li = db.GqlQuery('SELECT * FROM LoginInformation WHERE user_id = :1', item.
    created_by_id).get()
database.render_template(self, 'items/view_item.html', {'item': item, 'li': li}
    )
def post(self):...
user = database.users.get_current_user()
if user:
item = database.Item()
self.redirect('/')
item.title = cgi.escape(self.request.get('title'))
def get(self):...
item.description = cgi.escape(self.request.get('description'))
user = database.users.get_current_user()
item.price = '%.2f' % float(cgi.escape(self.request.get('price')))
if user:
item.created_by_id = user.user_id()
item = db.get(db.Key.from_path('Item', int(self.request.get('item_id'))))
self.redirect(self.request.referer)
item.put()
if item.created_by_id == user.user_id(
def get(self):...
database.logging.info(
    """Created a new item.
Title: %s
Description: %s
Price: %s
CreatedBy: %s"""
    , item.title, item.description, item.price, item.created_by_id)
database.logging.info('Deleting item with id %s', item.key().id())
user = database.users.get_current_user()
self.redirect('/items/')
database.db.delete(item)
if user:
item = db.get(db.Key.from_path('Item', int(self.request.get('item_id'))))
self.redirect('/')
database.render_template(self, 'items/edit_item.html', {'item': item})
def post(self):...
user = database.users.get_current_user()
if user:
item = db.get(db.Key.from_path('Item', int(cgi.escape(self.request.get(
    'item_id')))))
self.redirect('/')
item.title = cgi.escape(self.request.get('title'))
def get(self):...
item.description = cgi.escape(self.request.get('description'))
user = database.users.get_current_user()
item.price = cgi.escape(self.request.get('price'))
if user:
database.logging.info(
    """Item #%s changed to:
Title: %s
Description: %s
Price: %s""", item.
    key().id(), item.title, item.description, item.price)
items = db.GqlQuery(
    'SELECT * FROM Item WHERE created_by_id = :1 ORDER BY created_at DESC',
    user.user_id())
self.redirect('/')
item.put()
database.render_template(self, 'items/my_items.html', {'items': items})
def post(self):...
self.redirect('/items/my_items')
query = cgi.escape(self.request.get('query'))
items = db.GqlQuery(
    'SELECT * FROM Item WHERE title = :1 ORDER BY created_at DESC', query)
database.render_template(self, 'items/search.html', {'items': items,
    'query': query})
app = database.webapp2.WSGIApplication([('/items/', MainHandler), (
    '/items/new_item', NewHandler), ('/items/save_item', SaveHandler), (
    '/items/view_item', ViewHandler), ('/items/search', SearchHandler), (
    '/items/my_items', ShopHandler), ('/items/delete_item', DeleteHandler),
    ('/items/edit_item', EditHandler), ('/items/update_item', UpdateHandler
    )], debug=True)
