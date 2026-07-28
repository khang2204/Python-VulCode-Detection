def update_user_settings(self):...
user_settings = json.loads(get_user_settings(self.doctype))
if hasattr(self, 'user_settings'):
user_settings.update(self.user_settings)
if self.save_user_settings_fields:
user_settings['fields'] = self.user_settings_fields
update_user_settings(self.doctype, user_settings)
