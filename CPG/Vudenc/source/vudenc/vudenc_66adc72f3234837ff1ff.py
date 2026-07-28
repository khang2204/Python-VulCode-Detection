def get(self, dataset, *args, **kwargs):...
user = self.current_user
name = user.name
email = user.email
logging.info('Request: ' + name + ' ' + email)
self.finish(json.dumps({'user': name, 'email': email}))
