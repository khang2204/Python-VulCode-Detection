def get(self):...
item = db.get(db.Key.from_path('Item', int(self.request.get('item_id'))))
li = db.GqlQuery('SELECT * FROM LoginInformation WHERE user_id = :1', item.
    created_by_id).get()
database.render_template(self, 'items/view_item.html', {'item': item, 'li': li}
    )
