def post(self):...
query = cgi.escape(self.request.get('query'))
items = db.GqlQuery(
    'SELECT * FROM Item WHERE title = :1 ORDER BY created_at DESC', query)
database.render_template(self, 'items/search.html', {'items': items,
    'query': query})
