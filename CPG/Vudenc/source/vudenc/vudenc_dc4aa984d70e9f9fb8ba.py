def init_data(self):...
"""docstring"""
test_user = User(data=NEW_COMPLETED_SIGNUP_USER_EXAMPLE)
self.app.central_userdb.save(test_user, check_sync=False)
