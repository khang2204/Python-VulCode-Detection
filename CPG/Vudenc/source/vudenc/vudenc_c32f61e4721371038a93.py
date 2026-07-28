def post(self, dataset, *args, **kwargs):...
dataset = db.get_dataset(dataset)
email = self.get_argument('email', default='', strip=False)
affiliation = self.get_argument('affiliation', strip=False)
country = self.get_argument('country', strip=False)
newsletter = self.get_argument('newsletter', strip=False)
user = self.current_user
if user.email != email:
return
user.affiliation = affiliation
user.country = country
logging.info('Inserting into database: {}, {}'.format(user.name, user.email))
user.save()
logging.error(e)
da, _ = db.DatasetAccess.get_or_create(user=user, dataset=dataset)
da.wants_newsletter = newsletter
da.save()
db.UserAccessLog.create(user=user, dataset=dataset, action='access_requested')
