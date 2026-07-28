def get(self):...
items = db.GqlQuery('SELECT * FROM Item ORDER BY created_at DESC')
is_admin = database.users.is_current_user_admin()
database.render_template(self, 'items/index.html', {'items': items})
