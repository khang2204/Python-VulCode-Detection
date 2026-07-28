@auth.autologin...
limit = int(self.request.get('limit', 100))
cursor = datastore_query.Cursor(urlsafe=self.request.get('cursor'))
errors_found, cursor, more = models.Error.query().order(-models.Error.
    created_ts).fetch_page(limit, start_cursor=cursor)
params = {'cursor': cursor.urlsafe() if cursor and more else None, 'errors':
    errors_found, 'limit': limit, 'now': utils.utcnow()}
self.response.out.write(template.render('ereporter2/errors.html', params))
