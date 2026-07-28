async def do_insert(self, hashed_password):...
document = {'username': self.username, 'email': self.email, 'password':
    hashed_password}
result = await async_db.users.insert_one(document)
