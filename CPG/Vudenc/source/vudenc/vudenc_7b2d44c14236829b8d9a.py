def post(self, dataset, email):...
dataset = db.get_dataset(dataset)
user = db.User.select().where(db.User.email == email).get()
db.UserAccessLog.create(user=user, dataset=dataset, action='access_revoked')
