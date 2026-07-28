@gen.coroutine...
check_rss_updates(self.collection)
cursor = self.collection.find().sort([('date', -1)])
docs = yield cursor.to_list(length=20)
self.render('index.html', title=options.title, items=docs)
