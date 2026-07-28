@gen.coroutine...
cursor = collection.find()
cursor.sort([('date', -1)]).limit(1)
document = None
while (yield cursor.fetch_next):
document = cursor.next_object()
if document:
date = document['date']
articles = build_json_from_raw_data()
articles = build_json_from_raw_data(ch_date=date)
if len(articles) > 0:
bulk_insert(collection, articles)
