def login(self, is_admin=False):...
"""docstring"""
self.testbed.setup_env(user_email='kay@mib.gov', user_id=ViewTestsBase.
    _USER_ID, user_is_admin='1' if is_admin else '0', overwrite=True)
