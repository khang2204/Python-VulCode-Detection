def get(self, dataset, version=None):...
user = self.current_user
current_version = False
future_version = False
dataset = db.get_dataset(dataset)
if version:
version = db.DatasetVersion.select().where(db.DatasetVersion.version ==
    version, db.DatasetVersion.dataset == dataset).get()
version = dataset.current_version.get()
if version.available_from > datetime.now():
current_version = True
if not (user and user.is_admin(dataset)):
if not current_version:
self.send_error(status_code=403)
future_version = True
cv = dataset.current_version.get()
ret = build_dataset_structure(version, user, dataset)
return
current_version = cv.version == version.version
ret['current'] = current_version
ret['future'] = future_version
self.finish(ret)
