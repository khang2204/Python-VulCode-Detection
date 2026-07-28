def verify_account(self, email, user_password):...
query = "SELECT Pass FROM user WHERE Email = '" + email + "'"
self.cursor.execute(query)
fetch = self.cursor.fetchone()
password = ' '.join(map(str, fetch))
return check_password_hash(password, user_password)
