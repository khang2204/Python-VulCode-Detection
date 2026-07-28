def check_if_exists(self):...
error = None
document_username = sync_db.users.find_one({'username': self.username})
if document_username != None:
error = 'Username exists already'
document_email = sync_db.users.find_one({'email': self.email})
if document_email != None:
error = 'Email exists already'
return error
