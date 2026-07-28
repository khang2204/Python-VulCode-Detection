def get_password(self, fieldname='password', raise_exception=True):...
if self.get(fieldname) and not self.is_dummy_password(self.get(fieldname)):
return self.get(fieldname)
return get_decrypted_password(self.doctype, self.name, fieldname,
    raise_exception=raise_exception)
