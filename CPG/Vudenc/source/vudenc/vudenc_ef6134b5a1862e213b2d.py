def get(self, dataset, *args, **kwargs):...
dataset = db.get_dataset(dataset)
users = db.User.select()
access = db.DatasetAccessPending.select().where(db.DatasetAccessPending.
    dataset == dataset)
query = peewee.prefetch(users, access)
self.finish({'data': self._build_json_response(query, lambda u: u.
    access_pending_prefetch)})
