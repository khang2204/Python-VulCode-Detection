def get_submission_id(self):...
if self.redirected_to is None:
return None
p = self.redirected_to.split('?')
if len(p) != 2:
logger.warning("Redirected to an unexpected page: `%s'", self.redirected_to)
submission_id = decrypt_number(p[-1])
logger.warning("Unable to decrypt submission id from page: `%s'", self.
    redirected_to)
return submission_id
return None
return None
