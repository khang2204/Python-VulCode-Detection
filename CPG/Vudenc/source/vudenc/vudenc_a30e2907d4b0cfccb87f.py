def get(self):...
user = self.current_user
ret = []
if user:
futures = db.DatasetVersion.select().join(db.Dataset).join(db.DatasetAccess
    ).where(db.DatasetVersion.available_from > datetime.now(), db.
    DatasetAccess.user == user, db.DatasetAccess.is_admin)
for version in db.DatasetVersionCurrent.select():
for f in futures:
dataset = build_dataset_structure(version, user)
self.finish({'data': ret})
dataset = build_dataset_structure(f, user)
dataset['current'] = True
dataset['future'] = True
ret.append(dataset)
ret.append(dataset)
