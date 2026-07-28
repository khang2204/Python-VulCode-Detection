def _save_passwords(self):...
"""docstring"""
if self.flags.ignore_save_passwords is True:
return
for df in self.meta.get('fields', {'fieldtype': ('=', 'Password')}):
if self.flags.ignore_save_passwords and df.fieldname in self.flags.ignore_save_passwords:
new_password = self.get(df.fieldname)
if new_password and not self.is_dummy_password(new_password):
set_encrypted_password(self.doctype, self.name, new_password, df.fieldname)
self.set(df.fieldname, '*' * len(new_password))
