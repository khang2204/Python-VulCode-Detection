def get(self):...
user = database.users.get_current_user()
if user:
items = db.GqlQuery(
    'SELECT * FROM Item WHERE created_by_id = :1 ORDER BY created_at DESC',
    user.user_id())
self.redirect('/')
database.render_template(self, 'items/my_items.html', {'items': items})
