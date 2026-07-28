def get(self):...
if database.users.get_current_user():
database.render_template(self, 'items/new_item.html', {})
self.redirect('/')
