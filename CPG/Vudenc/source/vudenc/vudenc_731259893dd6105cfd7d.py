def hash_password(self):...
ph = PasswordHasher()
hashed_password = ph.hash(self.password)
ph.verify(hashed_password, self.password)
hashed_password = ph.hash(self.password)
return hashed_password
