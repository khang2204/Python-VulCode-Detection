def check_database(self):...
ph = PasswordHasher()
error = None
document_username = sync_db.users.find_one({'username': self.username})
if document_username == None:
error = "User doesn't exist. Please sign up first!"
if ph.verify(document_username['password'], self.password) == False:
return error
error = 'Password is wrong, try again!'
