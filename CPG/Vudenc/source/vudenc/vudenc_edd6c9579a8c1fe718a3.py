def post(self, dataset, event, target):...
user = self.current_user
if event == 'consent':
dv = db.DatasetVersion.select().where(db.DatasetVersion.version == target).get(
    )
db.UserConsentLog.create(user=user, dataset_version=dv)
