def get(self, dataset, *args, **kwargs):...
dataset = db.get_dataset(dataset)
users = db.User.select()
access = db.DatasetAccessCurrent.select().where(db.DatasetAccessCurrent.
    dataset == dataset)
query = peewee.prefetch(users, access)
self.finish({'data': self._build_json_response(query, lambda u: u.
    access_current_prefetch)})
