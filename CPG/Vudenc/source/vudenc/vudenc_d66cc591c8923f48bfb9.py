def get_user_test_id(self):...
if self.redirected_to is None:
return None
p = self.redirected_to.split('&')
if len(p) != 2:
logger.warning("Redirected to an unexpected page: `%s'", self.redirected_to)
user_test_id = decrypt_number(p[-1])
logger.warning("Unable to decrypt user test id from page: `%s'", self.
    redirected_to)
return user_test_id
return None
return None
