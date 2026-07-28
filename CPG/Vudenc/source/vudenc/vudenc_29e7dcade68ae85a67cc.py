def get(self, dataset):...
user = self.current_user
dataset = db.get_dataset(dataset)
versions = db.DatasetVersion.select(db.DatasetVersion.version, db.
    DatasetVersion.available_from).where(db.DatasetVersion.dataset == dataset)
logging.info('ListDatasetVersions')
data = []
found_current = False
for v in reversed(versions):
current = False
self.finish({'data': data})
future = False
if v.available_from > datetime.now():
if not (user and user.is_admin(dataset)):
if not found_current and v.available_from < datetime.now():
future = True
found_current = True
data.insert(0, {'name': v.version, 'available_from': v.available_from.
    strftime('%Y-%m-%d'), 'current': current, 'future': future})
current = True
